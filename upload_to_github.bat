@echo off
echo ========================================
echo GitHub 上传助手
echo ========================================
echo.

REM 检查 Git 是否安装
git --version >nul 2>&1
if errorlevel 1 (
    echo [错误] Git 未安装！
    echo 请先安装 Git: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [1] 检查 Git 状态...
git status >nul 2>&1
if errorlevel 1 (
    echo [信息] 初始化 Git 仓库...
    git init
)

echo.
echo [2] 添加所有文件...
git add .

echo.
echo [3] 提交文件...
set /p commit_msg="请输入提交信息（直接回车使用默认）: "
if "%commit_msg%"=="" set commit_msg=Initial commit: 体育场馆预约系统
git commit -m "%commit_msg%"

echo.
echo [4] 检查远程仓库...
git remote -v >nul 2>&1
if errorlevel 1 (
    echo [提示] 需要添加远程仓库
    set /p github_url="请输入 GitHub 仓库地址（例如：https://github.com/username/repo.git）: "
    if not "%github_url%"=="" (
        git remote add origin "%github_url%"
    ) else (
        echo [错误] 未提供仓库地址，请手动添加
        echo 使用命令: git remote add origin YOUR_REPO_URL
        pause
        exit /b 1
    )
)

echo.
echo [5] 推送到 GitHub...
git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo [错误] 推送失败！
    echo 可能的原因：
    echo 1. 需要登录 GitHub（使用 Personal Access Token）
    echo 2. 远程仓库地址错误
    echo 3. 网络连接问题
    echo.
    echo 请检查错误信息并重试
) else (
    echo.
    echo [成功] 文件已成功上传到 GitHub！
)

echo.
pause

