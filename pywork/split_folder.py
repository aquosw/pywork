#!/usr/bin/env python
# encoding: utf-8

import os, glob
from shutil import copy


def split_folder(file_path, save_dir, count, prefix, fformat):
        #i是用来计算文件的数量，k是用来计算新建文件夹的数量
        i = 0
        k = 0

        #如果目录不存在，则创建
        if not os.path.isdir(save_dir):
                os.makedirs(save_dir)

        #通过glob.glob来获取原始路径下，所有'.xxx'文件
        imageList = glob.glob(os.path.join(file_path, '*.'+fformat))

        for allImgDir in imageList:
                print(allImgDir)
                #获取文件名称（包括后缀）
                imgDir = os.path.basename(allImgDir)
                print(imgDir)
                #更改jpg文件后缀为ans
                (temp1, temp2) = os.path.splitext(imgDir)
                ansDir = temp1 + '.ans'

                #拼接路径与文件名
                from_imgPath = file_path+'/'+imgDir
                from_ansPath = file_path+'/'+ansDir
                #新建的文件夹
                to_path = save_dir + "\\" + prefix + str(k)

                # 如果 to_path 目录不存在，则创建
                if not os.path.isdir(to_path):
                        os.makedirs(to_path)
                copy(from_imgPath, to_path)
                if os.path.exists(from_ansPath):
                        #将ans文件遍历复制到目标文件夹中
                        copy(from_ansPath, to_path)
                i += 1
                if((i%count) == 0):
                        print('新建一个文件夹')
                        k += 1

if __name__ == '__main__':
        srcpath = input('请输入想要自动分组的文件夹路径：')
        fformat = input('输入参与自动分组的文件格式（如pdf）：')
        here = input("要在此文件夹进行分组吗？(y/n)")
        dstpath = srcpath if here == 'y' or here == 'Y' else input('请输入想保存的根目录：')
        count = int(input('请输入每一组文件的数量：'))
        prefix = input('请输入想保存的目录前缀：')
        #指定找到文件后，另存为的文件夹路径
        save_dir = os.path.abspath(dstpath)
        #指定文件的原始路径
        file_path = os.path.abspath(srcpath)
        split_folder(file_path, save_dir, count, prefix, fformat)