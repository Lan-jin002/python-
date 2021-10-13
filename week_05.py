# Author:bluejin
# time:week_05
# 列表

# 列表是有顺序的，所以可以按照indexed的方式去取值
user_data=["zhichao","jack","alex","marry"]

# 1.从左向右取值
print(user_data[2])

# 切片 slice,右边的值取不到 例如[0：3] 索引为3的值取不到
print(user_data[0:3])

# 当从0开始取值时，0可以忽略不写
print(user_data[:3])

#  从右往左取值（index & slice）
print(user_data[-2])
# 切片 slice，右边的值取不到，例如[-3：-1]，索引为-1的值取不到
print(user_data[-3:-1])

#指定slice切片的步长step
num_list = list(range(20))
print(num_list)
print(num_list[0:15:2])


#用户输入
name = input("name: ")
age = input("age: ")
job = input("job: ")
salary = input("salary: ")

#info    字符串的拼接 用 “+” 符号来连接
info = '''-------INFO''' +name+ '''--------
name:'''+name+'''
age:'''+age+'''
job:'''+job+'''
salary:'''+salary

print(info)

#info_占位符
info_占位符 = '''-------INFO %s--------
name:%s
age:%s
job:%s
salary:%s''' % (name, name, age, job, salary)

print(info_占位符)

# .format()
info_format = '''------INFO {姓名}------
name:{姓名}
age:{年龄}
job:{工作}
salary:{薪水}'''.format(年龄=age,姓名=name,工作=job,薪水=salary)

print(info_format)

# 获取官网的链接
url = "https://www.nfu.edu.cn"
高教动态 = "gjdt"
url_页面 = ".htm"
url_页面细节不变 ="/index"
for i in range(1,27):
    url = "https://www.nfu.edu.cn/{新闻}/index{页码}.htm".format(页码=str(i),新闻="ztb")
    print(url)


