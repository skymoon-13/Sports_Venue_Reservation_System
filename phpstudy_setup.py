"""
phpStudy MySQL 配置助手
"""
import os

def find_phpstudy_mysql():
    """查找 phpStudy MySQL 路径"""
    common_paths = [
        r"C:\phpStudy\PHPTutorial\MySQL\bin\mysql.exe",
        r"D:\phpStudy\PHPTutorial\MySQL\bin\mysql.exe",
        r"E:\phpStudy\PHPTutorial\MySQL\bin\mysql.exe",
        r"C:\phpstudy\PHPTutorial\MySQL\bin\mysql.exe",
        r"D:\phpstudy\PHPTutorial\MySQL\bin\mysql.exe",
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            return path
    
    return None

def create_database_sql():
    """生成创建数据库的 SQL"""
    sql = """
-- 创建数据库
CREATE DATABASE IF NOT EXISTS venue_booking 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- 查看数据库
SHOW DATABASES LIKE 'venue_booking';
"""
    return sql

if __name__ == '__main__':
    print("=" * 60)
    print("phpStudy MySQL 配置助手")
    print("=" * 60)
    
    mysql_path = find_phpstudy_mysql()
    
    if mysql_path:
        print(f"\n✓ 找到 phpStudy MySQL: {mysql_path}")
        print("\n请按照以下步骤操作：")
        print("\n方法1：使用 phpMyAdmin（推荐）")
        print("1. 打开 phpStudy 控制面板")
        print("2. 点击 'MySQL管理器' -> 'phpMyAdmin'")
        print("3. 在左侧点击 'SQL' 标签")
        print("4. 复制以下 SQL 并执行：")
        print("\n" + "-" * 60)
        print(create_database_sql())
        print("-" * 60)
    else:
        print("\n未找到 phpStudy MySQL 路径")
        print("请手动查找 phpStudy 安装目录")
    
    print("\n方法2：使用命令行")
    print("1. 打开命令提示符（CMD）")
    print("2. 进入 phpStudy MySQL 目录（例如）：")
    print("   cd C:\\phpStudy\\PHPTutorial\\MySQL\\bin")
    print("3. 执行以下命令：")
    print("   mysql.exe -u root -p")
    print("4. 输入密码（phpStudy 默认密码通常是 'root'）")
    print("5. 执行以下 SQL：")
    print("\n" + "-" * 60)
    print(create_database_sql())
    print("-" * 60)
    
    print("\n" + "=" * 60)
    print("数据库创建完成后，请修改 config.py：")
    print("\n如果 root 密码是 'root'：")
    print("  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/venue_booking?charset=utf8mb4'")
    print("\n如果 root 密码为空：")
    print("  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/venue_booking?charset=utf8mb4'")
    print("=" * 60)

