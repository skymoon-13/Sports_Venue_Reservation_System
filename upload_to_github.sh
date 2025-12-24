#!/bin/bash

echo "========================================"
echo "GitHub 上传助手"
echo "========================================"
echo ""

# 检查 Git 是否安装
if ! command -v git &> /dev/null; then
    echo "[错误] Git 未安装！"
    echo "请先安装 Git"
    exit 1
fi

echo "[1] 检查 Git 状态..."
if [ ! -d ".git" ]; then
    echo "[信息] 初始化 Git 仓库..."
    git init
fi

echo ""
echo "[2] 添加所有文件..."
git add .

echo ""
echo "[3] 提交文件..."
read -p "请输入提交信息（直接回车使用默认）: " commit_msg
if [ -z "$commit_msg" ]; then
    commit_msg="Initial commit: 体育场馆预约系统"
fi
git commit -m "$commit_msg"

echo ""
echo "[4] 检查远程仓库..."
if ! git remote | grep -q origin; then
    echo "[提示] 需要添加远程仓库"
    read -p "请输入 GitHub 仓库地址（例如：https://github.com/username/repo.git）: " github_url
    if [ ! -z "$github_url" ]; then
        git remote add origin "$github_url"
    else
        echo "[错误] 未提供仓库地址，请手动添加"
        echo "使用命令: git remote add origin YOUR_REPO_URL"
        exit 1
    fi
fi

echo ""
echo "[5] 推送到 GitHub..."
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "[成功] 文件已成功上传到 GitHub！"
else
    echo ""
    echo "[错误] 推送失败！"
    echo "可能的原因："
    echo "1. 需要登录 GitHub（使用 Personal Access Token）"
    echo "2. 远程仓库地址错误"
    echo "3. 网络连接问题"
    echo ""
    echo "请检查错误信息并重试"
fi

