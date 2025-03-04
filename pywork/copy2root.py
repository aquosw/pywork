import os
import shutil
# 将一个文件夹中的所有文件（包括子文件夹），拷贝到另一个文件夹中，去除子文件夹。
def copy_to_root(srcpath, dstpath):
    try:
        # 遍历源文件夹，得到根目录，子目录和文件名列表
        for root, dirs, files in os.walk(srcpath, topdown=True):
            counter = 0
            #获取文件名依次遍历
            for name in files:
                # 如果该文件在目标目录中已经存在，也就是重复文件，则给文件重命名，否则无法拷贝。
                if os.path.exists(dstpath + '\\' + name):
                    counter += 1
                    # 获取文件名
                    filename = name[0: name.rindex('.')]
                    # 获取文件类型（后缀）
                    filetype = name[name.rindex('.') + 1: ]
                    # 将文件名重命名后，拷贝到目标文件夹，注意，copy的两个参数都要是绝对路径的完整文件名
                    shutil.copy(os.path.join(root, name), dstpath + '\\' + filename + str(counter) + '.' + filetype)
                else:
                    # 如果该文件未重复，那就直接拷贝就好。
                    shutil.copy(os.path.join(root, name), dstpath + '\\' + name)
                    
    except Exception as e:
        print(f"发生错误：{e}")


if __name__ == "__main__":
    srcpath = input("请输入文件所在的文件夹：")
    here = input("要在此文件夹平展吗？(y/n)")
    dstpath = srcpath if here == 'y' or here == 'Y' else input("请输入平展文件的文件夹：")
    copy_to_root(srcpath, dstpath)