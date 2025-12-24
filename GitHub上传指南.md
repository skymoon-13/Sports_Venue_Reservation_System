# GitHub 上传指南

## 第一步：在 GitHub 上创建仓库

1. 登录 GitHub（如果没有账号，先注册：https://github.com）
2. 点击右上角的 **+** 号，选择 **New repository**
3. 填写仓库信息：
   - Repository name: `venue-booking-system`（或你喜欢的名字）
   - Description: `体育场馆预约系统 - Flask + MySQL`
   - 选择 **Public**（公开）或 **Private**（私有）
   - **不要**勾选 "Initialize this repository with a README"
4. 点击 **Create repository**

## 第二步：在本地初始化 Git 仓库

打开项目目录，在终端/命令行中执行：

### Windows PowerShell 或 CMD：

```bash
# 1. 进入项目目录（替换为你的实际路径）
cd D:\你的项目路径

# 2. 初始化 Git 仓库
git init

# 3. 添加所有文件
git add .

# 4. 提交文件
git commit -m "Initial commit: 体育场馆预约系统"

# 5. 添加远程仓库（替换 YOUR_USERNAME 和 YOUR_REPO_NAME）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 6. 推送到 GitHub
git branch -M main
git push -u origin main
```

## 第三步：详细步骤说明

### 1. 检查 Git 是否已安装

```bash
git --version
```

如果没有安装，下载安装：https://git-scm.com/download/win

### 2. 初始化仓库

```bash
git init
```

### 3. 配置 Git（如果还没配置）

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

### 4. 添加文件

```bash
# 添加所有文件
git add .

# 或者只添加特定文件
git add *.py
git add *.md
git add templates/
git add static/
```

### 5. 提交文件

```bash
git commit -m "Initial commit: 体育场馆预约系统完整代码"
```

### 6. 连接远程仓库

```bash
# 替换 YOUR_USERNAME 为你的 GitHub 用户名
# 替换 YOUR_REPO_NAME 为你的仓库名
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### 7. 推送到 GitHub

```bash
# 设置主分支为 main
git branch -M main

# 推送到 GitHub
git push -u origin main
```

## 第四步：如果遇到问题

### 问题1：提示需要认证

**解决方案：**
- 使用 Personal Access Token（推荐）
  1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  2. 点击 "Generate new token"
  3. 选择权限：至少勾选 `repo`
  4. 生成后复制 token
  5. 推送时使用 token 作为密码

- 或者使用 SSH（更安全）
  ```bash
  # 生成 SSH key
  ssh-keygen -t ed25519 -C "your_email@example.com"
  
  # 复制公钥到 GitHub
  # Settings → SSH and GPG keys → New SSH key
  ```

### 问题2：提示 "remote origin already exists"

**解决方案：**
```bash
# 删除现有远程仓库
git remote remove origin

# 重新添加
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### 问题3：推送被拒绝

**解决方案：**
```bash
# 先拉取远程代码（如果有）
git pull origin main --allow-unrelated-histories

# 然后再推送
git push -u origin main
```

## 第五步：后续更新

以后修改代码后，使用以下命令更新：

```bash
# 1. 查看修改的文件
git status

# 2. 添加修改的文件
git add .

# 3. 提交修改
git commit -m "更新说明：例如：修复预约功能"

# 4. 推送到 GitHub
git push
```

## 注意事项

1. **不要上传敏感信息**：
   - 数据库密码
   - 邮件密码
   - SECRET_KEY
   - 这些应该在 `.env` 文件中，并已添加到 `.gitignore`

2. **检查 .gitignore**：
   确保以下内容不会被上传：
   - `venv/`（虚拟环境）
   - `__pycache__/`（Python缓存）
   - `.env`（环境变量）
   - `*.log`（日志文件）

3. **README.md**：
   建议在 GitHub 上添加项目说明，包括：
   - 项目介绍
   - 安装步骤
   - 使用方法

## 快速命令总结

```bash
# 初始化
git init
git add .
git commit -m "Initial commit"

# 连接 GitHub
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## 需要帮助？

如果遇到问题，请提供：
1. 执行的命令
2. 错误信息
3. Git 版本：`git --version`

