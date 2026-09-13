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

---

## 八、续查 II：官方新手指引补采（2026-09-13）

复核 `raw/official-guide-a202609xszy.html`（官方新手指引全量文本）后发现 4 处未结构化的官方内容，已全部补采落地：

### 8.1 官方关键词词典（13 条）→ `json/keywords.json` + `keywords.csv`

官方新手指引「关键词词典」共 13 条，含 4 条 wiki 机制词典未单列的官方词条与数值：

- **复生**：英雄阵亡后复活并恢复 50% 生命值，**每名英雄单回合最多复活 10 次**（官方明确数值）；
- **夺取**：夺取周围 1 格随机 1 名己方英雄等级，**最多 10 级、不含临时等级**；
- **闪现**：战斗开始时英雄跳跃至敌方战场镜像位置；
- **败阵**：上阵期间战斗失败触发。

其余 9 条（登场 / 开团 / 整备 / 牺牲 / 合成 / 临时等级 / 转瞬 / 凯旋 / 退场）与 `mechanics.json` 交叉对照（见 `keywords.json` 的 `mechanics_id`）。已写入 `markdown/06-mechanics.md`。

### 8.2 官方入门阵容（5 套）→ `json/official_newbie_lineups.json`

三分登场流（吕布）、日落海整备流（安琪拉）、大河图腾流（敖隐）、河洛古币流（百里玄策）、逐鹿战术牌流（蒙犽）。其中日落海整备流 = 自动化第 1、大河图腾流 = 自动化第 3；三分登场流 / 河洛古币流 / 逐鹿战术牌流未纳入自动化。已写入 `markdown/02-lineups.md`。

### 8.3 大神教学（12 篇）→ `json/pro_guides.json` + `pro_guides.csv`

官方页「大神教学」收录 12 篇标题（作者 / 标题 / 推荐棋手），证据层级标为**作者经验**（非官方规则）。其中白歌三分倒转、玉环日落海倒转、香香开团射与简报“未选”一致；与 wiki 25 套预设同名/近似的已标注 `related_wiki_preset`。页面仅提供阵容码复制与导入三步，未提供逐阵容码文本。已写入 `markdown/02-lineups.md`。

### 8.4 棋手推荐语（5 名）→ 写回 `chessplayers.json` / `chessplayers.csv`

官方「棋手推荐」5 名棋手的推荐语（香香 / 瑶妹 / 白歌 / 常小娥 / 闹闹）补入 `recommendation_tagline` 字段（其余棋手为空串）；csv 同步新增该列（保持原 BOM 与 `|` 连接的 lineups 格式）。

### 8.5 本轮改动清单（续）

- 新增 `json/keywords.json` + `json/keywords.csv`
- 新增 `json/official_newbie_lineups.json`
- 新增 `json/pro_guides.json` + `json/pro_guides.csv`
- 更新 `json/chessplayers.json`（+`recommendation_tagline`）、重写 `json/chessplayers.csv`（+新列）
- 更新 `markdown/02-lineups.md`、`markdown/06-mechanics.md`、`markdown/00-INDEX.md`

---

## 九、续查 III：官网首页补采 + 外部来源清单（2026-09-13）

### 9.1 官网首页「新人推荐」→ `json/official_recommended_lineups.json`

官网首页 https://wxq.qq.com/ （首发专题 a20260709sfzt）「新人推荐」给出 6 组「推荐棋手→推荐阵容」官方配对与阵容描述，比新手指引 5 套多出「嫦娥四人队」：

白歌→三分登场流、香香→日落海整备流、常小娥→嫦娥四人队、瑶妹→大河图腾流、庄小鱼→河洛古币流、小妲己→逐鹿战术牌流。每套均有「复制阵容码」按钮（码字符串在页面 JS 中，本轮未抓取）。已写入 `markdown/02-lineups.md`。

### 9.2 本轮勘界：还可获取的外部来源（按价值排序，未全部落地）

1. **版本更新公告（patch notes）**：TapTap 官方号 / 旅法师营地(iyingdi) 有 5 月 26 日「终测整备赛季」完整更新公告（含：初始阵容由局外随机改为局内拍卖、钻石系统、成长之路、合成工坊、段位继承、有分同享开放至王者 3000 分、翻牌上限 200 次等）。注意为上线前测试版公告，需与 1.1.1 正式版逐条核验后才能入规则正文。
2. **上线期新闻/公告**：news.qq.com 9 月 10 日公测文（全平台互通、85 位英雄——与 wiki 86 英雄口径不一致，待核）、新浪/中关村在线 9 月 9 日配置要求（安卓 1.88GB / iOS 3.18GB / 鸿蒙 3.67GB、PC 20GB SSD）。
3. **官网下载与社群**：PC/WeGame/macOS 安装包直链（1.1.1 exe）、B站/抖音/快手/微博/小红书/微信公众号/小程序/腾讯频道/王者营地官方账号。
4. **教学视频（9 条）**：官方新手指引 9 条腾讯视频（vid 已录在 `ui_operations.json`），可拼 v.qq.com 播放页/接口地址，用 yt-dlp/you-get 在沙箱外下载。
5. **社区攻略**：旅法师营地(iyingdi) 有逐阵容详细运营/站位/装备攻略（如常小娥刺客七三），证据层级=作者经验，且多为 2025-12/2026-01 测试版内容，需版本核验；部分站点（bufan/gamedog/ali213）的「最强阵容」含不知火舞、娜可露露、橘右京等非本游戏英雄，属错误资料，弃用。
6. **剩余 1184 张原图**：脚本已就绪（`scripts/fetch_remaining_images.py`），受沙箱出口限制，需可访问 `assets.wanxiangqiwiki.com` 的环境执行。

