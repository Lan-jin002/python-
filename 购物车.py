# 要求：1、运行程序后，让用户输入支付宝余额，然后打印我们的商品列表给用户。
# 　　  2、让用户输入商品编号进行商品的购买。
# 　　  3、用户选择商品后，检查用户的余额是否够，若够则直接扣款，不够则提醒用户。
# 　　  4、用户可以随时退出购买，推出时打印用户已购买的商品和支付宝余额。

# 商品列表

goods_list = [
    # 商品1 商品名称，商品价格，商品编号...
    # 商品模板 ： [商品名称，商品名称]
    ["煎饼mini",1],
    ["煎饼",10],
    ["煎饼Plus",100],
    ["煎饼Max",1000],
    ["煎饼Pro",10000],
]

user_shopping_cart = []#append 新增

# 用户输入 ： input
Alipay = int(input("请输入您的余额："))

# 打印商品列表 （规范打印，样式是先写的，然后再输入数据）
# 先涉及模板样式： 商品编号：%s，商品名称：%s，商品价格：%d

while True:
    print("------商品列表-------")
    for i in range(len(goods_list)):
        print("商品编号：%s，商品名称：%s，商品价格：%d 元"%(i,goods_list[i][0],goods_list[i][1]))

    # 2.让用户输入商品编号进行商品的购买。
    choice = input("请输入正确的商品编号(输入q退出购买)：") # 输入的可能不是数值

    # 是正确的编号
    if choice.isdigit():
        # 用int转换
        choice = int(choice)
        if choice < len(goods_list):
        # 商品的信息： goods_list[choice]，商品名称：goods_list[choice][0],商品价格：goods_list[choice][1]
            # 1.看看用户钱够不够：
            if Alipay < goods_list[choice][1]:
                print("您的余额不够")
                break
            # 2.钱够，扣钱，加到购物车
            else:
                Alipay = Alipay - goods_list[choice][1]
                user_shopping_cart.append(goods_list[choice])
                # 提示购买成功
            print("【%s】已经添加到您的购物车，您的余额还有【%d】 元"%(goods_list[choice][0],Alipay))
        # 不是正确的编号
        else :
            print("您输入的商品不存在，请输入正确的编号")
    elif choice == "q":
        print("您的购物车： %s" %(user_shopping_cart),'\n',"您的余额还有：%d 元"%(Alipay))
        break
        # 两种情况
        # 1.按照我们的要求输入的文本，例如：输入q表示quit退出的意思

        # 2. 输入的不符合要求
    else:
        print("请输入正确的商品编号，或者输入“q”退出")
        pass