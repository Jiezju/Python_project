# 模拟一个简单的进销存软件，要用到装饰器（需要考虑哪些功能适合使用装饰器）：

# 1.操作之前需要通过*账户密码*验证是否登陆成功

# 2.每次登陆需要将登陆的用户名、登陆时间写入*日志*（日志用某个数据类型记录即可）

# 3.登陆成功后可以增加商品名称以及对应的库存，增加商品时，需要判断你的商品不能是*违禁商品*（自定义违禁商品）

# 4.当有商品入库或销售出去的时候，需要改变对应*库存*

# 5.可以查询某商品现有库存（注意这里的数据结构）

# 基本功能函数
import time
from functools import wraps

# 定义一个全局变量，控制登陆状态 bool
login_status = False

# 日志list
log = []

# 定义违禁物品
prohibit_list = ['枪支','弹药','药品','野生动物']

# 定义一个全局变量保存管理员用户名和密码
super_adm = {'user':'peipei','pwd':'123456'}

# 定义一个全局变量保存添加的商品
product = {}

# 定义装饰器函数来增强函数
# 登陆功能 *装饰器*
def login(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        global login_status, super_adm

        if login_status == True:
            return func(*args, **kwargs)
        else:
            login_user = input('Please input name!')
            input_paswd = input('Please input pass word!')
            if login_user == super_adm['user'] and input_paswd == super_adm['pwd']:
                login_status = True
                return func(*args, **kwargs)
            else:
                print('Login fail!')

    return wrapper_func

# 装饰器 登录日志记录
def log_write(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        global log,super_adm
        log_dic={} #建立一个临时字典 存储用户操作行为和信息
        log_dic['用户名'] = super_adm['user']
        log_dic['登陆时间'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        log_dic['操作类型'] = wrapper_func.__name__
        log_dic['操作内容'] = args
        log.append(log_dic) #向全局log添加这个临时字典 log_dic
        return func(*args, **kwargs)
    return wrapper_func

# 装饰器 判断是否有违禁物品 *装饰器*
def is_prohibit(func):
    @wraps(func)
    def wrapper_func(product_name, product_stock_num): # 传递具体参数
        global prohibit_list
        if product_name in prohibit_list:
            print('{} is prohibit'.format(product_name))
        else:
            return func(product_name, product_stock_num)
    
    return wrapper_func


# 增加商品入库
@log_write
@is_prohibit
def add_product_stock(product_name, product_stock_num):
    global product
    if product_name in product:
        product[product_name] += product_stock_num
    else:
        product[product_name] = product_stock_num

@log_write
def sale_product(product_name, product_sale_num):
    global product
    if product_name not in product:
        print('Product not in product!')
    elif product_sale_num > product[product_name]:
        print('Not enough product!')
    else:
        product[product_name] -= product_sale_num

@log_write
def query_product(product_name):
    global product
    if product_name not in product:
        print('{} not in product !'.format(product_name))
    else:
        print('{} stock num is {}'.format(product_name, product[product_name]))


@login
def main():
     #函数调用的新玩儿法，因为python没有switch case语句 即多选。所以我们用字典搞定
    functions = {
        '1':add_product_stock,
        '2':sale_product,
        '3':query_product,
    }
    func_choice = input('请输入功能编号---:')
    
    if func_choice == '1':
        #注意这里的调用关系，func.get(key)获得了值，但是这个值是一个对象，是一个函数那么再加（）就执行了该函数
        product_name = input('请输入入库产品名称:')
        stock_num = int(input('请输入入库产品数量:'))
        functions.get(func_choice)(product_name,stock_num)
    
    elif func_choice == '2':
        product_name = input('请输入销售产品名称:')
        product_sale_num = int(input('请输入销售产品数量:'))
        functions.get(func_choice)(product_name,product_sale_num)
        
    elif func_choice == '3':
        product_name = input('请输入查询产品名称:')
        functions.get(func_choice)(product_name)


if  __name__ == '__main__':
    print("****欢迎来到万门大学Python趣讲精练 ERP 演示系统****")
    print("****请输入功能编号进行操作****")
    print('输入1 进行商品添加入库操作','输入2 销售减库操作','输入3 库存查询操作',sep='\n')
    main()
    print(log)