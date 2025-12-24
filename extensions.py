"""
Flask 扩展初始化
"""
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# 初始化扩展
db = SQLAlchemy()
mail = Mail()