### 9.3 本轮改动清单（续）

- 新增 `json/official_recommended_lineups.json`（6 组推荐阵容）
- 更新 `markdown/02-lineups.md`（官网首页推荐阵容节）、`markdown/00-INDEX.md`

---

## 十、续查 IV：英雄详情（hero-sulie 同源数据）（2026-09-13）

任务：去 `https://wanxiangqiwiki.com/explore/hero-sulie` 继续获取英雄属性等资料。

要点：
- 该详情页为纯前端渲染（fetch_page 只回「正在载入英雄资料」），但页面数据源就是本地已存的 `raw/wanxiangqiwiki.com_explorer-catalogs_hero.json`（86 英雄全量，`currentCount=86` 与目录一致）。
- 该原始 JSON 里存在 `heroes.json` **未收录**的三块内容，本轮全部补采结构化：

### 10.1 成长模型（85/86）→ `json/hero_details.json` + `json/hero_growth.csv`

- 字段：`template`（成长模板）、`baseProperties`（基础属性 10 项）、`levelSnapshots`（1/10/40/100/150/200 六级快照）、`templateReference`（逐级成长公式 + 节点）、`skillBreakpoints`（10/40/100 技能节点）、`awakeningDesc`。
- 证据层级：wiki「官方卡牌资料 + 同源成长模型」（wiki 自标注，逐级公式为同源模型，档位快照非逐级）。
- 成长模板分布：法师 20 / 物理坦克 13 / 战士 11 / 辅助 10 / 法坦 8 / 刺客 8 / 416射手 6 / 普通射手 6 / 法战·法射·法刺 各 1。
- 唯一缺失：王维（`hero-1381`）无 growth。
- `hero_growth.csv`：85 行 ×（6 级 × 6 维生命/物攻/法攻/物防/法防/攻速）数值矩阵，供自动化直接读。

### 10.2 知识理解/实战关联（12/86）→ `hero_details.json` knowledge

wiki 作者理解（作者经验层级），每名含 formal/resource/trigger/receivers/failures/confidence/pending/related：苏烈、曜、孙膑、沈梦溪、盾山、虞姬、公孙离、云中君、张良、少司缘、李信、花木兰。自动化 3 套阵容涉及苏烈、虞姬、张良、少司缘 4 名。

### 10.3 关联卡牌（86/86）→ `hero_details.json` related_cards

觉醒卡面 85、来源天赋 42、效果预览 33、英雄预览 6、相关预览 2。

### 10.4 后续可补（同源目录里还有 formal 知识理解字段）

- 效果牌 6 / 装备 20 / 天赋 6 张卡也有 `formal`（知识理解）字段，本轮未展开，可后续补采成 `effect_details.json` / `equipment_details.json` / `talent_details.json`。

### 10.5 本轮改动清单（续）

- 新增 `json/hero_details.json`、`json/hero_growth.csv`
- 更新 `markdown/03-cards.md`（成长模型与知识理解节）、`markdown/00-INDEX.md`

---

## 十一、续查 V：效果牌 / 装备 / 天赋详情（2026-09-13）

补采 `raw/wanxiangqiwiki.com_explorer-catalogs_{effect,equipment,talent}.json` 中 `effects.json` / `equipment.json` / `talents.json` 未收录的 wiki 详情字段 → `json/card_details.json` + `json/equipment_combat.csv`。

### 11.1 知识理解 / 实战关联（wiki 作者理解，非官方规则）

- 效果牌 6/101：吸纳人才、研读会、援护战术、古币、演练战术、招兵买马（含 formal/resource/trigger）。
- 装备 20/95：含「当前资料未收录正式理解」占位条；实质理解有霸者重铠、护命灵珠、玄微之种、双剑·雄、贤者之书等。
- 天赋 6/269：一个响指、一分钱一分货、一身是胆（赵云专属）、三三得三、三分增援、三人游。

### 11.2 关联卡牌反向索引

- 效果牌 24/101 有 `relation=source`（这张卡由谁产出）；装备 55/95、天赋 91/269 有 `relation=preview` 关联预览。
- 例：古币 ← 李元芳、盾山、程咬金、狄仁杰、上官婉儿、李白、花木兰、武则天（英雄）+ 多彩古币、古币翻新、丝绸之路（天赋）。

### 11.3 装备战斗数值

- `combatCategory`：防御 8 / 攻击 14 / 功能 10（32 件）；另有 2 件仅 illustration/其他。
- 仅 2 件有 wiki 数值修正：霸者重铠（生命>70% 减伤 40%）、护命灵珠（有护盾增伤 25%）。
- `equipment_combat.csv` 34 行（id/名称/品阶/子类/装备类型/战斗分类/修正值/卡面）。

### 11.4 天赋衍生卡面（derivedCards）

101/269 天赋带衍生卡面（天赋「获得1张天赋牌XX」的 XX），含卡面图 URL。

### 11.5 冲突：天赋出现阶段 vs 拍卖回合（未裁决）

wiki 天赋目录 `talentStage` 分布含「第八轮拍卖 167 张」，与机制词典「拍卖 4/8/12 回合（3 次）」不一致。可能原因：按 8 次拍卖录入 / 含初始阵容拍卖 / 版本差异。已记入 `unknowns_conflicts.json` 的 `unknowns.talents` 与 `conflicts.talents`，规则正文维持 4/8/12。

### 11.6 本轮改动清单（续）

- 新增 `json/card_details.json`、`json/equipment_combat.csv`
- 更新 `json/unknowns_conflicts.json`（+unknowns.talents、+conflicts.talents）
- 更新 `markdown/03-cards.md`（效果/装备/天赋详情节）、`markdown/00-INDEX.md`
