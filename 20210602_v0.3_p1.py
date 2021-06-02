import redis
import sys
from wordcount import getText
#pool=redis.ConnectionPool(host="124.71.227.41",port=6379)
r = redis.Redis(host='127.0.0.1', port=6379)
#r = redis.Redis(connection_pool=pool)
print(r.flushdb())

excludes = {"the","and","of","you","a","i","my","in","is"}#设定无效词
def dealText():
    name_search='2'
    hamletTxt = getText()
    words  = hamletTxt.split()
    counts = {}
    for word in words:			
        counts[word] = counts.get(word,0) + 1
    for word in excludes:#不统计无效词
        del(counts[word])    
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True) 
    dict_tag=dict(items)

    name_in=input("请输入存储名称：")
    r.hmset(name_in, dict_tag)
    while name_search!='0':
        name_search=input("请输入所要查询的存储空间名称：")
        if name_search!='0':
            search_tar=input("请输入所查询的关键词：")
        print(r.hget(name_search,search_tar))
    
    ret=input("是否继续进行录入？（y/n）")
    if ret=='y':
        return dealText()
    else:
        print("thanks for using")
    sys.exit()
    
dealText()

