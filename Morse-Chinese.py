#!/usr/bin/python
# encoding:utf-8
import requests, json, urllib, os
# 电码转中文
#读取电码文件
file_obj = open("Morse.txt")			
all_lines = file_obj.readlines()
code=""
for line in all_lines:
	number=""
#这里切片有个问题，按照空格切片，不知道为什么会把最后一个忽略掉，没办法操作，只能显示，这里的解决方法是在最后再加一个空格，其实每行刚开始也有个空格
	for c in line.split(" "):
		if c=="-----":
			number=number+"0"
		elif c==".----":
			number=number+"1"
		elif c=="..---":
			number=number+"2"
		elif c=="...--":
			number=number+"3"
		elif c=="....-":
			number=number+"4"
		elif c==".....":
			number=number+"5"
		elif c=="-....":
			number=number+"6"
		elif c=="--...":
			number=number+"7"
		elif c=="---..":
			number=number+"8"
		elif c=="----.":
			number=number+"9"
		else:
			continue
	code=code+number+","	
code=code.strip(',')
print(code)
#编写请求
data = {}
data["appkey"] = "83f4921688d2a368"
# 用,分割
data["code"] = code  
url_values = urllib.parse.urlencode(data) 
url = "https://api.jisuapi.com/chinesecode/chinese" + "?" + url_values
#发送请求
request=urllib.request.Request(url)#把url构造成一个request对象
result=urllib.request.urlopen(request)#再把request对象传给urlopen
#写入中文
#判断文件是否存在，存在删除
if os.path.exists("Chinese.txt"):
	os.remove("Chinese.txt")
#新建摩斯电码文件
file_write_obj = open("Chinese.txt", 'w')
#分析json文件
jsonarr = json.loads(result.read().decode('utf-8'))
if jsonarr["status"] != u"0":
	print (jsonarr["msg"])
	#exit()
result = jsonarr["result"]
for val in result:
	print (val["code"], val["character"])
	file_write_obj.writelines(val["character"])