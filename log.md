# 变更日志

## 2026-05-16 — 项目初始化 + 架构确定

### 完成
- 初始化项目文档结构（instruction / background / architecture / rule / log / todo / decisions / terms / deploy / AGENTS.md）
- 完成架构讨论：Agent 编排 + LangGraph + Kimi + 知乎 API + GitHub Pages + Railway
- 确认知乎直答 API 为内容聚合来源，非基座模型
- 确认地图方案：Leaflet.js + 高德地图
- 确认后端部署：Railway（Hackathon 阶段）
- 配置 .env、frontend/config.js、backend/requirements.txt、railway.toml
- 从 Notion Vault 写入已有 API Key（知乎、Kimi、高德 Web 服务、高德 JS Web）
- 修复所有 md 文件编码问题（Mac Roman → UTF-8）

### 待跟进
- 申请和风天气 API Key（QWEATHER_API_KEY 当前为空）
- Railway 后端首次部署
- 开始实现 backend/api/main.py 骨架

---

<!-- 新日志在上方添加 -->
