# 王者万象棋 · 机制词典

来源：https://wanxiangqiwiki.com/mechanics  
落地：当前工作区 `/wangzhe-wanxiangqi-data/raw/wiki-knowledge-payload-0.json`（2026-09-13 从 latin-1 误读还原）  
结构化：`/wangzhe-wanxiangqi-data/json/mechanics.json` + `mechanics.csv`  
证据层级：wiki 机制词典。未改写为其他自走棋规则。

| id | 名称 | 类别 |
|---|---|---|
| prepare | 整备 | 触发时点 |
| combat-start | 开团（别名：交锋） | 触发时点 |
| entry | 登场 | 触发时点 |
| sacrifice | 牺牲 | 战斗与计算 |
| triumph | 凯旋 | 触发时点 |
| exit | 退场 | 触发时点 |
| temporary-level | 临时等级 | 成长与等级 |
| co-battle | 共战 | 战斗与计算 |
| hero-shop-odds | 英雄商店概率 | 概率与随机 |
| population | 上阵人数 | 结算与上限 |
| auction | 拍卖 | 经济与牌库 |
| player-experience | 棋手经验 | 成长与等级 |
| synthesis | 合成进度 | 成长与等级 |
| talent-selection | 天赋选择 | 经济与牌库 |
| equipment-acquisition | 装备获取 | 经济与牌库 |
| player-loss-cap | 战败伤害上限 | 结算与上限 |

完整 26 条定义、证据引用与边界见 JSON。商店概率、人口、拍卖回合、经验表、战败伤害已写入 `01-rules.md` / `rules.json`。

---

## 官方关键词词典（13 条）

来源：官方新手指引《万象启航》关键词词典，https://wxq.qq.com/cp/a202609xszy/index.html（官方规则，2026-09-13 采集）。
结构化：`/wangzhe-wanxiangqi-data/json/keywords.json` + `keywords.csv`。

| 词 | 定义 | wiki 对照 |
|---|---|---|
| 登场 | 使用此卡牌后，触发效果。 | entry |
| 开团 | 战斗开始时，触发效果。 | combat-start |
| 整备 | 回合开始时，触发效果。 | prepare |
| 牺牲 | 英雄阵亡时，触发效果。 | sacrifice |
| 合成 | 使用场上已存在的英雄牌，与场上英雄结合，使其强化。 | synthesis |
| 闪现 | 战斗开始时，英雄会跳跃至敌方战场的镜像位置。 | 未单列 |
| 夺取 | 使用此卡牌时，夺取周围1格随机1名己方英雄的等级（最多10级，不包含临时等级）。 | 未单列 |
| 临时等级 | 战斗结束时，临时等级将会被清除。 | temporary-level |
| 转瞬 | 回合结束时自动销毁，且出售不会获得能量。 | 未单列 |
| 复生 | 英雄在阵亡后会复活，并恢复50%生命值（每名英雄单回合最多复活10次）。 | 未单列 |
| 凯旋 | 英雄上阵期间若战斗胜利，触发效果。 | triumph |
| 败阵 | 英雄上阵期间若战斗失败，触发效果。 | 未单列 |
| 退场 | 场上的此英雄被出售时，触发效果。 | exit |

官方明确数值：复生单回合最多复活 10 次；夺取最多夺取 10 级、不含临时等级。wiki 机制词典未单列闪现 / 夺取 / 复生 / 败阵。
