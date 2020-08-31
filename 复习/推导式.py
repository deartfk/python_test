# 列表推倒式; 最终给你的是列表
# 语法 [最终结果(变量) for 变量 in 可迭代对象]
lis = [1,3,5,66,44,777]
lst1 = [a for a in lis if a > 66]
print(lst1)

# 字典推倒式; 最终给你的是字典
lst1 = ["name", "age", "shengao", "xingbie"]
lst2 = ['ss', 19, 20, "男"]

dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
print(dic)

dic2 ={'name': 'ss', 'age': 19, 'shengao': 20, 'xingbie': '男'}
dic3 = {dic2[k]:k for k in dic2}
print(dic3)

# 集合推导式
lst = ["马化腾", "马化腾", "王建忠", "张建忠", "张建忠", "张雪峰", "张雪峰"]

s = {i for i in lst}
print(s)

# 内置函数sorted
lst = ["大阳哥a", "尼古拉斯aa", "赵四aaa", "刘能a", "广坤aaaaaa", "谢大脚a"]

lst3 = sorted(lst,key=lambda s:s.count('a'))   # 内置函数. 返回给你一个新列表  新列表是被排序的
print(lst3)