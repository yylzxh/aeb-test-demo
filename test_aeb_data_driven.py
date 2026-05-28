import os
import pytest
import pandas as pd
base_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(base_dir, 'aeb_scenarios.xlsx')
from aeb_controller import should_break
#骨架：导入需要的库
    # 定义加载Excel的函数：
    #     读取Excel
    #     处理空值
    #     返回字典列表
    #
    # 定义测试函数：
    #     从用例中取speed, distance, expected
    #     如果是异常用例：
    #         用pytest.raises检查异常
    #     否则：
    #         调用被测函数，断言结果等于期望
def load_case():
    """ 从EXCEL加载所有用例，返回列表【字典】"""
    read=pd.read_excel(excel_path)
    read=read.fillna('')#将dataframe中的缺失值NaN/None填充为指定的值
    return read.to_dict('records')#将 DataFrame 转换为 Python 字典列表。
    # 'records' 模式表示每一行转换为一个字典，键为列名，值为该行的数据。最终返回一个列表，例如 [{"col1": val1, "col2": val2}, ...]
ALL_CASES=load_case()#
@pytest.mark.parametrize("case",ALL_CASES,ids=lambda c:f"ID_{c['case_id']}")##c：和c[]是什么意思
def test_aeb_brake(case):
    speed=case["speed"]###这三行是什么意思
    distance=case["distance"]
    expected=case["expected"]
    #处理异常用例,
    if expected=="Exception":#判断语句为什么在装饰器里面
        with pytest.raises(Exception):#with的作用没看懂-异常用例?
            should_break(speed, distance)
    else:
        if isinstance(expected, str):#检查对象 expected 是否为指定类型（这里是 str 字符串类型）
            expected=expected.lower()=="true"#将字符串中的所有大写字母转换为小写字母，返回新字符串，这里配合 == "true" 实现判断返回布尔值T/F
        result = should_break(speed, distance)
        assert result == expected,f"speed={speed}.distance={distance},expected={expected},got={result}"
