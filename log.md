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

## 2026-05-17 — DeepSeek 替换 + 天气/知乎修复 + 输出格式重构

### 完成
- **LLM 切换**：Kimi (401 失效) → DeepSeek (`sk-c593f1f8db8945119acee62f5e0cdf30`)
- **天气 API**：QWeather (404/403) → Open-Meteo（免费，无需 key）
- **知乎 API**：修复端点 `openapi.zhihu.com/v3/search` → `developer.zhihu.com/api/v1/content/zhihu_search`
- **输出格式重构**：
  - 新增 `### 🌤️ 天气情况`（第1模块）
  - `推荐路线` → `推荐景点`
  - 新增 `### 🛍️ 周边购物推荐`（第5模块，含地址、坐标 GCJ-02、推荐商品）
  - 完整6模块：天气 → 概览 → 景点 → 装备 → 购物 → 小贴士
- **Prompt 模板化**：创建 `dialog/prompt.md`（完整 system + user + 输出格式模板）
- **Dialog 持久化**：每次生成保存 `dialog/{uuid}_prompt.md` + `dialog/{uuid}.md`
- **Session 结构重构**：
  - 文件夹格式：`session/{uuid}/meta.json + chat.json + attractions.json + shopping.json`
  - 兼容旧 `.json` 文件格式
  - 景点/购物分拆，含完整坐标（lat/lng + crs）
- **前端交互增强**：
  - 历史记录下拉框（每行右对齐删除按钮 ×）
  - 清空全部按钮（确认提示 + 反馈提示）
  - Inline 输入新建 session，BottomSheet 内续聊
  - 加载中动画（`正在查询...·` 脉冲提示）
- **日期选择器**：当前步骤为 `date` 时自动渲染 HTML5 date picker，避免日期格式错误
- **术语更新**：`terms.md` 新增 主面板、甄选路线、路线关键地点

### 待跟进
- 和风天气 QWEATHER key 仍未解决（Open-Meteo 已替代）
- 前端构建测试（npm run build）
- 部署 Railway / GitHub Pages

## 2026-05-17 — 清空历史记录修复 + 日期选择器

### 完成
- **清空历史记录修复**：`DELETE /api/session/all` 同时清空 session 和 dialog 目录
- **日期选择器**：前端根据 `current_step` 字段自动切换输入框为日期选择器，后端返回 `current_step` 标识当前收集步骤
- **删除确认**：删除单条和清空全部均增加 `confirm()` 确认框

### 待跟进
- 和风天气 QWEATHER key（Open-Meteo 已替代）
- 前端构建测试（npm run build）
- 部署 Railway / GitHub Pages

---

<!-- 新日志在上方添加 -->
