import os
import sys

def batch_prefix(folder_name, prefix):
    file_names = os.listdir(folder_name)   #获取文件夹内所有文件的名字
    try:
        for name in file_names:    #如果某个文件名在file_names内
            old_name = folder_name + '/' + name   #获取旧文件的名字，注意名字要带路径名
            new_name = folder_name + '/' + prefix + name  
            os.rename(old_name, new_name)  #用rename()函数重命名
            print(new_name)  #打印新的文件名字
            
    except Exception as e:
        print(f"发生错误：{e}")


if __name__ == "__main__":
    while 1:
        folder_name = input("请输入加前缀文件的文件夹：")    #获取文件夹的名字，即路径
        prefix = input("请输入想加入的前缀：")
        batch_prefix(folder_name, prefix)
        
