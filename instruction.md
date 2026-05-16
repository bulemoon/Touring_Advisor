# Touring Advisor — 文档导航

> 本文件是项目文档体系的入口，说明每个文档的用途和使用时机。

## 文档地图

| 文件 | 用途 | 更新频率 |
|------|------|----------|
| instruction.md | 文档体系说明（本文件） | 文档结构变更时 |
| background.md | 项目背景、目标、约束 | 项目定义变更时 |
| architecture.md | 系统架构与组件关系 | 架构调整时 |
| rule.md | 开发规范与 AI 协作规则 | 规范变更时 |
| deploy.md | 部署手册 | 部署配置变更时 |
| log.md | 每日变更记录 | 每次提交后 |
| todo.md | 当前任务 Backlog | 每次计划/完成任务时 |
| decisions.md | 技术决策记录（ADR） | 做出重要决策时 |
| terms.md | 项目术语表 | 引入新术语时 |

## 使用原则

- 开始新功能前：先看 todo.md 和 architecture.md
- 做技术选型时：先在 decisions.md 记录候选方案，决策后更新结论
- 每次开发结束：更新 log.md，同步 todo.md 状态
- 发现架构变化：立即更新 architecture.md
- 引入新术语：在 terms.md 补充定义
- 部署遇到问题：查 deploy.md

## 文档同步指令

| 指令 | 动作 |
|------|------|
| /sync-docs | 扫描健康度 → 更新 log.md → 同步 todo.md → 补全建议 → 输出报告 |

详细执行逻辑见 AGENTS.md。
