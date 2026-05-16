# 术语表

> 统一项目内的术语定义。
> 最后更新：2026-05-17

## 术语列表

| 术语 | 全称 / 英文 | 定义 | 首次出现 |
|------|------------|------|----------|
| Planner | Agent Planner | 系统主 Agent，使用 Kimi LLM | architecture.md |
| Tool | Agent Tool | 封装单一外部 API 的可调用函数 | architecture.md |
| 知乎直答 | Zhihu Answer API | 知乎内容聚合 API，非基座模型 | decisions.md |
| POI | Point of Interest | 地图上的兴趣点 | architecture.md |
| GCJ-02 | 火星坐标系 | 高德地图坐标系，需与 WGS-84 互转 | architecture.md |
| SSE | Server-Sent Events | 服务端向客户端推送流式数据 | architecture.md |
| LangGraph | LangGraph | 有状态 Agent 编排框架 | decisions.md |
| Kimi | Kimi API | Moonshot AI 的 LLM API | decisions.md |
| Railway | Railway | PaaS 部署平台 | decisions.md |
| 淘宝联盟 | Taobao Affiliate | 电商推广平台 | decisions.md |
| coordtransform | coordtransform | Python 坐标转换库 | architecture.md |
| WebSocket | WebSocket | 全双工通信协议，用于 AI 聊天 | design.md |
| JWT | JSON Web Token | 无状态用户认证 Token | design.md |
| Bottom Sheet | Bottom Sheet | 移动端底部弹出面板 UI 模式 | design.md |
| PWA | Progressive Web App | 可离线、可安装的 Web 应用 | design.md |
| 消息发送框 | Chat Input Bar | 主页上的 AI 聊天输入组件（ChatSection.vue 中的 assistant-card 区域） | ChatSection.vue |
| 行程对话窗口 | Itinerary Chat Window | 点击发送后弹出的底部面板，显示 AI 对话消息（ChatSection.vue 中的 BottomSheet） | ChatSection.vue |
| 行程规划会话 | Tour Planning Session | 一次完整的行程规划对话，由 UUID 标识，保存在 /session/ 目录 | dev_main.py |
| 装备推荐 | Gear Recommendation | 根据天气（温度、紫外线、降雨）和地形（山/水/森林）自动推荐装备 | dev_main.py |
| 多轮对话引导 | Multi-turn Guided Conversation | 分步骤收集目的地、日期、居住地、行程时长的对话流程 | dev_main.py |
| 主面板 | Main Panel | `App.vue`，组合 MapArea、ChatSection、TourSection、ShoppingSection 的根布局组件 | App.vue |
| 甄选路线 | Tour Section | `TourSection.vue`，展示路线标签页（半日精选/一日漫游/三日深度）及路线卡片 | TourSection.vue |
| 路线关键地点 | Route Highlights | `ShoppingSection.vue`，展示路线上关键地点的卡片列表 | ShoppingSection.vue |
| DeepSeek | DeepSeek AI | 替代 Kimi 的 LLM API，用于生成旅行推荐 | dev_main.py |
| Open-Meteo | Open-Meteo API | 免费天气数据源，替代 QWeather | dev_main.py |
| Dialog | Dialog Directory | 存储 AI 对话 prompt 和生成结果 | dialog/ |
| GCJ-02 | 火星坐标系 | 高德地图坐标系，需与 WGS-84 互转 | architecture.md |
