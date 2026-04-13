__all__ = ['area','aa']
PI = 3.14
NAME = __name__
def area(r):
    """
    计算圆的面积
    :param r: 半径
    :return: 面积
    """
    pi = 3.14
    return pi * r * r
def aa():
    print("1111111111111")
if __name__ == '__main__':
    print("测试")
    print(__name__)
    print(area(5))