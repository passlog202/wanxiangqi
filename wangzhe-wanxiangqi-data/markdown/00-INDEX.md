# 王者万象棋资料包

目标游戏：王者万象棋。未用王者模拟战或其他自走棋规则补空。

- 适用版本：1.1.1（2026-09-09）；全平台 2026-09-10 07:00
- 卡图：官方 2026-08-28
- 模式：万象大赛
- 采集：2026-09-12 至 2026-09-13
- 主来源：https://wanxiangqiwiki.com/explore/hero-sulie ；https://wxq.qq.com/cp/a202609xszy/index.html

优先完成顺序：基础规则 → 3 套阵容与决策 → 相关卡牌 → 操作截图 → 其余目录。

## 文件

| 路径 | 内容 |
|---|---|
| `/wangzhe-wanxiangqi-data/json/rules.json` | 规则结构化 |
| `/wangzhe-wanxiangqi-data/markdown/01-rules.md` | 规则说明 |
| `/wangzhe-wanxiangqi-data/json/lineups.json` | 3 套阵容 |
| `/wangzhe-wanxiangqi-data/markdown/02-lineups.md` | 阵容说明 |
| `/wangzhe-wanxiangqi-data/json/decisions.json` + csv | 条件→动作表（20 条） |
| `/wangzhe-wanxiangqi-data/json/lineups.csv` | 3 套阵容摘要 |
| `/wangzhe-wanxiangqi-data/markdown/04-decisions.md` | 决策说明 |
| `/wangzhe-wanxiangqi-data/json/mechanics.json` + csv | wiki 机制词典 26 条（已修编码） |
| `/wangzhe-wanxiangqi-data/json/unknowns_conflicts.json` | 未知与冲突汇总 |
| `/wangzhe-wanxiangqi-data/json/heroes.json` + csv | 英雄 86 |
| `/wangzhe-wanxiangqi-data/json/effects.json` + csv | 效果牌 101（官方 currentCount 98） |
| `/wangzhe-wanxiangqi-data/json/equipment.json` + csv | 装备 95（官方 currentCount 73） |
| `/wangzhe-wanxiangqi-data/json/talents.json` + csv | 天赋 269（官方 currentCount 255） |
| `/wangzhe-wanxiangqi-data/json/chessplayers.json` + csv | 棋手 21 |
| `/wangzhe-wanxiangqi-data/markdown/03-cards.md` | 卡牌摘录 |
| `/wangzhe-wanxiangqi-data/json/image_index.json` | URL/文件名对应表（1328 条目，144 已下 / 1184 待下） |
| `/wangzhe-wanxiangqi-data/scripts/fetch_remaining_images.py` | 剩余图片断点续跑下载工具 |
| `/wangzhe-wanxiangqi-data/markdown/07-continuation.md` | 2026-09-13 续查记录 |
| `/wangzhe-wanxiangqi-data/json/ui_operations.json` | 操作 |
| `/wangzhe-wanxiangqi-data/json/screenshot_index.json` | 截图对应表（57/57 与磁盘一致） |
| `/wangzhe-wanxiangqi-data/markdown/05-operations.md` | 界面证据 |
| `/wangzhe-wanxiangqi-data/images/` | 英雄/棋手头像原图 |
| `/wangzhe-wanxiangqi-data/screenshots/` | 官方教学截图 57 张 |
| `/wangzhe-wanxiangqi-data/raw/` | wiki 原始 JSON |
| `/wangzhe-wanxiangqi-data/AGENT_BRIEFING.md` | 采集简报 |

## 自动化 3 套

1. 日落海整备流（闹闹）
2. 嫦娥四人队 / 马瑶经典（常小娥：苏烈、瑶、马超、海月）
3. 大河图腾流（瑶妹：鬼谷子、少司缘、大司命、虞姬、张良、敖隐、东皇太一）

未选：白歌三分倒转、玉环日落海倒转、香香低阶开团射。

## 证据层级

官方规则、wiki 机制词典、作者经验、推测分开标注。冲突与未知写在各文件末尾。

## 冲突（采用）

| 主题 | 采用 |
|---|---|
| 常小娥秘技门槛 | 官网 50/150/375（弃用 chessplayerFacts 50/175/400） |
| wiki 25 套 mid/late | 污染，只用 early / 标题 / 官方图文 |
| 日落海海诺站位 | 官方前排左 |
| 雅典娜装备 | 官方三件：霸者重铠 / 近卫荣耀 / 不死鸟之眼 |
| 棋手升级 | 操作花能量点按钮；节奏按官方回合升 2/3/5/6；wiki 经验表 7/13/17/23/27 并存 |
| 拍卖回合 | wiki 校准 4/8/12 |

## 未知（禁止用其他自走棋补）

每回合能量定额与上限；刷新单价与上限；锁店；手牌上限；1 级起始人口；升级能量表；拍卖最高出价与分红公式；效果牌完整费用；觉醒张数条件；准备倒计时；战斗/淘汰页实机截图。

## 核对

- 2026-09-13 续查：`git pull` 已最新；线上 wiki 各机制页与 `mechanics.json` 逐项一致；`image_index.json` 已去重 24 条重复条目（`items` 1328 = `count`，ok 144 / url_only 1184），并新增剩余图片下载工具 `scripts/fetch_remaining_images.py`；详见 `markdown/07-continuation.md`。沙箱无法直连 `assets.wanxiangqiwiki.com`，剩余原图需在可访问该 CDN 的环境用该脚本补下。
- `screenshot_index.json` 57 条与 `screenshots/` 57 文件一一对应。
- `ui_operations.json` 完整落盘（大厅到开战、买/上/合成/升级/出售/拍卖/天赋）。
- 2026-09-13 补下大河核心卡图：大司命、敖隐、东皇太一、干将莫邪。
- `raw/wiki-knowledge-payload-0.json` 已从 latin-1 误读还原为 UTF-8（26 条，如「整备」「开团」）。
- `heroes.csv` 已同步 `lineups` 自动化标签。
