# 系统架构

> 最后更新：2026-05-16

## 架构决策

**采用方案**：Agent 编排 + 轻量后端，GitHub Pages + Railway 部署
**理由**：
- AI 是核心价值，系统围绕 Agent 编排构建，其他模块均为 Agent 的 Tool
- MVP 全部模块均会变化，每个外部 API 封装为独立 Tool
- 不想管服务器 + 中国可访问 → GitHub Pages + Railway
- v2 新增：用户系统（PostgreSQL）、AI 聊天（WebSocket）、购物车/订单

**评估**
| 维度 | 评级 | 说明 |
|------|------|------|
| 耦合度 | 极低 | 每个 Tool 独立封装 |
| 复杂度 | 低-中 | 远低于微服务 |
| 成本 | 低 | GitHub Pages 免费 + Railway 按用量 + PostgreSQL |

---

## 技术栈

| 层 | 方案 | 说明 |
|----|------|------|
| 前端托管 | GitHub Pages | 静态，国内基本可访问，免费 |
| 后端部署 | Railway | 无备案，GitHub 直连，按用量计费 |
| Agent 基座 LLM | Kimi API (Moonshot AI) | 国内稳定，支持 Function Calling |
| Agent 编排 | LangGraph (Python) | 有状态 DAG 编排 |
| 内容聚合 | 知乎直答 + 知乎搜索 + 全网搜索 API | 旅行攻略、景点信息 |
| 天气 | 和风天气 API | 国内可访问 |
| 地图 | Leaflet.js + 高德地图底图 | 国内稳定 |
| 购买链接 | MVP 静态映射 | 账号申请期间不阻塞 |
| 缓存 | Railway 内置 Redis | 缓存知乎 API 响应 |

---

## 系统模块

Touring Advisor
├── frontend/
│   ├── index.html                  # Vue 3 入口
│   ├── public/config.js            # 运行时配置（API Key，不提交 Git）
│   ├── src/
│   │   ├── main.ts                 # Vue 3 入口
│   │   ├── App.vue                 # 单页主布局
│   │   ├── components/
│   │   │   ├── MapArea.vue         # 顶部地图
│   │   │   ├── ChatSection.vue     # AI 聊天输入框 + 面板
│   │   │   ├── TourSection.vue     # 路线推荐区
│   │   │   ├── ShoppingSection.vue # 伴手礼购物区
│   │   │   ├── AuthOverlay.vue     # 登录遮罩
│   │   │   ├── UserDrawer.vue      # 个人中心抽屉
│   │   │   └── BottomSheet.vue     # 通用底部面板
│   │   └── stores/
│   │       ├── auth.ts
│   │       ├── cart.ts
│   │       └── chat.ts
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── package.json
└── backend/
    ├── api/
    │   ├── main.py                 # FastAPI 入口 + 路由挂载
    │   ├── deps.py                 # JWT 依赖注入
    │   ├── auth.py                 # 认证 API
    │   ├── tour.py                 # 路线 API
    │   ├── product.py              # 商品 API
    │   ├── order.py                # 购物车 + 订单 API
    │   └── chat.py                 # WebSocket 聊天
    ├── agent/
    │   ├── planner.py              # LangGraph Agent
    │   └── tools/
    │       ├── zhihu_answer.py
    │       ├── zhihu_search.py
    │       ├── global_search.py
    │       ├── weather.py
    │       ├── gear.py
    │       ├── commerce.py
    │       ├── map_poi.py
    │       ├── taobao_search.py
    │       ├── update_itinerary.py  # v2 新增
    │       └── update_cart.py       # v2 新增
    ├── db/
    │   ├── session.py              # 异步引擎连接
    │   └── models/
    │       ├── user.py
    │       ├── tour.py
    │       ├── cart.py
    │       └── order.py
    ├── alembic/                    # 数据库迁移
    ├── alembic.ini
    ├── utils/coord.py
    ├── requirements.txt
    └── railway.toml

---

## 知乎 API 说明

| API | Base URL | 鉴权方式 | 用途 |
|-----|----------|---------|------|
| 知乎开放平台 | developer.zhihu.com | Bearer Token + X-Request-Timestamp | 内容搜索、直答 |
| 知乎社区 API | openapi.zhihu.com | HMAC-SHA256 | 圈子内容 |

> 知乎直答 API 不是可自定义的基座模型，系统使用 Kimi 作为基座 LLM。

> 坐标系：高德地图使用 GCJ-02，GPS/WGS-84 坐标需用 coordtransform 库转换。

限流：知乎开放平台全局 10 QPS，需做 Redis 缓存。

---

## 组件关系图



---

## 数据流图



---

## 关键接口

| 接口 | 说明 |
|------|------|
| POST /api/plan | 接收行程文本，SSE 流式返回推荐结果 |
| GET /api/poi | 查询高德 POI，返回 GCJ-02 坐标 |
| GET /health | Railway 健康检查 |
| POST /api/auth/send-code | 发送验证码 |
| POST /api/auth/login | 验证码登录/注册 |
| GET /api/auth/user/profile | 用户信息 |
| GET /api/tours | 路线列表 |
| GET /api/tours/{id} | 路线详情 |
| GET /api/products | 商品搜索 |
| POST /api/products/ai-recommend | AI 选品推荐 |
| GET /api/cart | 购物车列表 |
| POST /api/cart | 添加购物车 |
| DELETE /api/cart/{id} | 删除购物车项 |
| POST /api/orders/quick | 一键下单 |
| GET /api/orders | 订单列表 |
| GET /api/orders/{id} | 订单详情 |
| WS /ws/chat | AI 聊天 WebSocket |

---

## 部署架构

| 层 | 方案 | 说明 |
|----|------|------|
| 前端 | GitHub Pages | 静态托管，国内可访问 |
| 后端 API | Railway | GitHub 直连，按用量计费 |
| 缓存 | Railway Redis | 项目内网 |
| LLM | Kimi API | 国内直连 |
| 知乎 API | developer.zhihu.com | Bearer Token，10 QPS |
| 天气 API | 和风天气 | 国内可访问 |
| 地图 | 高德地图 JS API + POI API | 国内稳定 |
