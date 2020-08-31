# 列表是可以改变的
# 语法
# lis = [元素1,元素2,元素3]    元素可以是任意数据类型
lst = ['lala', 'ojoj', 123, '派森', '派森']
# 每个元素都有索引，可以根据索引范文列表的值
lst[0]  # 值是'lala'

# 列表元素的修改
lst[1] = 'hehehe'

# 列表元素的删除
del lst[2]
print(lst)
# 移除lala这个元素
lst.remove('lala')
# 清空列表元素
lst.clear()
print(lst)

# 列表的迭代
for i in lst:
    print(i)

# 列表的方法

# 在列表最后添加一个元素a
lst.append('a')

# 在列表中2这个位置插入一个元素，其他元素索引依次后移,如果没有索引2，则插入到列表最后
lst.insert(2, '尼玛')
print(lst)

# 返回'派森'元素在列表中的个数
print(lst.count('派森'))

# 返回索引0~3之间lala的位置
print(lst.index('lala', 0, 3))

# 给列表内元素排序,如果参数有reverse=True就是倒序
lst_sort = [5, 6, 4, 2, 8, 34, 87, 1, 2, 3, ]
lst_sort.sort(reverse=True)
print(lst_sort)

# 删除第0个元素，默认值为-1（最后一个元素）
lst.pop(0)

# 拷贝一个列表，返回一个新列表
lst2 = lst.copy()
print(lst)
print(lst2)

# 反向列表中元素
lst.reverse()
print(lst)

# 在lst列表末尾追加lst3列表的值
lst3 = [2, 3, 54, 6]
lst.extend(lst3)
print(lst)

