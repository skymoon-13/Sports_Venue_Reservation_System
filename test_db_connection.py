"""
数据库连接测试脚本
用于检查数据库配置是否正确
"""
from config import Config
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

def test_connection():
    """测试数据库连接"""
    print("=" * 50)
    print("数据库连接测试")
    print("=" * 50)
    
    # 获取数据库连接字符串
    db_uri = Config.SQLALCHEMY_DATABASE_URI
    print(f"\n连接字符串: {db_uri.replace(db_uri.split('@')[0].split('//')[1].split(':')[1] if ':' in db_uri.split('@')[0].split('//')[1] else '', '***') if '@' in db_uri else db_uri}")
    
    # 先测试 MySQL 服务器连接（不指定数据库）
    import urllib.parse
    server_uri = db_uri.rsplit('/', 1)[0]  # 移除数据库名部分
    print(f"\n[步骤1] 测试 MySQL 服务器连接...")
    print(f"服务器连接: {server_uri.split('@')[0].split('//')[1].split(':')[0] if '@' in server_uri else ''}:***@{server_uri.split('@')[1] if '@' in server_uri else ''}")
    
    try:
        server_engine = create_engine(server_uri)
        with server_engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            result.fetchone()
        print("✓ MySQL 服务器连接成功！")
    except OperationalError as e:
        error_msg = str(e)
        print(f"✗ MySQL 服务器连接失败！")
        print(f"错误: {error_msg}")
        
        if "Access denied" in error_msg:
            print("\n⚠ 密码验证失败！")
            print("可能的原因：")
            print("  1. phpStudy 的 root 密码可能不是 'root'")
            print("  2. 请打开 phpStudy -> MySQL管理器 -> phpMyAdmin")
            print("  3. 尝试登录，确认实际密码")
            print("  4. 如果密码为空，修改 config.py 为：")
            print("     mysql+pymysql://root@localhost:3306/venue_booking?charset=utf8mb4")
        elif "Can't connect" in error_msg or "2003" in error_msg:
            print("\n⚠ 无法连接到 MySQL 服务器！")
            print("  1. 确认 phpStudy MySQL 已启动")
            print("  2. 检查端口号（phpStudy 可能使用其他端口）")
            print("  3. 在 phpStudy 控制面板查看实际端口")
        
        return False
    
    # 测试数据库连接
    print(f"\n[步骤2] 测试数据库 'venue_booking' 连接...")
    print("\n正在测试连接...")
    
    try:
        # 创建引擎
        engine = create_engine(db_uri)
        
        # 测试连接
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            result.fetchone()
        
        print("✓ 数据库连接成功！")
        
        # 检查数据库是否存在
        try:
            with engine.connect() as conn:
                result = conn.execute(text("SHOW DATABASES LIKE 'venue_booking'"))
                db_exists = result.fetchone()
                
                if db_exists:
                    print("✓ 数据库 'venue_booking' 已存在")
                else:
                    print("✗ 数据库 'venue_booking' 不存在")
                    print("\n请先创建数据库，执行以下 SQL：")
                    print("CREATE DATABASE venue_booking CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
                    return False
        except Exception as e:
            print(f"✗ 检查数据库时出错: {str(e)}")
            return False
        
        return True
        
    except OperationalError as e:
        error_msg = str(e)
        print("✗ 数据库连接失败！")
        print(f"\n错误信息: {error_msg}")
        
        # 提供常见错误的解决方案
        if "Access denied" in error_msg:
            print("\n可能的原因：")
            print("  1. 用户名或密码错误")
            print("  2. 请检查 config.py 中的数据库连接信息")
            print("  3. 如果 root 密码为空，使用：mysql+pymysql://root@localhost:3306/venue_booking")
        elif "Can't connect" in error_msg or "2003" in error_msg:
            print("\n可能的原因：")
            print("  1. MySQL 服务未启动")
            print("  2. 端口号错误（默认 3306）")
            print("  3. 如果使用 XAMPP，请确保 MySQL 已启动")
        elif "Unknown database" in error_msg:
            print("\n可能的原因：")
            print("  1. 数据库 'venue_booking' 尚未创建")
            print("  2. 请先创建数据库")
        
        return False
    except Exception as e:
        print(f"✗ 发生未知错误: {str(e)}")
        return False

if __name__ == '__main__':
    success = test_connection()
    
    if success:
        print("\n" + "=" * 50)
        print("数据库配置正确！可以运行项目了。")
        print("下一步：运行 python init_db.py 初始化数据库表")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("请先解决上述问题，然后重新运行此脚本测试。")
        print("详细配置说明请查看：数据库配置指南.md")
        print("=" * 50)

