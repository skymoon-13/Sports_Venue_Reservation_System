"""
详细的数据库连接测试脚本
用于排查连接问题
"""
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import urllib.parse

def test_connection_without_db(host='localhost', port=3306, user='root', password='root'):
    """测试连接到 MySQL 服务器（不指定数据库）"""
    print("=" * 60)
    print("测试 MySQL 服务器连接（不指定数据库）")
    print("=" * 60)
    
    # 构建连接字符串（不包含数据库名）
    db_uri = f'mysql+pymysql://{user}:{urllib.parse.quote_plus(password)}@{host}:{port}'
    print(f"\n连接字符串: mysql+pymysql://{user}:***@{host}:{port}")
    print("正在测试...")
    
    try:
        engine = create_engine(db_uri)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            result.fetchone()
        print("✓ MySQL 服务器连接成功！")
        return True
    except OperationalError as e:
        error_msg = str(e)
        print(f"✗ 连接失败: {error_msg}")
        
        if "Access denied" in error_msg:
            print("\n密码验证失败！可能的原因：")
            print("  1. 密码确实不对")
            print("  2. phpStudy 的 root 密码可能不是 'root'")
            print("  3. 可能需要使用其他用户")
            print("\n建议：")
            print("  1. 打开 phpStudy 控制面板")
            print("  2. 点击 'MySQL管理器' -> 'phpMyAdmin'")
            print("  3. 尝试用 root 和你的密码登录")
            print("  4. 如果登录成功，说明密码是对的")
        elif "Can't connect" in error_msg or "2003" in error_msg:
            print("\n无法连接到 MySQL 服务器！")
            print("  1. 确认 phpStudy MySQL 已启动")
            print("  2. 检查端口号是否正确（phpStudy 可能使用其他端口）")
            print("  3. 在 phpStudy 控制面板查看 MySQL 端口")
        
        return False
    except Exception as e:
        print(f"✗ 发生错误: {str(e)}")
        return False

def test_different_passwords():
    """测试不同的密码组合"""
    print("\n" + "=" * 60)
    print("尝试常见密码组合")
    print("=" * 60)
    
    passwords = ['root', '', '123456', '12345678', 'admin']
    
    for pwd in passwords:
        print(f"\n尝试密码: {'(空密码)' if pwd == '' else pwd}")
        if test_connection_without_db(password=pwd):
            print(f"\n✓ 找到正确密码: {'(空密码)' if pwd == '' else pwd}")
            return pwd
    
    return None

def test_different_ports():
    """测试不同的端口"""
    print("\n" + "=" * 60)
    print("尝试常见端口")
    print("=" * 60)
    
    ports = [3306, 3307, 3308, 3309]
    
    for port in ports:
        print(f"\n尝试端口: {port}")
        if test_connection_without_db(port=port):
            print(f"\n✓ 找到正确端口: {port}")
            return port
    
    return None

if __name__ == '__main__':
    print("\n开始详细测试...\n")
    
    # 首先测试默认配置
    print("第一步：测试默认配置（root/root，端口3306）")
    success = test_connection_without_db()
    
    if not success:
        print("\n默认配置失败，开始排查...")
        
        # 测试不同密码
        print("\n第二步：测试不同密码")
        correct_password = test_different_passwords()
        
        if not correct_password:
            # 测试不同端口
            print("\n第三步：测试不同端口")
            correct_port = test_different_ports()
            
            if correct_port:
                print(f"\n找到正确端口: {correct_port}")
                print(f"请修改 config.py，将端口改为 {correct_port}")
            else:
                print("\n" + "=" * 60)
                print("无法自动找到正确配置")
                print("=" * 60)
                print("\n请手动检查：")
                print("1. phpStudy 控制面板 -> 查看 MySQL 端口号")
                print("2. phpStudy -> MySQL管理器 -> phpMyAdmin -> 尝试登录，确认密码")
                print("3. 根据实际情况修改 config.py")
        else:
            print(f"\n找到正确密码: {correct_password if correct_password else '(空密码)'}")
            if correct_password:
                print(f"请修改 config.py，将密码改为: {correct_password}")
            else:
                print("请修改 config.py，使用空密码: mysql+pymysql://root@localhost:3306/venue_booking")
    else:
        print("\n" + "=" * 60)
        print("✓ 默认配置正确！")
        print("=" * 60)
        print("\n如果还是连接失败，可能是数据库 'venue_booking' 不存在")
        print("请先创建数据库，然后重新测试")

