"""
更新数据库表结构（添加payment_status字段）
"""
from app import create_app
from extensions import db
from sqlalchemy import text

def update_database():
    """更新数据库表结构"""
    app = create_app()
    
    with app.app_context():
        try:
            # 检查payment_status字段是否存在
            result = db.session.execute(text("""
                SELECT COUNT(*) as count 
                FROM information_schema.COLUMNS 
                WHERE TABLE_SCHEMA = DATABASE() 
                AND TABLE_NAME = 'reservations' 
                AND COLUMN_NAME = 'payment_status'
            """))
            
            count = result.fetchone()[0]
            
            if count == 0:
                print("检测到数据库表缺少 payment_status 字段，正在添加...")
                
                # 添加payment_status字段
                db.session.execute(text("""
                    ALTER TABLE reservations 
                    ADD COLUMN payment_status VARCHAR(20) NOT NULL DEFAULT 'unpaid' 
                    AFTER status
                """))
                
                # 更新现有数据
                # 已取消的预约设为free，其他的根据用户角色判断
                db.session.execute(text("""
                    UPDATE reservations r
                    INNER JOIN users u ON r.user_id = u.id
                    SET r.payment_status = CASE 
                        WHEN r.status = 'cancelled' THEN 'free'
                        WHEN u.role = 'teacher' OR u.role = 'admin' THEN 'free'
                        WHEN r.price = 0 THEN 'free'
                        ELSE 'unpaid'
                    END
                """))
                
                db.session.commit()
                print("✓ 数据库表结构更新成功！")
            else:
                print("✓ payment_status 字段已存在，无需更新")
            
            print("\n数据库更新完成！")
            
        except Exception as e:
            db.session.rollback()
            print(f"✗ 更新失败: {str(e)}")
            print("\n如果更新失败，可以手动执行以下SQL：")
            print("""
ALTER TABLE reservations 
ADD COLUMN payment_status VARCHAR(20) NOT NULL DEFAULT 'unpaid' AFTER status;

UPDATE reservations r
INNER JOIN users u ON r.user_id = u.id
SET r.payment_status = CASE 
    WHEN r.status = 'cancelled' THEN 'free'
    WHEN u.role = 'teacher' OR u.role = 'admin' THEN 'free'
    WHEN r.price = 0 THEN 'free'
    ELSE 'unpaid'
END;
            """)
            return False
    
    return True

if __name__ == '__main__':
    update_database()

