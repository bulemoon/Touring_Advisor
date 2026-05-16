# 部署手册

> 最后更新：2026-05-16

---

## 一、外部服务账号与 Key 清单

所有 Key 存放在 .env（不提交 Git），同步维护在 Notion Subscriptions Vault。

| 服务 | 用途 | 申请地址 | 环境变量名 | 状态 |
|------|------|---------|-----------|------|
| 知乎开放平台 | 内容搜索、直答 | developer.zhihu.com | ZHIHU_ACCESS_SECRET | ✅ 已配置 |
| 和风天气 | 天气查询 | dev.qweather.com | QWEATHER_API_KEY | ⏳ 待申请 |
| Kimi (Moonshot AI) | Agent 基座 LLM | platform.moonshot.cn | KIMI_API_KEY | ✅ 已配置 |
| 高德地图 Web 服务 | 后端 POI 搜索 | lbs.amap.com | AMAP_SERVER_KEY | ✅ 已配置 |
| 高德地图 Web JS | 前端底图加载 | lbs.amap.com | 写入 frontend/config.js | ✅ 已配置 |
| Railway | 后端 + Redis | railway.com | OAuth 登录 | — |
| GitHub | 前端静态托管 | github.com | 仓库 Settings 开启 Pages | — |

### Key 申请步骤

**知乎开放平台**
1. 登录 developer.zhihu.com → 《个人中心》→ 复制 Access Secret
2. 需开通《知乎搜索 API》和《直答 API》权限

**和风天气**
1. 登录 dev.qweather.com → 【控制台】→ 【项目管理】→ 创建项目 → 添加 Key → 选 Web API

**Kimi**
1. 登录 platform.moonshot.cn → 【API Keys】→ 创建 Key

**高德地图（已有两个 Key，无需再申请）**
- Web 服务 Key → AMAP_SERVER_KEY
- Web JS Key → frontend/config.js

---

## 二、本地开发环境



本地 Redis：

---

## 三、Railway 后端部署

1. 登录 railway.com（GitHub OAuth）
2. New Project → Deploy from GitHub repo → 选 Touring_Advisor
3. Root Directory 设为 backend
4. 添加 Redis：+ New → Database → Add Redis（自动注入 REDIS_URL）
5. Variables 标签填入环境变量：



**常用命令**



---

## 四、GitHub Pages 前端部署

1. 仓库 → Settings → Pages
2. Branch: main，目录: /frontend
3. 访问 

**frontend/config.js**（不提交 Git）


---

## 五、故障排查

| 现象 | 排查步骤 |
|------|---------|
| ModuleNotFoundError | 重新 pip install |
| Railway 部署失败 | railway logs 查看构建日志 |
| 知乎 20001 | 检查 ZHIHU_ACCESS_SECRET 和 X-Request-Timestamp |
| 知乎 30001 | 超频（10 QPS），检查 Redis 缓存 |
| 高德 INVALID_USER_KEY | 检查 Key 类型（后端用 Web 服务 Key） |
| Kimi 401 | 检查 KIMI_API_KEY 和 base_url |
| 地图不显示 | 检查 config.js 的 AMAP_JS_KEY |

---

## 六、部署检查清单

- [ ] 后端 /health 接口返回 200
- [ ] Redis 连接正常
- [ ] 知乎搜索 API 调用成功
- [ ] 高德 POI API 调用成功
- [ ] Kimi Function Calling 调用成功
- [ ] 前端页面正常加载
- [ ] 高德底图正常显示
- [ ] 前端能正常调用后端 API
