# 任务 Backlog

> 状态：`[ ]` 待做 · `[x]` 完成 · `[~]` 进行中 · `[!]` 阻塞

## 本周目标
完成 AI 旅伴助手 v2 后端骨架 + 前端 MVP 页面

## Backlog

### v2: AI 旅伴助手 — 后端
- [x] PostgreSQL + SQLAlchemy 数据模型
- [x] Alembic 迁移配置
- [x] JWT 用户认证系统（register/login/profile）
- [x] 路线推荐 API（list/detail/favorite）
- [x] 商品搜索 + AI 选品推荐 API
- [x] 购物车 CRUD + 一键下单 + 订单管理
- [x] WebSocket AI 聊天端点
- [x] Agent tools: update_itinerary, update_cart
- [~] 对接真实短信服务商（当前 MVP 模拟验证码）
- [x] 对接 DeepSeek LLM 真实 AI 回复（已替换 Kimi）

### v2: AI 旅伴助手 — 前端
- [x] Vue 3 + Vite 项目初始化
- [x] 单页布局（地图 → 聊天 → 路线推荐 → 购物）
- [x] Leaflet + 高德地图组件
- [x] AI 聊天输入框 + Bottom Sheet 面板
- [x] 路线推荐 Tab + 横向滚动卡片
- [x] 伴手礼商品卡片 + 一键下单 + 购物车
- [x] 登录遮罩层
- [x] 个人中心抽屉
- [x] 流式消息打字机效果
- [x] 聊天操作反馈（行程/购物车更新提示）
- [x] 订单提交表单
- [x] 个人中心子视图（历史/订单/收藏）
- [x] 历史记录下拉框 + 删除/清空功能
- [x] 日期选择器（根据对话步骤自动切换）
- [x] 加载中动画（脉冲提示）

### 环境准备
- [x] 配置知乎开放平台 Access Secret
- [x] 配置 Kimi API Key
- [x] 配置高德地图 Web 服务 Key
- [x] 配置高德地图 Web JS Key
- [~] 申请和风天气 API Key（Open-Meteo 已临时替代）
- [ ] 注册 Railway 账号，创建项目
- [ ] 申请淘宝联盟开发者账号

### 部署
- [x] 创建 GitHub Actions 构建工作流 (Vite build → GitHub Pages)
- [x] 更新 railway.toml（启动命令、环境变量）
- [x] 配置 GitHub Pages 目录为 /frontend/dist
- [ ] Railway 附加 PostgreSQL（需在 Dashboard 手动操作）
- [ ] 填写 Railway 环境变量（需在 Dashboard 手动操作）
- [ ] 更新 frontend/public/config.js 的 API_BASE_URL
