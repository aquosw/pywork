import os,zipfile
from random_name import random_name

def unzip(file):
    zip_obj = zipfile.ZipFile(file)
    dest = file.rstrip(".zip")
    zip_obj.extractall(dest)
    return dest

if __name__ == "__main__":
    while 1:
        folder_name = input("请输入批量解压(zip文件)的文件夹：")
        isrename = input("需不需要重命名？(y/n)")
        isremove = input("需不需要删除源文件？(y/n)")
        fnames = os.listdir(folder_name)   #获取文件夹内所有文件的名字
        files = [os.path.join(folder_name, fname) for fname in fnames]    # 绝对路径
        try:
            for file in files:    #如果某个文件名在file_names内
                if file.endswith(".zip"):
                    dest = unzip(file)
                    print(dest)
                    if isrename == "y" or isrename == "Y":
                        random_name(dest)
                    if isremove == "y" or isremove == "Y":
                        os.remove(file)

        except Exception as e:
            print(f"发生错误：{e}")