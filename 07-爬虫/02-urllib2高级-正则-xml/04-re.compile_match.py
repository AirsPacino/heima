# coding:utf-8
import re

pattern = re.compile("\w+@\w+")

result = pattern.match("airs_pacino@www.com")
print(result.group())