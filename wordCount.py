
excludes = {"the","and","of","you","a","i","my","in"}#设定无效词
def getText():
    txt = open("D:/DLR/code/PYTHON/6-行文代码codes/hamlet.txt", "r").read()
    txt = open(input("请输入文章(txt)路径(例D:/hamlet.txt)："), "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt
