#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
拉取 image_index.json 中尚未落盘的图片（url_only 项），并把结果写回索引。

用法（在仓库根目录运行）：
    python3 wangzhe-wanxiangqi-data/scripts/fetch_remaining_images.py
    python3 wangzhe-wanxiangqi-data/scripts/fetch_remaining_images.py --owner-type hero
    python3 wangzhe-wanxiangqi-data/scripts/fetch_remaining_images.py --kind card --limit 50
    python3 wangzhe-wanxiangqi-data/scripts/fetch_remaining_images.py --dry-run

说明：
- 只下载 download_status == "url_only" 的条目；已 ok / fail 的跳过。
- 若本地文件已存在（例如之前手动补下但索引未标记），直接标记为 ok，不重复下载。
- 每下载成功一条就写回 image_index.json（可中断续跑）。
- 断点续传：再次运行会自动跳过已完成条目。
"""

import argparse
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # wangzhe-wanxiangqi-data/
INDEX_PATH = os.path.join(ROOT, "json", "image_index.json")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def load_index():
    with open(INDEX_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_index(data):
    tmp = INDEX_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, INDEX_PATH)


def recalc_counts(data):
    items = data.get("items", [])
    data["count"] = len(items)
    data["download_ok"] = sum(1 for it in items if it.get("download_status") == "ok")
    data["download_fail"] = sum(1 for it in items if it.get("download_status") == "fail")
    data["url_only"] = sum(1 for it in items if it.get("download_status") == "url_only")


def download(url, timeout=30, retries=3):
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(min(2 ** attempt, 8))
    raise last_err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--owner-type", choices=["hero", "effect", "equipment", "talent", "chessplayer"],
                    help="只下载该 owner_type")
    ap.add_argument("--kind", help="只下载该 kind（如 card / awake_card / thumbnail / skill_icon / portrait）")
    ap.add_argument("--limit", type=int, default=0, help="最多下载条数（0 = 不限制）")
    ap.add_argument("--dry-run", action="store_true", help="只打印计划，不下载")
    args = ap.parse_args()

    data = load_index()
    items = data.get("items", [])

    todo = [it for it in items if it.get("download_status") == "url_only" and it.get("url")]
    if args.owner_type:
        todo = [it for it in todo if it.get("owner_type") == args.owner_type]
    if args.kind:
        todo = [it for it in todo if it.get("kind") == args.kind]
    if args.limit:
        todo = todo[:args.limit]

    print(f"待处理 {len(todo)} 条（owner_type={args.owner_type or '全部'}，kind={args.kind or '全部'}）")

    if args.dry_run:
        for it in todo:
            print("  [dry-run]", it.get("local_path"), "<-", it.get("url"))
        return

    ok = fail = existed = 0
    for i, it in enumerate(todo, 1):
        local = it.get("local_path")
        if not local:
            continue
        abs_local = os.path.join(ROOT, local)
        os.makedirs(os.path.dirname(abs_local), exist_ok=True)

        if os.path.exists(abs_local) and os.path.getsize(abs_local) > 0:
            it["download_status"] = "ok"
            it["bytes"] = os.path.getsize(abs_local)
            existed += 1
            print(f"[{i}/{len(todo)}] 已存在 {local}")
            continue

        try:
            body = download(it["url"])
            with open(abs_local, "wb") as f:
                f.write(body)
            it["download_status"] = "ok"
            it["bytes"] = len(body)
            ok += 1
            print(f"[{i}/{len(todo)}] ok  {local}  ({len(body)} B)")
        except Exception as e:  # noqa: BLE001
            it["download_status"] = "fail"
            it["fail_reason"] = str(e)[:200]
            fail += 1
            print(f"[{i}/{len(todo)}] FAIL {local}  ({e})", file=sys.stderr)

        # 每 20 条写回一次，并逐条失败后也写回，保证可中断续跑
        if i % 20 == 0 or fail:
            recalc_counts(data)
            save_index(data)

    recalc_counts(data)
    save_index(data)

    print("\n完成：ok %d ｜ 已存在 %d ｜ 失败 %d" % (ok, existed, fail))
    print("索引已写回：count=%d ok=%d fail=%d url_only=%d" % (
        data["count"], data["download_ok"], data["download_fail"], data["url_only"]))


if __name__ == "__main__":
    main()
