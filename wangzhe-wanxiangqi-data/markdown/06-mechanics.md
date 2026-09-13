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
