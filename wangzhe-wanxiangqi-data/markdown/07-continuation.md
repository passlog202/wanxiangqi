# 07-续查记录（2026-09-13）

目标游戏：**王者万象棋**（腾讯天美，2026-09-10 全平台上线）。本文件记录 2026-09-13 当天继续“拉取文件 + 信息搜集整理”的结果，只覆盖本游戏，未用王者模拟战 / 其他自走棋规则补空。

## 一、拉取结果

- `git pull origin main`：已是最新（`Already up to date`），远程 `passlog202/wanxiangqi` 无新提交。
- 工作区数据与仓库 `main`（`7cd123a`）一致；本续查全部落在会话分支 `arena/01a098e7-wanxiangqi`。

## 二、线上来源复核（fetch_page 直连 wiki）

对权威来源逐项复核，与已落盘数据一致，未发现版本漂移：

| 来源 | 复核结果 |
|---|---|
| wiki 英雄目录 `/explore/hero-catalog` | 仍为 **英雄牌 86**（`currentCount=86` 与 `heroes.json` 一致） |
| wiki 机制页 `/mechanics/auction` | 拍卖回合 **4 / 8 / 12**、拍卖结束 **+3 经验**（与 `mechanics.json` 一致） |
| `/mechanics/player-experience` | 升级经验 **7 / 13 / 17 / 23 / 27**，战斗 +1、拍卖 +3、同回合不叠加（一致） |
| `/mechanics/population` | 上阵人数 **3 级、5 级各 +1**（一致；同时回答“6 级不再 +1”） |
| `/mechanics/synthesis` | 打出与场上同名英雄计 1 次合成；累计 **3 次合成 → 1 张效果锦囊**（一致） |
| `/mechanics/hero-shop-odds` | 按棋手等级的费用层概率表（6 行全表，一致） |
| `/mechanics/shared-pool` | 公共牌库 1阶14 / 2阶11 / 3阶9 / 4阶7 / 5阶6（一致，人工校准） |
| `/mechanics/equipment-acquisition` | 基础装备固定回合 **1 / 4 / 8 / 12 / 16**（一致，官网规则截图） |
| `/mechanics/talent-selection` | 升级 3 选 1 免费；铜/银/金三阶；同等级 6 名玩家品阶相同；白银段位每局可刷 1 次（一致） |
| `/mechanics/effect-card-odds` | wiki 明确：效果牌商店/拍卖/天赋候选**无**可复核权重（“待补资料”），与未知清单一致 |

结论：`mechanics.json`（26 条）、`rules.json`、`unknowns_conflicts.json` 均已完整收录上述内容，无需改写正文；本轮仅做交叉确认。

## 三、数据修正：`image_index.json` 去重

发现 2026-09-13 补下的 8 名英雄（大司命、敖隐、东皇太一、干将莫邪、牛魔、弈星、太乙真人、刘邦）× 3 种图（card/awake/thumbnail）在索引里被**追加成重复条目**（`url_only` 旧条目 + `ok` 新条目并存），导致 `items=1352` 而 `count=1328`、`url_only` 里含 24 条“文件其实已存在”的假缺口。

处理：按 `local_path` 去重，保留 `ok` 条目（含 `bytes` 与补下备注）。修正后：

- `items = 1328`（= `count`），无重复 `local_path`；
- `download_ok = 144`、`download_fail = 0`、`url_only = 1184`；
- “ok 条目缺文件”0 条、“url_only 条目文件已存在”0 条，索引与磁盘重新一致。

## 四、图片缺口与下载工具

索引现覆盖 **1328** 个图片条目，已落盘 **144**，待拉取 **1184**（`url_only`）。缺口分布：

| owner_type | 待拉取 | | kind | 待拉取 |
|---|---|---|---|---|
| talent | 538 | | thumbnail | 531 |
| hero | 276 | | card | 525 |
| effect | 202 | | skill_icon | 85 |
| equipment | 190 | | awake_card | 59 |
| chessplayer | 2 | | portrait | 6 |

