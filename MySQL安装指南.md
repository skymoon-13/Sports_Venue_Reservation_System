# MySQL 安装指南（使用 XAMPP）

## 为什么选择 XAMPP？
- ✅ 一键安装，包含 MySQL
- ✅ 图形界面管理，简单易用
- ✅ 适合学习和开发
- ✅ 免费开源

---

## 安装步骤

### 第一步：下载 XAMPP

1. 访问 XAMPP 官网：https://www.apachefriends.org/
2. 点击 "Download" 按钮
3. 选择 Windows 版本（通常会自动识别你的系统）
4. 下载安装包（约 150MB）

### 第二步：安装 XAMPP

1. 双击下载的安装包（例如：xampp-windows-x64-8.x.x-installer.exe）
2. 如果出现安全提示，点击 "是" 或 "允许"
3. 安装向导：
   - 点击 "Next"
   - 选择要安装的组件（至少选择 MySQL，其他可选）
   - 选择安装路径（默认 C:\xampp 即可）
   - 点击 "Next" 开始安装
   - 等待安装完成（可能需要几分钟）
   - 点击 "Finish"

### 第三步：启动 MySQL

1. 打开 XAMPP Control Panel
   - 可以在开始菜单搜索 "XAMPP Control Panel"
   - 或者在安装目录找到 `xampp-control.exe`

2. 在 XAMPP Control Panel 中：
   - 找到 "MySQL" 这一行
   - 点击 "Start" 按钮
   - 如果看到绿色背景，说明 MySQL 已启动

3. 如果启动失败：
   - 可能是端口被占用（3306 端口）
   - 可以点击 "Config" 修改端口
   - 或者关闭其他可能占用端口的程序

---

## 验证安装

### 方法1：使用 XAMPP 命令行

1. 在 XAMPP Control Panel 中，点击 MySQL 旁边的 "Shell" 按钮
2. 输入以下命令：
```bash
mysql -u root
```
3. 如果看到 `MariaDB [(none)]>` 提示符，说明安装成功！
4. 输入 `exit;` 退出

### 方法2：使用系统命令行

1. 打开命令提示符（CMD）或 PowerShell
2. 进入 XAMPP 的 MySQL 目录：
```bash
cd C:\xampp\mysql\bin
```
3. 执行：
```bash
mysql.exe -u root
```
4. 如果成功进入 MySQL，说明安装成功！

---

## 常见问题

### Q1: 启动 MySQL 时提示端口被占用？

**解决方案：**
- 打开 XAMPP Control Panel
- 点击 MySQL 旁边的 "Config" 按钮
- 选择 "my.ini"
- 找到 `port=3306`，改为其他端口（如 3307）
- 保存后重启 MySQL

### Q2: 找不到 XAMPP Control Panel？

**解决方案：**
- 在开始菜单搜索 "XAMPP"
- 或者直接进入安装目录（默认 C:\xampp）
- 运行 `xampp-control.exe`

### Q3: 安装时被杀毒软件拦截？

**解决方案：**
- 这是正常现象，XAMPP 是安全的
- 在杀毒软件中添加信任/白名单
- 或者暂时关闭杀毒软件安装

---

## 下一步

安装完成后，请告诉我，我会帮你：
1. 创建数据库
2. 配置项目连接
3. 测试连接
4. 初始化数据表

