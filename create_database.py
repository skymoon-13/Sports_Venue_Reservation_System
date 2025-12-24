"""
自动创建数据库脚本
用于在 MySQL 中创建 venue_booking 数据库
"""
import subprocess
import sys
import os

def find_mysql():
    """查找 MySQL 可执行文件"""
    # 检查 XAMPP 路径
    xampp_paths = [
        r"C:\xampp\mysql\bin\mysql.exe",
        r"D:\xampp\mysql\bin\mysql.exe",
        r"E:\xampp\mysql\bin\mysql.exe"
    ]
    
    for path in xampp_paths:
        if os.path.exists(path):
            return path
    
    # 检查系统 PATH
    try:
        subprocess.run(['mysql', '--version'], 
                      capture_output=True, 
                      timeout=2)
        return 'mysql'
    except:
        pass
    
    return None

def create_database():
    """创建数据库"""
    print("=" * 60)
    print("创建数据库：venue_booking")
    print("=" * 60)
    
    mysql_path = find_mysql()
    
    if not mysql_path:
        print("\n✗ 未找到 MySQL！")
        print("请先安装 MySQL 或 XAMPP")
        print("详细说明请查看：MySQL安装指南.md")
        return False
    
    print(f"\n找到 MySQL: {mysql_path}")
    
    # SQL 命令
    sql_commands = [
        "CREATE DATABASE IF NOT EXISTS venue_booking CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
        "SHOW DATABASES LIKE 'venue_booking';"
    ]
    
    # 构建命令
    if mysql_path.endswith('.exe'):
        # XAMPP 默认 root 无密码
        cmd = [mysql_path, '-u', 'root']
    else:
        cmd = ['mysql', '-u', 'root', '-p']
    
    # 执行 SQL
    try:
        print("\n正在创建数据库...")
        print("提示：如果提示输入密码，XAMPP 默认 root 密码为空，直接按回车")
        
        # 使用管道输入 SQL
        sql_input = '\n'.join(sql_commands)
        
        if mysql_path.endswith('.exe'):
            result = subprocess.run(
                cmd,
                input=sql_input,
                text=True,
                capture_output=True,
                timeout=10
            )
        else:
            # 对于需要密码的情况，提示用户
            print("\n请输入 MySQL root 密码（如果为空直接按回车）：")
            result = subprocess.run(
                cmd,
                input=sql_input,
                text=True,
                capture_output=True,
                timeout=10
            )
        
        if result.returncode == 0:
            print("✓ 数据库创建成功！")
            if 'venue_booking' in result.stdout:
                print("✓ 数据库 'venue_booking' 已存在")
            return True
        else:
            print(f"✗ 创建失败: {result.stderr}")
            if 'Access denied' in result.stderr:
                print("\n提示：密码错误，请手动创建数据库：")
                print("1. 打开命令提示符")
                print("2. 执行: mysql -u root -p")
                print("3. 输入密码后执行: CREATE DATABASE venue_booking CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
            return False
            
    except subprocess.TimeoutExpired:
        print("✗ 操作超时")
        return False
    except Exception as e:
        print(f"✗ 发生错误: {str(e)}")
        return False

if __name__ == '__main__':
    success = create_database()
    
    if success:
        print("\n" + "=" * 60)
        print("数据库创建完成！")
        print("\n下一步：")
        print("1. 修改 config.py 中的数据库连接信息")
        print("   - 如果 root 密码为空：mysql+pymysql://root@localhost:3306/venue_booking")
        print("   - 如果有密码：mysql+pymysql://root:你的密码@localhost:3306/venue_booking")
        print("2. 运行 'python test_db_connection.py' 测试连接")
        print("3. 运行 'python init_db.py' 初始化数据表")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("请先解决上述问题后重试")
        print("=" * 60)

