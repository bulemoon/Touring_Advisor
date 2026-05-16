# AGENTS.md — Touring Advisor

> 本文件定义 AI Agent 在此项目中可执行的指令。
> 放置于项目根目录，Claude Code 等工具启动时自动读取。

---

## 指令：/sync-docs

**用途**：根据 instruction.md 的规则，对项目所有文档执行完整审查与同步。

### Step 0 — 探测文档位置
检查文档实际存放位置（本项目文档在根目录，非 docs/ 子目录）。

### Step 1a — 检查文件是否存在
检查以下文件，缺失则基于已有文档推断内容自动创建：
- instruction.md · background.md · architecture.md · rule.md
- deploy.md · log.md · todo.md · decisions.md · terms.md

### Step 1b — 检查内容质量
- 是否有 [待补充] 占位符未填写
- 是否有空白章节
- 是否超过 14 天未更新

### Step 2 — 更新 log.md
读取 git log 或文件变更，生成今日条目。无法推断时提示用户描述今日工作。

### Step 3 — 同步 todo.md
将发现的问题追加到 todo.md（去重），检查进行中任务是否已完成。

### Step 4 — 补全建议
针对空白/占位内容逐一给出建议，确认后写入。

### Step 5 — 输出报告

---

## 其他约定
- 遵守 rule.md 中的所有开发规范
- 不确定需求时停下来提问，不假设
- 修改任何文件前先展示变更内容，等待确认
