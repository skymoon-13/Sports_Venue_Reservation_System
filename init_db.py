"""
数据库初始化脚本
用于创建初始数据（管理员账号、测试场馆等）
"""
from app import create_app
from extensions import db
from models.user import User
from models.venue import Venue
from datetime import time

def init_database():
    """初始化数据库"""
    app = create_app()
    
    with app.app_context():
        # 创建所有表
        db.create_all()
        print("✓ 数据库表创建成功")
        
        # 检查是否已有管理员
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(
                username='admin',
                email='admin@example.com',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            print("✓ 创建管理员账号: admin / admin123")
        
        # 检查是否已有测试场馆
        if Venue.query.count() == 0:
            venues = [
                Venue(
                    name='篮球场A',
                    location='体育馆一楼',
                    capacity=20,
                    open_time=time(8, 0, 0),
                    close_time=time(22, 0, 0),
                    price_per_hour=10.00
                ),
                Venue(
                    name='羽毛球场B',
                    location='体育馆二楼',
                    capacity=8,
                    open_time=time(9, 0, 0),
                    close_time=time(21, 0, 0),
                    price_per_hour=15.00
                ),
                Venue(
                    name='乒乓球室C',
                    location='体育馆三楼',
                    capacity=4,
                    open_time=time(8, 0, 0),
                    close_time=time(20, 0, 0),
                    price_per_hour=8.00
                )
            ]
            
            for venue in venues:
                db.session.add(venue)
            
            print("✓ 创建测试场馆数据")
        
        # 提交更改
        db.session.commit()
        print("✓ 数据库初始化完成！")
        print("\n默认管理员账号:")
        print("  用户名: admin")
        print("  密码: admin123")
        print("\n请登录后立即修改密码！")

if __name__ == '__main__':
    init_database()

