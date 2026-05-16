# 任务 Backlog

> 状态：`[ ]` 待做 · `[x]` 完成 · `[~]` 进行中 · `[!]` 阻塞

## 本周目标
搭建后端骨架，跑通一次完整的行程输入 → Agent 调用 → 结果返回流程

## Backlog

### 环境准备
- [x] 配置知乎开放平台 Access Secret
- [x] 配置 Kimi API Key
- [x] 配置高德地图 Web 服务 Key
- [x] 配置高德地图 Web JS Key
- [ ] 申请和风天气 API Key
- [ ] 注册 Railway 账号，创建项目
- [ ] 申请淘宝联盟开发者账号

### 后端
- [ ] 初始化 Python 项目结构
- [ ] 实现 FastAPI 接口层
- [ ] 实现 Agent planner.py（LangGraph + Kimi）
- [ ] 实现 Tool: zhihu_search.py
- [ ] 实现 Tool: zhihu_answer.py
- [ ] 实现 Tool: weather.py
- [ ] 实现 Tool: gear.py
- [ ] 实现 Tool: commerce.py
- [ ] 实现 Tool: map_poi.py
- [ ] 实现 utils/coord.py
- [ ] 接入 Redis 缓存层

### 前端
- [ ] 实现行程输入页面
- [ ] 实现推荐结果展示页面
- [ ] 集成 Leaflet.js + 高德地图
- [ ] 对接后端 SSE 流式接口

### 部署
- [ ] 配置 GitHub Pages 自动部署
- [ ] 配置 Railway 部署
- [ ] 填写 Railway 环境变量
- [ ] Railway 部署后更新 frontend/config.js 的 API_BASE_URL

### 技术债
- [ ] commerce.py 替换为淘宝联盟 API
- [ ] Hackathon 后评估迁移后端至 Zeabur
