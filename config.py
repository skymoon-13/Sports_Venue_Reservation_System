"""
配置文件
"""
import os
from datetime import timedelta

class Config:
    """基础配置"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # 数据库配置
    # 格式：mysql+pymysql://用户名:密码@主机:端口/数据库名?charset=utf8mb4
    # 示例：
    #   - root密码为空：'mysql+pymysql://root@localhost:3306/venue_booking?charset=utf8mb4'
    #   - root密码123456：'mysql+pymysql://root:123456@localhost:3306/venue_booking?charset=utf8mb4'
    #   - 其他端口：'mysql+pymysql://root:password@localhost:3307/venue_booking?charset=utf8mb4'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/venue_booking?charset=utf8'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3306/venue_booking?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 邮件配置（需要根据实际情况修改）
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'noreply@example.com'
    
    # 业务规则配置
    MAX_BOOKING_DURATION_HOURS = 2  # 单次预约最大时长（小时）
    CANCEL_DEADLINE_HOURS = 1  # 开场前多少小时内禁止取消
    
    # JWT Token 配置（可选，当前使用 session）
    JWT_EXPIRATION_DELTA = timedelta(hours=24)
    
    # 注册码配置
    REGISTRATION_CODES = {
        'student': ['STUDENT2024', 'STUDENT2025'],  # 学生注册码
        'teacher': ['TEACHER2024', 'TEACHER2025']   # 教职工注册码
    }

