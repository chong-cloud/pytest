import pytest
"""
注： -m 为根据maker， -k 为根据测试函数名，两个参数也可用于测试类
控制台运行命令：
pytestModel -sv -k "1" pytestini-test.py   # 函数名中带有1的所有测试用例
pytestModel -sv -m "web_test" pytestini-test.py
pytestModel -sv -m "web_test or app_test" pytestini-test.py
pytestModel -sv -m "web_test and app_test" pytestini-test.py
pytestModel -sv -m "not web_test" pytestini-test.py

pytestModel.ini中添加addopts = -sv后
pytestModel  -m "web_test" pytestini-test.py
pytestModel  -m "web_test or app_test" pytestini-test.py
pytestModel  -m "web_test and app_test" pytestini-test.py
pytestModel  -m "not web_test" pytestini-test.py

其它选项：
--ff / --failed-first：先执行上次失败的测试用例
--lf / --last-failed：只执行上次失败的测试用例
-x / --exitfirst：遇到测试用例fail，就结束测试
--maxfail=num：遇到num条测试用例fail, 就结束测试
--tb="style":打印断言失败的信息
    --tb=auto 有多个用例失败的时候，只打印第一个和最后一个用例的回溯信息
    --tb=long 输出最详细的回溯信息
    --tb=short 输入assert的一行和系统判断内容
    --tb=line 使用一行显示错误信息
    --tb=native 只输出python标准库的回溯信息
    --tb=no 不显示回溯信息


"""
@pytest.mark.web_test
def test_demo1():
    print("web_test")


@pytest.mark.app_test
def test_demo2():
    print("web_test")

@pytest.mark.app_test
@pytest.mark.web_test
def test_demo3():
    print("APP_test and web_test")