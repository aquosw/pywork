import os
import win32com.client

def split_pdf(file, pagesize):
    fdir = os.path.dirname(file)
    acrobat = win32com.client.Dispatch("AcroExch.App")
    avdoc = win32com.client.Dispatch("AcroExch.PDDoc")
    avdoc.Open(file)
    pages = avdoc.GetNumPages()
    count = 0
    while count*pagesize < pages:
        tempdoc = win32com.client.Dispatch("AcroExch.PDDoc")
        tempdoc.Create()
        tempdoc.InsertPages(-1, avdoc, count*pagesize, \
        pagesize if (count+1)*pagesize < pages else pages-count*pagesize , \
        1)# 本文件页数，他文件，他文件起始页码-1，复制页数，1
        print(tempdoc.GetNumPages())
        tempdest = os.path.join(fdir, r'split-' + str(count) + r'.pdf')
        tempdoc.save(1, tempdest)
        tempdoc.Close()
        count += 1
    avdoc.Close()
    acrobat.Exit()

while 1:   
    file = input("输入pdf路径：")
    split_pdf(file, 40)
    print(f"文档已分割好，在文件所属文件夹下")
