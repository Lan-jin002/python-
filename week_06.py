names = ["dad","bluejin","mom"]
id = [1001,1002,1003]

# 增加
## .append()  ---在末尾增加
names.append("grandpa")
print(names)

## .insert() ---在指定位置增加
names.insert(3,"grandma")
print(names)

# 删除
##.pop() ---指定位置删除
names.pop(3)
print(names)

## .remove() ---要判断存不存在，然后再删除
# names.remove("name")
# print(names)

# .index() ---查询所在位置
a = id.index(1003)
print(a)

# .clear() ---清除
# id.clear()
# print(id)

# .count() ---查询次数
print(names.count("bluejin"))

# len() ---查看list长度
print(len(names))

# .extend() ---扩充
names.extend(id)
print(names)

# 枚举法
stu_id = [1001, 1002, 1003, 1001,1004,1001]

# 目的：取出所有位置1001的index
for i in stu_id:
    # 循环遍历stu_id的所有内容
    if i == 1001:
        # 判断如果元素为1001的时候,怎么取出索引值？
        print()
# 枚举:因为list其实不仅有values值，还有index索引，但for循环主要循环遍历其值，不遍历索引
# 因此，有了枚举的方法，同时遍历两者
# enumerate()
pop_values_list = []  # append方法经常用于新建列表
for index,item in enumerate(stu_id):
    print(index,item)
    pop_values_list.append(index)
    print(pop_values_list)

# .copy() ---复制
id_matedata = id.copy()
id.pop(1)
print("id:",id,'\n','id_matedata:',id_matedata)
