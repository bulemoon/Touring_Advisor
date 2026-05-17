# Plan — 攻略路线地图联动

> 状态：Done
> 日期：2026-05-17

## 阶段 1：整理当前链路

### 目标

确认现有地图、聊天、路线规划模块的职责边界。

### 检查点

- `frontend/src/components/MapArea.vue`
- `frontend/src/components/ChatSection.vue`
- `frontend/src/stores/chat.ts`
- `frontend/src/App.vue`
- `backend/dev_main.py`
- `backend/services/route_planner.py`

### 输出

形成最小改动方案，不改变数据库结构，不替换地图方案。

## 阶段 2：后端聊天接口返回路线

### 文件

- `backend/dev_main.py`

### 任务

- 增加攻略意图识别。
- 从用户输入中提取：
  - 城市/区域 hint
  - 天数
  - 出行模式
- 调用高德周边 POI。
- 让 Kimi 从候选 POI 中选择路线点。
- 将 Kimi 返回地点映射回 POI 坐标。
- 调用 `build_route_plan` 生成优化路线。
- 在 `/api/chat` 响应中返回 `route_plan`。

### 验收

- 普通聊天仍返回文本。
- 攻略类聊天尽可能返回 `route_plan`。
- 无法生成路线时返回 `route_plan: null`，不影响聊天。

## 阶段 3：前端聊天状态接入路线

### 文件

- `frontend/src/stores/chat.ts`

### 任务

- 增加 `RouteStop` 类型。
- 增加 `RoutePlan` 类型。
- 增加 `currentRoutePlan`。
- 在 `send()` 中读取接口返回的 `route_plan`。

### 验收

- 聊天请求成功后，store 能保存路线。
- 没有路线时状态为 `null`。

## 阶段 4：聊天组件向上同步路线

### 文件

- `frontend/src/components/ChatSection.vue`

### 任务

- 增加 `route-plan` emit。
- watch `chat.currentRoutePlan`。
- 当路线更新时通知父组件。

### 验收

- 聊天生成路线后，父组件能收到新路线。

## 阶段 5：App 统一管理地图路线

### 文件

- `frontend/src/App.vue`

### 任务

- 增加 `routePlan` 状态。
- 将 `routePlan` 传入 `MapArea`。
- 接收：
  - `ChatSection` 的 `route-plan`
  - `TourSection` 的 `route-plan`

### 验收

- 路线卡片和聊天都能驱动地图。
- 后触发的路线覆盖当前地图路线。

## 阶段 6：地图展示增强

### 文件

- `frontend/src/components/MapArea.vue`

### 任务

- 支持 `routePlan` prop。
- 绘制编号 marker。
- 绘制 polyline。
- popup 展示地址、停留时间、推荐理由。
- 路线更新时自动 fitBounds。

### 验收

- 地图能显示路线点。
- 地图能显示路径线。
- marker 弹窗信息完整。
- 空路线不会报错。

## 阶段 7：验证

### 命令

```bash
.venv\Scripts\python.exe -m compileall backend
```

```bash
cd frontend
npm run build
```

### 验收

- 后端编译通过。
- 前端构建通过。
- 无 TypeScript 类型错误。

## 阶段 8：记录和后续任务

### 建议更新

- `log.md`
- `todo.md`
- 必要时更新 `architecture.md`

### 后续任务

- 支持指定城市 POI 检索。
- 增加路线来源切换。
- 支持多日路线分日展示。
- 支持保存 AI 生成路线。

## 执行结果

### 已完成

- 后端聊天接口可在攻略类请求中返回 `route_plan`。
- 前端聊天 store 已保存 `currentRoutePlan`。
- `ChatSection` 已向父组件同步聊天生成路线。
- `App.vue` 已统一向地图传递当前路线。
- `MapArea` 已支持编号 marker、polyline、popup 和自动视野缩放。
- 已保留现有路线卡片驱动地图的能力。

### 验证

- 后端 Python 编译通过。
- 前端生产构建通过。
