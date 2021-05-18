import pytest

"""
fixture里面有个scope参数可以控制fixture的作用范围：session>module>class>function

-function：每一个函数或方法都会调用
-class：每一个类调用一次，一个类中可以有多个方法
-module：每一个.py文件调用一次，该文件内又有多个function和class
-session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module

不同层级的固定功能，与set***和teardown***类似，但fixture的功能更强大

"""

#情形一：
@pytest.fixture() #此时相当于定义了setup***方法
def login():
    print("这里是fixure固件")
    result = "fixure固件"
    return result

def test_demo(login):
    print("这里是测试demo1，  在使用", login)

#情形2，与python自带的yield同理，遇到next时才开始执行logins内函数，返回result的值
@pytest.fixture() #此时相当于定义了setup***方法
def logins():
    print("这里是fixure固件")
    result = "fixure固件"
    yield result   #此处相当于teatdown***方法
    print("yield 之后运行的代码")

def test_demo1(logins):
    print("这里是测试demo1，  在使用", logins)

#情形3使用注册清理函数
@pytest.fixture() #此时相当于定义了setup***方法
def logink(request):
    print("这里是fixure固件")
    result = "fixure固件"

    def fin():
        print('退出登录')
    def fin1():
        print('退出登录1')


    # 注册一个清理函数
    request.addfinalizer(fin1)    #此处相当于teatdown***方法，执行顺序与注册的顺序相反
    # 注册一个清理函数
    request.addfinalizer(fin)
    # 注册完清理函数后，如果在测试固件里抛出异常,只有清理函数照常执
    return result

def test_demo2(logink):
    print("这里是测试demo22，  在使用", logink)


#情形四：增加name参数，指定固件的名字
@pytest.fixture(name="kk")
def login3():
    print("这里是fixure固件")
    result = "fixure固件"
    return result

def test_demo3(kk, login5):  # 可以部署多个固件，注意适用范围, 固件调用顺序参考：作用域——>>参数顺序,若定义了autouse则在同作用域中根据函数名的编码从小到大
    print("这里是测试demo1，  在使用", kk)

#情形五：增加scope参数
# 级别session > module > class > function

@pytest.fixture(scope="function") #此时因为定义了别名，函数名就不再冲突了
def login4():
    print("scope测试")
    result = "scope测试"
    return result

@pytest.fixture(scope="module") #此时因为定义了别名，函数名就不再冲突了
def login5():
    print("开始 scope测试-module")
    result = "scope测试-module"
    yield result
    print("结束 scope测试-module")

def test_demo4(login5):
    print("这里是测试demo1，  在使用", login5)

#情形六：增加params参数,实现测试固件的参数化

@pytest.fixture(params=['tom', 'jack'])
def login6(request):
    print('%s登录' % request.param)


def test_demo6(login6):
    print('执行测试test6')

@pytest.fixture(params=[('tom', '12'),('jack', '18')], ids=['user_a', 'user_b']) #ids与params的参数个数对应
def login7(request):
    print('%s登录, %s岁' % (request.param[0], request.param[1]))


def test_demo7(login7):
    print('执行测试test7')