英雄卡面缺口：86 名英雄中 **34 已下 / 52 待下**（3 套自动化阵容已全部齐图）。

**注意**：本会话沙箱只能直连 GitHub / PyPI 等白名单域名，`assets.wanxiangqiwiki.com`、`game.gtimg.cn` 的 HTTPS 出口被拦截（`SSL_ERROR_SYSCALL`），故本轮无法直接下载剩余原图。已提供可断点续跑的工具：

```bash
# 仓库根目录运行；在网络可访问 assets.wanxiangqiwiki.com 的环境执行
python3 wangzhe-wanxiangqi-data/scripts/fetch_remaining_images.py            # 全部
python3 wangzhe-wanxiangqi-data/scripts/fetch_remaining_images.py --owner-type hero
python3 wangzhe-wanxiangqi-data/scripts/fetch_remaining_images.py --kind card --limit 50
python3 wangzhe-wanxiangqi-data/scripts/fetch_remaining_images.py --dry-run  # 只看计划
```

脚本特性：只拉 `url_only`；本地已存在则直接标 `ok` 不重下；逐条写回 `image_index.json`（可中断续跑）；自动重算 `count / download_ok / download_fail / url_only`。

## 五、新增来源（待纳入索引）

- wiki **数值研究** `https://wanxiangqiwiki.com/analysis/dps`：逐英雄伤害时间轴模拟器（可算总伤害/秒伤/伤害类型/来源，含事件流水）。wiki 自身标注为“试验推算”，并明确 **40/100 级技能节点、召唤物、分裂/多目标、护盾、治疗、控制等尚未计入**；成长模板“尚未与图鉴完全统一”。建议仅作为“作者经验/试验推算”层级引用，不作为官方数值写入规则正文。
- 效果牌来源口径复核：`effects.json` 中 83 张来源为“商店购买、效果锦囊、拍卖等渠道”，**18 张为“仅在第三轮拍卖出现，无法从商店购买”**（`auctionRound=3`，对应第 12 回合拍卖）；效果牌能量费用（`shopCost`/`cost`）官方与 wiki 均未公开，维持“未知”。

## 六、未知项状态复核（本轮后）

仍维持“未知、禁止补空”的条目（官方与 wiki 均未给出精确值）：

- 每回合能量定额与能量上限、商店刷新单价/上限、锁店、商店栏位数、手牌上限；
- 1 级起始人口（已确认 3/5 级各 +1、6 级不再 +1，但起始值未公开）；
- 棋手升级货币口径（官方“能量” vs wiki“经验”两套并存，未裁决）；
- 拍卖最高出价与分红公式、效果牌完整费用表、觉醒精确条件（张数/合成次数/等级）；
- 效果牌商店 / 拍卖拍品 / 天赋候选的具体权重（wiki 已明示“待补资料”，权威侧同样缺失）；
- 准备阶段倒计时秒数、战斗是否可跳过。

已知事实（本轮再次确认，供自动化直接使用）：

- 拍卖回合 4 / 8 / 12，拍卖结束 +3 经验（不与同回合战斗 +1 叠加）；
- 棋手升级经验 7 / 13 / 17 / 23 / 27（1→4 累计 37，1→5 累计 60）；
- 上阵人数 3 级、5 级各 +1；基础装备投放 1 / 4 / 8 / 12 / 16 回合；
- 累计 3 次合成 → 1 张效果锦囊；天赋升级 3 选 1 免费、铜/银/金三阶、白银段位每局可刷 1 次；
- 商店费用层概率表（见 `mechanics.json` `hero-shop-odds`）、公共牌库 14/11/9/7/6。

## 七、本轮改动清单

- `json/image_index.json`：去重 24 条重复条目，重算 `count / download_ok / download_fail / url_only`，索引与磁盘一致。
- 新增 `scripts/fetch_remaining_images.py`：可断点续跑的剩余图片下载工具。
- 新增 `markdown/07-continuation.md`：本续查记录。
- 未改动 `rules.json` / `mechanics.json` / `lineups.json` / 各 csv（复核后内容无变化）。
