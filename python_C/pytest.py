from ctypes import *

# 基本打印demo
def test01():
    ll = cdll.LoadLibrary   
    lib = ll("./pytest.so")
    lib.hello()

# C基本类型参数
def test02():
    ll = cdll.LoadLibrary   
    lib = ll("./pytest.so")
    c = lib.add(1,2)
    print(c)

# 传入C指针类型
def test03():
    ll = cdll.LoadLibrary   
    lib = ll("./pytest.so")  
    a = (c_int)(2)
    a_p = POINTER(c_int)(a)
    lib.inc(a_p)
    print(a_p[0])
    print(a.value)

# 传入数组指针类型
def test04():
    ll = cdll.LoadLibrary   
    lib = ll("./pytest.so")
    arr = [1,2,3,4]
    a = (c_int*len(arr))(*arr)
    a_p = POINTER(c_int)(a)
    lib.printArr(a_p,4)

# 传入并返回数组指针类型
def test05():
    ll = cdll.LoadLibrary   
    lib = ll("./pytest.so")
    lib.getArr.restype  = POINTER(c_int) #设置返回值类型为 int*
    a = lib.getArr()
    for i in range(0,4):
        print(a[i])


if __name__ == '__main__':
    test04()







