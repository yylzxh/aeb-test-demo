#存放测试用例
from pickle import FALSE
import pytest
from aeb_controller import should_break
@pytest.mark.parametrize("speed,distance,expected", [
    #参数化列表：6个独立的子测试用例
    (70,8,True),#pytest每次遍历元组，将值赋值给测试函数的形参
    (50,30,False),
    (65,9,True),
    (60,10,False),
    (80,15,False),
    (22,22,False)
])
def test_aeb_brake_logic(speed, distance, expected):
    #执行测试函数体之前从参数化列表中取出数据，解包赋值给形参
    result = should_break(speed, distance)
    assert result == expected
    #6个测试用例各自具有独立生命周期