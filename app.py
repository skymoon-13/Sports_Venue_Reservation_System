"""
体育场馆预约系统 - 主应用文件
"""
from flask import Flask
from config import Config
from extensions import db, mail

def create_app(config_class=Config):
    """应用工厂函数"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # 初始化扩展
    db.init_app(app)
    mail.init_app(app)
    
    # 注册蓝图
    from routes.auth import auth_bp
    from routes.venue import venue_bp
    from routes.reservation import reservation_bp
    from routes.admin import admin_bp
    from routes.user import user_bp
    from routes.feedback import feedback_bp
    from routes.payment import payment_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(venue_bp, url_prefix='/api/venues')
    app.register_blueprint(reservation_bp, url_prefix='/api/reservations')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(feedback_bp, url_prefix='/api/feedbacks')
    app.register_blueprint(payment_bp, url_prefix='/api/payment')
    
    # 注册前端路由（用于页面访问）
    from flask import send_from_directory, send_file
    import os
    
    @app.route('/')
    def index():
        return send_file(os.path.join('templates', 'index.html'))
    
    @app.route('/test')
    def test_page():
        """API测试页面"""
        return send_file('test_api_connection.html')
    
    # 静态文件路由
    @app.route('/static/<path:filename>')
    def static_files(filename):
        return send_from_directory('static', filename)
    
    # 创建数据库表
    with app.app_context():
        try:
            db.create_all()
            # 检查并更新payment_status字段（如果不存在）
            from sqlalchemy import inspect, text
            inspector = inspect(db.engine)
            columns = [col['name'] for col in inspector.get_columns('reservations')]
            if 'payment_status' not in columns:
                try:
                    db.session.execute(text("""
                        ALTER TABLE reservations 
                        ADD COLUMN payment_status VARCHAR(20) NOT NULL DEFAULT 'unpaid' 
                        AFTER status
                    """))
                    db.session.commit()
                    print("✓ 已添加 payment_status 字段")
                except Exception as e:
                    db.session.rollback()
                    print(f"⚠ 添加 payment_status 字段失败: {e}")
                    print("请运行 python update_database.py 手动更新")
        except Exception as e:
            print(f"⚠ 数据库初始化警告: {e}")
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

