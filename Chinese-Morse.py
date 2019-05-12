#!/usr/bin/python 
# encoding:utf-8 
import requests, json, urllib, os
# 中文转电码
#读取中文文件
file_obj = open("Chinese.txt")				
all_lines = file_obj.readlines()
chinese=""
for line in all_lines:
	chinese=chinese+line
file_obj.close()
#编写请求
data = {} 
data["appkey"] = "83f4921688d2a368" 
data["chinese"] = chinese 
url_values = urllib.parse.urlencode(data) 
url = "http://api.jisuapi.com/chinesecode/code" + "?" + url_values 
#发送请求
request=urllib.request.Request(url)#把url构造成一个request对象
result=urllib.request.urlopen(request)#再把request对象传给urlopen
#写入摩斯电码
#判断文件是否存在，存在删除
if os.path.exists("Morse.txt"):
	os.remove("Morse.txt")
#新建摩斯电码文件
file_write_obj = open("Morse.txt", 'w')
#分析json文件
jsonarr = json.loads(result.read().decode('utf-8')) 
if jsonarr["status"] != u"0": 
	print (jsonarr["msg"]) 
	#exit() 
	result = jsonarr["result"] 
#转摩斯电码
	for val in result: 
		#print (val["code"], val["character"])
		out=""
		for v in val["code"]:
			if v=="0":
				out=out+" -----"
			elif v=="1":
				out=out+" .----"
			elif v=="2":
				out=out+" ..---"
			elif v=="3":
				out=out+" ...--"				
			elif v=="4":
				out=out+" ....-"
			elif v=="5":
				out=out+" ....."
			elif v=="6":
				out=out+" -...."
			elif v=="7":
				out=out+" --..."
			elif v=="8":
				out=out+" ---.."
			elif v=="9":
				out=out+" ----."
			else :	
				continue
		out=out+" "
		print(out)
		file_write_obj.writelines(out)
		file_write_obj.write('\n')
file_write_obj.close()