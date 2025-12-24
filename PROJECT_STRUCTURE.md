# 项目文件结构

本项目已生成以下文件结构：

## 核心文件

- `app.py` - Flask 主应用文件
- `config.py` - 配置文件（数据库、邮件等）
- `extensions.py` - Flask 扩展初始化
- `requirements.txt` - Python 依赖包列表
- `init_db.py` - 数据库初始化脚本
- `README.md` - 项目说明文档
- `.gitignore` - Git 忽略文件配置

## 数据模型 (models/)

- `models/__init__.py` - 模型模块初始化
- `models/user.py` - 用户模型（User）
- `models/venue.py` - 场馆模型（Venue）
- `models/reservation.py` - 预约模型（Reservation）
- `models/notification.py` - 通知模型（Notification）

## 路由 (routes/)

- `routes/__init__.py` - 路由模块初始化
- `routes/auth.py` - 用户认证路由（注册、登录、登出）
- `routes/venue.py` - 场馆路由（列表、详情）
- `routes/reservation.py` - 预约路由（创建、查看、取消）
- `routes/admin.py` - 管理员路由（场馆管理、预约管理、统计）
- `routes/user.py` - 用户路由（通知管理）

## 业务逻辑服务 (services/)

- `services/__init__.py` - 服务模块初始化
- `services/reservation_service.py` - 预约业务逻辑（冲突检测、费用计算等）
- `services/notification_service.py` - 通知服务（创建通知、发送邮件）

## 前端文件

- `templates/index.html` - 主页面模板
- `static/css/style.css` - 样式文件
- `static/js/app.js` - 前端 JavaScript 逻辑

## 快速开始

1. 安装依赖：`pip install -r requirements.txt`
2. 配置数据库：修改 `config.py` 中的数据库连接信息
3. 初始化数据库：`python init_db.py`
4. 运行项目：`python app.py`

## 功能清单

### ✅ 已实现功能

**用户端：**
- [x] 用户注册/登录
- [x] 查看场馆列表
- [x] 查看场馆详情
- [x] 创建预约（自动计算费用）
- [x] 查看我的预约
- [x] 取消预约（开场前1小时内禁止）
- [x] 邮件通知

**管理员端：**
- [x] 场馆管理（CRUD）
- [x] 查看所有预约
- [x] 手动修改/取消预约
- [x] 查看统计数据

**业务规则：**
- [x] 同一用户同一时间段只能有一个有效预约
- [x] 单次预约时长不超过2小时
- [x] 开场前1小时内禁止取消
- [x] 教职工免费，学生按标准收费

