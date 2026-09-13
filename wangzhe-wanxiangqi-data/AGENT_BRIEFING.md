# 王者万象棋资料采集简报（只限本游戏）

目标游戏：**王者万象棋**（腾讯天美，2026-09-10 全平台上线）。禁止用王者模拟战 / 其他自走棋规则补空。

## 已落地的原始文件

- `当前工作区/wangzhe-wanxiangqi-data/raw/wanxiangqiwiki.com_explorer-catalogs_hero.json`（86 英雄，官方 2026-08-28）
- `当前工作区/wangzhe-wanxiangqi-data/raw/wanxiangqiwiki.com_explorer-catalogs_effect.json`（98 效果牌）
- `当前工作区/wangzhe-wanxiangqi-data/raw/wanxiangqiwiki.com_explorer-catalogs_equipment.json`（73 装备）
- `当前工作区/wangzhe-wanxiangqi-data/raw/wanxiangqiwiki.com_explorer-catalogs_talent.json`（255 天赋）
- `当前工作区/wangzhe-wanxiangqi-data/raw/wanxiangqiwiki.com_lineup-featured-presets.json`（25 套阵容预设）
- `当前工作区/wangzhe-wanxiangqi-data/raw/wiki-knowledge-payload-0.json`（机制词典）

## 权威来源（按优先级）

1. 王者万象棋 wiki：https://wanxiangqiwiki.com/explore/hero-sulie 及 `/explore/hero-catalog`、`/explore/equipment-catalog`、`/explore/effect-catalog`、`/explore/talent-catalog`、`/mechanics`、`/lineups`
2. 官方新手指引：https://wxq.qq.com/cp/a202609xszy/index.html
3. 官网：https://wxq.qq.com/
4. 官方卡图 CDN：https://assets.wanxiangqiwiki.com/ 、https://game.gtimg.cn/images/osgame/cp/a202609xszy/

## 交付目录

- JSON/CSV → `当前工作区/wangzhe-wanxiangqi-data/json/`
- Markdown → `当前工作区/wangzhe-wanxiangqi-data/markdown/`
- 图片原图 → `当前工作区/wangzhe-wanxiangqi-data/images/`
- 截图 → `当前工作区/wangzhe-wanxiangqi-data/screenshots/`
- 图片对应表 → `当前工作区/wangzhe-wanxiangqi-data/json/image_index.json`

每项必须带：来源链接、适用版本、更新时间、证据层级（官方规则 / 作者经验 / 推测）。冲突和未知单独列出。

## 2026-09-13 收尾

- Markdown：`00-INDEX.md`、`02-lineups.md`、`04-decisions.md`、`05-operations.md`
- 自动化 3 套：日落海整备流、常小娥四人队、大河图腾流（未选香香开团射）
- `heroes.json` 的 `lineups` = 自动化标签；原 wiki 预设在 `wiki_featured_presets`
- 截图 57/57 对齐；补下大司命/敖隐/东皇太一/干将莫邪卡图
- `lineups.json` id：大司命 `hero-5171`，东皇太一 `hero-donghuang`
