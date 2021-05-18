from pytestModel.decorator import  *
#调用其它文件的固件
#情形一：用装饰器
@pytest.mark.usefixtures(name=login)
def test_demo():
    print("这里是测试demo1，  在使用", login)

#情形二：直接调用
def test_demo2(login, login7): # 固件调用顺序参考：作用域——>>参数顺序
    print("这里是测试demo1，  在使用", login)

#情形三：跳过测试用例的三种方式，以下装饰器的方式时用在测试函数外的， pytestModel.skip("我就是要跳过去")可以用在很多地方，甚至用于跳过整个模块的测试
# @pytestModel.mark.skip(reason="莫须有")
@pytest.mark.skipif(condition="1 > 3", reason="莫须有")
def test_demo3(): # 固件调用顺序参考：作用域——>>参数顺序
    print("这里是跳过测试")
    pytest.skip("我就是要跳过去")


#情形四：预判成功或失败
@pytest.mark.xfail(condition="2>1", reason="kkkkk", run=True )  # condition用于规定xfail是否执行，run用于规定测试函数test_demo4是否执行
def test_demo4(): # 固件调用顺序参考：作用域——>>参数顺序
    print("这里是测试xfail的使用")
    assert 11 > 2


#情形五：携带参数
# argnames：指定测试函数里要参数化的形参。列表或字符串格式。
# argvalues：定义测试用例（要传给测试函数的实参）。列表格式，列表中每个元素（元组）对应生成一条测试用例。
# ids：同测试固件参数化作用一样,设置每一条测试用例的id。
@pytest.mark.parametrize(argnames=['a', 'b', 'c'],
# @pytestModel.mark.parametrize(argnames='a,b,c',
                         argvalues=[(1,2,3), (-1, -2, -3)],
                         ids=['two_first', 'two_second'],
                         scope="module")   # scope指定范围改变了该测试函数的执行位置
def test_demo5(login, a, b, c): # 固件调用顺序参考：作用域——>>参数顺序
    print("这里是测试xparametrize参数的使用", a, b, c, login)

