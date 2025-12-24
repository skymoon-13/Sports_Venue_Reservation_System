# 体育场馆预约系统

一个基于 Flask + MySQL 的校园体育场馆预约系统，支持学生、教职工和管理员三种角色。

## 技术栈

- **后端**: Python 3.7+ / Flask 2.3
- **数据库**: MySQL 5.7+
- **ORM**: SQLAlchemy
- **邮件**: Flask-Mail
- **前端**: HTML / CSS / JavaScript (原生)

## 功能特性

### 用户端功能
- ✅ 用户注册/登录
- ✅ 查看场馆列表和详情
- ✅ 创建预约（自动计算费用）
- ✅ 查看我的预约
- ✅ 取消预约（开场前1小时内禁止）
- ✅ 邮件通知

### 管理员功能
- ✅ 场馆管理（CRUD）
- ✅ 查看所有预约
- ✅ 手动修改/取消预约
- ✅ 查看统计数据

### 业务规则
- 同一用户同一时间段只能有一个有效预约
- 单次预约时长不超过2小时
- 开场前1小时内禁止取消
- 教职工预约免费，学生按场馆收费标准计费

## 项目结构

```
.
├── app.py                 # 主应用文件
├── config.py              # 配置文件
├── extensions.py          # Flask扩展初始化
├── requirements.txt       # 依赖包
├── README.md              # 项目说明
├── models/                # 数据模型
│   ├── __init__.py
│   ├── user.py           # 用户模型
│   ├── venue.py          # 场馆模型
│   ├── reservation.py    # 预约模型
│   └── notification.py   # 通知模型
├── routes/                # 路由
│   ├── __init__.py
│   ├── auth.py           # 认证路由
│   ├── venue.py          # 场馆路由
│   ├── reservation.py    # 预约路由
│   ├── admin.py          # 管理员路由
│   └── user.py           # 用户路由
├── services/             # 业务逻辑服务
│   ├── __init__.py
│   ├── reservation_service.py    # 预约服务
│   └── notification_service.py   # 通知服务
├── templates/            # 前端模板
│   └── index.html
└── static/              # 静态文件
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

## 安装与运行

### 1. 创建虚拟环境

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置数据库

1. 创建 MySQL 数据库：
```sql
CREATE DATABASE venue_booking CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. 修改 `config.py` 中的数据库连接信息：
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://用户名:密码@localhost:3306/venue_booking?charset=utf8mb4'
```

### 4. 配置邮件（可选）

修改 `config.py` 中的邮件配置：
```python
MAIL_SERVER = 'smtp.qq.com'  # 或其他SMTP服务器
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your_email@qq.com'
MAIL_PASSWORD = 'your_password'  # 如果是QQ邮箱，使用授权码
MAIL_DEFAULT_SENDER = 'your_email@qq.com'
```

### 5. 初始化数据库

**方法一：使用初始化脚本（推荐）**

```bash
python init_db.py
```

这会自动创建数据库表、管理员账号和测试场馆数据。

**方法二：手动初始化**

运行应用后，数据库表会自动创建。你也可以手动初始化：

```python
python
>>> from app import create_app
>>> from extensions import db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
```

### 6. 运行项目

```bash
python app.py
```

应用将在 `http://localhost:5000` 启动。

## API 接口文档

### 认证接口

- `POST /api/auth/register` - 用户注册
- `POST /api/auth/login` - 用户登录
- `POST /api/auth/logout` - 用户登出
- `GET /api/auth/me` - 获取当前用户信息

### 场馆接口

- `GET /api/venues` - 获取场馆列表
- `GET /api/venues/<id>` - 获取场馆详情

### 预约接口

- `POST /api/reservations` - 创建预约
- `GET /api/reservations` - 获取我的预约列表
- `GET /api/reservations/<id>` - 获取预约详情
- `POST /api/reservations/<id>/cancel` - 取消预约

### 管理员接口

- `POST /api/admin/venues` - 创建场馆
- `PUT /api/admin/venues/<id>` - 更新场馆
- `DELETE /api/admin/venues/<id>` - 删除场馆
- `GET /api/admin/reservations` - 获取所有预约
- `PUT /api/admin/reservations/<id>` - 修改预约
- `POST /api/admin/reservations/<id>/cancel` - 取消预约
- `GET /api/admin/statistics` - 获取统计数据

### 用户接口

- `GET /api/user/notifications` - 获取通知列表
- `POST /api/user/notifications/<id>/read` - 标记通知已读

## 使用示例

### 创建管理员账号

```python
python
>>> from app import create_app
>>> from extensions import db
>>> from models.user import User
>>> app = create_app()
>>> with app.app_context():
...     admin = User(username='admin', email='admin@example.com', role='admin')
...     admin.set_password('admin123')
...     db.session.add(admin)
...     db.session.commit()
```

### 创建测试场馆

```python
python
>>> from app import create_app
>>> from extensions import db
>>> from models.venue import Venue
>>> from datetime import time
>>> app = create_app()
>>> with app.app_context():
...     venue = Venue(
...         name='篮球场A',
...         location='体育馆一楼',
...         capacity=20,
...         open_time=time(8, 0, 0),
...         close_time=time(22, 0, 0),
...         price_per_hour=10.00
...     )
...     db.session.add(venue)
...     db.session.commit()
```

## 注意事项

1. **生产环境配置**: 请修改 `config.py` 中的 `SECRET_KEY` 为随机字符串
2. **数据库安全**: 生产环境请使用环境变量存储数据库密码
3. **邮件服务**: 如果不需要邮件功能，可以跳过邮件配置，但通知功能会受影响
4. **CORS**: 如果前后端分离部署，需要配置 CORS

## 开发说明

- 代码遵循 RESTful API 设计规范
- 使用 SQLAlchemy ORM 进行数据库操作
- 业务逻辑封装在 `services/` 目录
- 路由处理在 `routes/` 目录
- 数据模型在 `models/` 目录

## 许可证

本项目仅用于课程设计学习使用。

