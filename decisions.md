# 技术决策记录（ADR）

---

## ADR-010 — 新增：用户认证系统

**日期**：2026-05-16  **状态**：已采纳

### 决策
引入用户系统（JWT + 手机号验证码），突破原 MVP "匿名无状态"约束。用户数据存储于 PostgreSQL。

---

## ADR-009 — 前端框架：Vue 3 + Vite

**日期**：2026-05-16  **状态**：已采纳

### 决策
从 vanilla HTML/JS 迁移至 Vue 3 + Vite，支持 PWA、状态管理（Pinia）、组件化开发。构建产物输出至 `frontend/dist/`，GitHub Pages 目录调整为 `/frontend/dist`。

---

## ADR-008 — 数据库：PostgreSQL

**日期**：2026-05-16  **状态**：已采纳

### 决策
从无状态升级为持久化，选用 PostgreSQL（SQLAlchemy async + asyncpg），通过 Railway 托管。

## ADR-007 — 后端部署：Railway（Hackathon 阶段）

**日期**：2026-05-16  **状态**：已采纳

### 决策
后端和 Redis 均部署在 Railway，GitHub 直连自动部署。Hackathon 结束后如需正式上线，再迁移至 Zeabur 或阿里云。

---

## ADR-006 — 地图方案：Leaflet.js + 高德地图

**日期**：2026-05-16  **状态**：已采纳

### 决策
Leaflet.js + 高德地图底图 + 高德 POI 搜索 API。高德使用 GCJ-02，需用 coordtransform 库转换坐标。

---

## ADR-005 — Agent 编排框架：LangGraph

**日期**：2026-05-16  **状态**：已采纳

### 决策
LangGraph（Python），支持有状态 DAG 编排，与 Kimi Function Calling 兼容。

---

## ADR-004 — 电商购买链接：MVP 静态映射，二期接淘宝联盟

**日期**：2026-05-16  **状态**：已采纳

### 决策
commerce.py 一期用静态字典映射，账号到位后替换为淘宝联盟 API。

---

## ADR-003 — 知乎直答 API 定位：内容聚合 Tool

**日期**：2026-05-16  **状态**：已采纳

### 决策
知乎直答 API 不支持自定义 System Prompt，不能作为基座 LLM。作为 Tool 提供旅行内容聚合。

---

## ADR-002 — Agent 基座 LLM：Kimi API

**日期**：2026-05-16  **状态**：已采纳（替换原 DeepSeek 方案）

### 候选方案
| 方案 | 国内访问 | Function Calling | 成本 |
|------|---------|-----------------|------|
| Kimi API | 稳定 | 支持 | 低 |
| DeepSeek API | 稳定 | 支持 | 极低 |

### 决策
Kimi API（platform.moonshot.cn），国内稳定，支持 Function Calling，兼容 OpenAI SDK。

---

## ADR-001 — 部署方案：GitHub Pages + Railway

**日期**：2026-05-16  **状态**：已采纳（Hackathon 阶段）

### 决策
GitHub Pages（前端）+ Railway（后端 + Redis）。push 即部署，适合快速迭代。
