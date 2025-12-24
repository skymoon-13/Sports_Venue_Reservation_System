"""
检查 MySQL 是否已安装并运行
"""
import subprocess
import sys
import os

def check_mysql_installed():
    """检查 MySQL 是否已安装"""
    print("=" * 60)
    print("MySQL 安装检查")
    print("=" * 60)
    
    # 检查常见安装路径
    xampp_paths = [
        r"C:\xampp\mysql\bin\mysql.exe",
        r"D:\xampp\mysql\bin\mysql.exe",
        r"E:\xampp\mysql\bin\mysql.exe"
    ]
    
    mysql_found = False
    mysql_path = None
    
    # 检查 XAMPP
    print("\n[1] 检查 XAMPP MySQL...")
    for path in xampp_paths:
        if os.path.exists(path):
            print(f"  ✓ 找到 XAMPP MySQL: {path}")
            mysql_found = True
            mysql_path = path
            break
    
    if not mysql_found:
        print("  ✗ 未找到 XAMPP MySQL")
    
    # 检查系统 PATH 中的 MySQL
    print("\n[2] 检查系统 MySQL...")
    try:
        result = subprocess.run(['mysql', '--version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            print(f"  ✓ 找到系统 MySQL: {result.stdout.strip()}")
            mysql_found = True
            mysql_path = "mysql"
    except FileNotFoundError:
        print("  ✗ 未找到系统 MySQL")
    except Exception as e:
        print(f"  ✗ 检查出错: {str(e)}")
    
    # 检查 MySQL 服务是否运行
    print("\n[3] 检查 MySQL 服务状态...")
    try:
        result = subprocess.run(['sc', 'query', 'MySQL'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if 'RUNNING' in result.stdout:
            print("  ✓ MySQL 服务正在运行")
        elif 'STOPPED' in result.stdout:
            print("  ⚠ MySQL 服务已安装但未运行")
            print("    提示：如果使用 XAMPP，请在 XAMPP Control Panel 中启动 MySQL")
        else:
            print("  ✗ 未找到 MySQL 服务")
    except Exception as e:
        print(f"  ⚠ 无法检查服务状态（可能未安装为服务）")
    
    # 测试连接
    print("\n[4] 测试 MySQL 连接...")
    if mysql_path:
        try:
            # 尝试连接（XAMPP 默认 root 无密码）
            if mysql_path.endswith('.exe'):
                result = subprocess.run([mysql_path, '-u', 'root', '-e', 'SELECT 1'], 
                                      capture_output=True, 
                                      text=True, 
                                      timeout=5)
            else:
                result = subprocess.run([mysql_path, '-u', 'root', '-e', 'SELECT 1'], 
                                      capture_output=True, 
                                      text=True, 
                                      timeout=5)
            
            if result.returncode == 0:
                print("  ✓ MySQL 连接成功！")
                return True, mysql_path
            else:
                print(f"  ✗ 连接失败: {result.stderr}")
                print("    提示：可能需要输入密码，或 MySQL 未启动")
        except Exception as e:
            print(f"  ✗ 连接测试失败: {str(e)}")
    
    return mysql_found, mysql_path

def show_installation_guide():
    """显示安装指南"""
    print("\n" + "=" * 60)
    print("MySQL 未安装或未运行")
    print("=" * 60)
    print("\n推荐安装方式：XAMPP（最简单）")
    print("\n安装步骤：")
    print("1. 访问 https://www.apachefriends.org/")
    print("2. 下载 Windows 版本的 XAMPP")
    print("3. 运行安装程序，至少选择 MySQL 组件")
    print("4. 安装完成后，打开 XAMPP Control Panel")
    print("5. 点击 MySQL 旁边的 'Start' 按钮")
    print("\n详细说明请查看：MySQL安装指南.md")
    print("=" * 60)

if __name__ == '__main__':
    mysql_found, mysql_path = check_mysql_installed()
    
    print("\n" + "=" * 60)
    if mysql_found:
        print("✓ MySQL 已安装！")
        if mysql_path:
            print(f"  路径: {mysql_path}")
        print("\n下一步：")
        print("1. 确保 MySQL 服务已启动（XAMPP Control Panel 中启动）")
        print("2. 运行 'python create_database.py' 创建数据库")
        print("3. 修改 config.py 中的数据库连接信息")
        print("4. 运行 'python test_db_connection.py' 测试连接")
    else:
        show_installation_guide()
    print("=" * 60)

