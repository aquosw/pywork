import os
from os import walk
import uuid



def random_name(directory):
    try:
        for root, dirs, filenames in walk(directory):
            for file in filenames:
                oldname=root + os.sep + file   # os.sep添加系统分隔符
                suffix = os.path.splitext(file)[-1]
                uniq_id = uuid.uuid1()
                newname=root + os.sep +str(uniq_id)+suffix
                os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
                print(file,'======>',newname)            
    except Exception as e:
        print(f"发生错误：{e}")


if __name__ == "__main__":
    while 1:
        directory = input("请输入随机化命名的文件夹：")    #获取文件夹的名字，即路径
        random_name(directory)
        
