import re

patten = "itcast"
string = "itcastha"

result = re.match(patten, string)
print(result.group())


"""match() search() findall() sub("re", "sub", "str") split(r"分隔符|分隔符|分隔符")
贪婪模式：尽可能多匹配。。加上？取消前面模式的贪婪，变为尽可能少的匹配
"""

"""
match()从左到右匹配，search()是在字符串中搜索，只要出现不符合的情况就返回NONE
\d \D
\s \S
\w \W
\b \B 描述边界 "test this line"
.
[]
\number "引用分组num匹配到的字符串"
(?P<name>) 为分组起别名
(?P=name) 引用分组

"""