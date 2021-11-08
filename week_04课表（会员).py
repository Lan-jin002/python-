# 1.判断是不是会员账号
# 2.账号密码是否都正确
# 3.输入时间，输出对应时期的课程
# 4.非会员用户询问是否开通会员


VIP_user_data = ["bluejin"]
VIP_password_data = ['10086']
user_data = ["jinblue"]
password_data = ["68001"]
username = input("请输入用户名")
password = input("请输入密码")
Pass_count = 3  # 账号密码输入次数
while True:
    Pass_count -= 1
    if Pass_count == 0:
        break

    # 判断是否会员
    if username in VIP_user_data:
        if password in VIP_password_data:
            # 会员密码正确
            print("欢迎您登录使用查询系统，您有10次查询机会")

            count = 11
            while True:
                count -= 1
                if count == 0:
                    print("查的次数太多啦")
                    break
                else:
                    print("你还有", count, "次查询机会")

                    week_time = int(input("想要查周几的课呀"))
                    import datetime

                    time = datetime.datetime.today().weekday()

                    if week_time == 1:
                        print("6-7 写作训练周秀梅 @1-401")
                        print("8-9 创越基础（实践）高进 @1-401")
                    elif week_time == 2:
                        print("8-9 H5互动技术与应用 游鸽@3实308")
                        print("10-11 大学英语（三）B1 洪明@9-202")
                    elif week_time == 3:
                        print("今天没有课！！！")
                    elif week_time == 4:
                        print("1-2 大学英语（三）B1 洪明@9-204")
                        print("3-5 Python语言 许智超@新综合楼612")
                        print("8-9 广告文案写作 罗希@1-303")
                        print("10-11 武术 巩森森 @西区体育馆西面")
                        print("12-14 毛泽东思想和中国特色社会主义理论体系概论  张锦标@9-201")

                    elif week_time == 5:
                        print("1-2 Illustrator软件应用 阚风霞@新综合楼612")
                        print("4-5 毛泽东思想和中国特色社会主义理论体系概论（实践）杨益孜@7-402")

                    elif week_time == 6:
                        print("周末happy")

                    elif week_time == 7:
                        print("周末happy")
                    else:
                        print("没有这一天哈")

        # 会员密码错误
        else:
            if Pass_count == 0:
                print("你没机会了！")
                break

            else:
                print("密码不对噢！您还有", Pass_count, "次机会，好好珍惜哟")
                username = input("请输入用户名")
                password = input("请输入密码")

    #非会员账号正确
    elif username in user_data:
        if password in password_data:
        # 非会员的账号密码都对了
            print("欢迎您登录使用查询系统，您有5次查询机会")
            count = 6
            while True:
                count -= 1
                if count == 0:

                    print("机会用完了，想查更多次嘛，开通会员可以增加五次哟~")
                    #选择是否开通会员
                    q=int(input("你要开会员吗？1=yes 2=no"))
                    #开通会员
                    if q == 1 :
                        print("您已开通会员，获得额外五次查询机会")
                        count = 6
                        while True:
                            count -= 1
                            if count == 0:
                                print("查的次数太多啦")
                                break
                            else:
                                print("你还有", count, "次查询机会")

                                week_time = int(input("想要查周几的课呀"))
                                import datetime

                                time = datetime.datetime.today().weekday()

                                if week_time == 1:
                                    print("6-7 写作训练周秀梅 @1-401")
                                    print("8-9 创越基础（实践）高进 @1-401")
                                elif week_time == 2:
                                    print("8-9 H5互动技术与应用 游鸽@3实308")
                                    print("10-11 大学英语（三）B1 洪明@9-202")
                                elif week_time == 3:
                                    print("今天没有课！！！")
                                elif week_time == 4:
                                    print("1-2 大学英语（三）B1 洪明@9-204")
                                    print("3-5 Python语言 许智超@新综合楼612")
                                    print("8-9 广告文案写作 罗希@1-303")
                                    print("10-11 武术 巩森森 @西区体育馆西面")
                                    print("12-14 毛泽东思想和中国特色社会主义理论体系概论  张锦标@9-201")

                                elif week_time == 5:
                                    print("1-2 Illustrator软件应用 阚风霞@新综合楼612")
                                    print("4-5 毛泽东思想和中国特色社会主义理论体系概论（实践）杨益孜@7-402")

                                elif week_time == 6:
                                    print("周末happy")

                                elif week_time == 7:
                                    print("周末happy")
                                else:
                                    print("没有这一天哈")

                        break
                    #不开通会员
                    elif q==2:
                        print("感谢您的使用")
                    #输入错误直接退出
                    else:
                        print("输入错误")
                    break

                else:
                    print("你还有", count, "次查询机会")

                    week_time = int(input("想要查周几的课呀"))

                    import datetime

                    time = datetime.datetime.today().weekday()
                    if week_time == 1:
                        print("6-7 写作训练周秀梅 @1-401")
                        print("8-9 创越基础（实践）高进 @1-401")
                    elif week_time == 2:
                        print("8-9 H5互动技术与应用 游鸽@3实308")
                        print("10-11 大学英语（三）B1 洪明@9-202")
                    elif week_time == 3:
                        print("今天没有课！！！")
                    elif week_time == 4:
                        print("1-2 大学英语（三）B1 洪明@9-204")
                        print("3-5 Python语言 许智超@新综合楼612")
                        print("8-9 广告文案写作 罗希@1-303")
                        print("10-11 武术 巩森森 @西区体育馆西面")
                        print("12-14 毛泽东思想和中国特色社会主义理论体系概论  张锦标@9-201")

                    elif week_time == 5:
                        print("1-2 Illustrator软件应用 阚风霞@新综合楼612")
                        print("4-5 毛泽东思想和中国特色社会主义理论体系概论（实践）杨益孜@7-402")
                    elif week_time == 6:
                        print("周末happy")
                    elif week_time == 7:
                        print("周末happy")
                    else:
                        print("没有这一天哈")
            break
        else:
            # 非会员密码错误
            if Pass_count == 0:
                print("你没机会了！")
                break
            else:
                print("密码不对噢！您还有", Pass_count, "次机会，好好珍惜哟")
                username = input("请输入用户名")
                password = input("请输入密码")
#账号输入错误
    else:
        print("账号不对哟")
        break
