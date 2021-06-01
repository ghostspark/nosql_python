import redis
import sys
#pool=redis.ConnectionPool(host="124.71.227.41",port=6379)
r = redis.Redis(host='127.0.0.1', port=6379)
#r = redis.Redis(connection_pool=pool)
print(r.flushdb())

i='2'
j='2'
excludes = {"the","and","of","you","a","i","my","in"}#设定无效词
def getText():
    #txt = open("D:/DLR/code/PYTHON/6-行文代码codes/hamlet.txt", "r").read()
    txt = open(input("请输入文章(txt)路径(例D:/hamlet.txt)："), "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
hamletTxt = getText()
words  = hamletTxt.split()
counts = {}
for word in words:			
    counts[word] = counts.get(word,0) + 1
for word in excludes:#不统计无效词
    del(counts[word])    
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
#for i in range(10):
    #word, count = items[i]
    #print ("{0:<10}{1:>5}".format(word, count))
dict_tag=dict(items)

name_in=input("请输入存储名称：")
i=name_in
r.hmset(name_in, dict_tag)
while j!='0':
    name_search=input("请输入所要查询的存储空间名称：")
    j=name_search
    print(r.hget(name_search,"hamlet"))

