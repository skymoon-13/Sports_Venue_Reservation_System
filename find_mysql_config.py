"""
自动查找 phpStudy MySQL 正确配置
"""
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import urllib.parse

def test_config(host='localhost', port=3306, user='root', password='root', database=None):
    """测试数据库配置"""
    if database:
        uri = f'mysql+pymysql://{user}:{urllib.parse.quote_plus(password)}@{host}:{port}/{database}?charset=utf8mb4'
    else:
        uri = f'mysql+pymysql://{user}:{urllib.parse.quote_plus(password)}@{host}:{port}'
    
    try:
        engine = create_engine(uri)
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True, None
    except OperationalError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def find_correct_config():
    """查找正确的配置"""
    print("=" * 60)
    print("phpStudy MySQL 配置自动检测")
    print("=" * 60)
    
    # 测试常见密码
    passwords = ['root', '', '123456', '12345678']
    ports = [3306, 3307, 3308]
    
    print("\n正在测试常见配置组合...\n")
    
    for port in ports:
        for pwd in passwords:
            pwd_display = '(空密码)' if pwd == '' else pwd
            print(f"测试: 端口={port}, 密码={pwd_display}...", end=' ')
            
            success, error = test_config(port=port, password=pwd)
            
            if success:
                print("✓ 成功！")
                print("\n" + "=" * 60)
                print("找到正确配置：")
                print("=" * 60)
                print(f"  端口: {port}")
                print(f"  密码: {pwd_display}")
                
                # 生成配置字符串
                if pwd:
                    config_str = f"mysql+pymysql://root:{pwd}@localhost:{port}/venue_booking?charset=utf8mb4"
                else:
                    config_str = f"mysql+pymysql://root@localhost:{port}/venue_booking?charset=utf8mb4"
                
                print(f"\n请修改 config.py 第 17 行为：")
                print(f"  SQLALCHEMY_DATABASE_URI = '{config_str}'")
                
                # 检查数据库是否存在
                print("\n检查数据库 'venue_booking' 是否存在...")
                success_db, _ = test_config(port=port, password=pwd, database='venue_booking')
                if success_db:
                    print("✓ 数据库 'venue_booking' 已存在")
                else:
                    print("✗ 数据库 'venue_booking' 不存在，需要先创建")
                    print("\n创建数据库的 SQL：")
                    print("  CREATE DATABASE venue_booking CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
                
                print("=" * 60)
                return True
            else:
                if "Access denied" in error:
                    print("✗ (密码错误)")
                elif "Can't connect" in error:
                    print("✗ (无法连接)")
                else:
                    print("✗")
    
    print("\n" + "=" * 60)
    print("无法自动找到正确配置")
    print("=" * 60)
    print("\n请手动检查：")
    print("1. 打开 phpStudy 控制面板，查看 MySQL 端口号")
    print("2. 打开 phpStudy -> MySQL管理器 -> phpMyAdmin")
    print("3. 尝试登录，确认 root 密码")
    print("4. 根据实际情况修改 config.py")
    print("=" * 60)
    return False

if __name__ == '__main__':
    find_correct_config()

