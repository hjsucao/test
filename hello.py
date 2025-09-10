import random

def get_random_6_digits():
    """
    获取6位随机数
    返回值范围：100000-999999
    """
    return random.randint(100000, 999999)

# 测试随机数方法
random_number = get_random_6_digits()
print(f"6位随机数: {random_number}")