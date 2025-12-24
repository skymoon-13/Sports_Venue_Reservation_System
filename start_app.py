"""
启动应用并显示详细错误信息
"""
import sys
import traceback

def start_app():
    """启动 Flask 应用"""
    try:
        print("=" * 60)
        print("正在启动体育场馆预约系统...")
        print("=" * 60)
        
        # 检查必要的模块
        print("\n[1] 检查依赖模块...")
        try:
            from flask import Flask
            from config import Config
            from extensions import db, mail
            print("  ✓ Flask 模块导入成功")
        except ImportError as e:
            print(f"  ✗ 导入失败: {e}")
            print("\n请先安装依赖：")
            print("  pip install -r requirements.txt")
            return False
        
        # 检查数据库配置
        print("\n[2] 检查数据库配置...")
        try:
            from config import Config
            db_uri = Config.SQLALCHEMY_DATABASE_URI
            print(f"  ✓ 数据库配置: {db_uri.split('@')[0]}@***")
        except Exception as e:
            print(f"  ✗ 配置错误: {e}")
            return False
        
        # 测试数据库连接
        print("\n[3] 测试数据库连接...")
        try:
            from sqlalchemy import create_engine, text
            engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("  ✓ 数据库连接成功")
        except Exception as e:
            print(f"  ✗ 数据库连接失败: {e}")
            print("\n请检查：")
            print("  1. MySQL 服务是否已启动")
            print("  2. config.py 中的数据库配置是否正确")
            print("  3. 数据库 'venue_booking' 是否已创建")
            return False
        
        # 启动应用
        print("\n[4] 启动 Flask 应用...")
        try:
            from app import create_app
            app = create_app()
            print("  ✓ 应用创建成功")
            print("\n" + "=" * 60)
            print("应用启动成功！")
            print("=" * 60)
            print("\n访问地址: http://localhost:5000")
            print("按 Ctrl+C 停止应用")
            print("=" * 60 + "\n")
            
            app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
        except Exception as e:
            print(f"  ✗ 启动失败: {e}")
            print("\n详细错误信息：")
            traceback.print_exc()
            return False
            
    except KeyboardInterrupt:
        print("\n\n应用已停止")
        return True
    except Exception as e:
        print(f"\n发生未知错误: {e}")
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = start_app()
    if not success:
        sys.exit(1)

