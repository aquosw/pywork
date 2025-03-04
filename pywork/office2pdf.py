from win32com.client import Dispatch
from os import walk
import sys


def doc2pdf(input_file):
    # word = DispatchEx('Word.Application')  # 启动独立进程
    output_file = input_file.split(".")
    try:
        doc = word.Documents.Open(input_file)
        doc.SaveAs(output_file[0] + ".pdf", FileFormat=17) # Word另存为PDF为17
        doc.Close(SaveChanges=False)
    except:
        print("Unexpected error:", sys.exc_info())


def ppt2pdf(input_file):
    output_file = input_file.split(".")
    try:
        ppt = powerpoint.Presentations.Open(input_file)
        ppt.SaveAs(output_file[0] + ".pdf", FileFormat=32) # PPT另存为PDF为32
        ppt.Close(SaveChanges=False)
    except:
        print("Unexpected error:", sys.exc_info())
    

def xls2pdf(input_file):
    output_file = input_file.split(".")
    try:
        xls = excel.Workbooks.Open(input_file)
        xls.SaveAs(output_file[0] + ".pdf", FileFormat=57) # Excel另存为PDF为57
        xls.Close(SaveChanges=False)
    except:
        print("Unexpected error:", sys.exc_info())
    

if __name__ == "__main__":
    directory = input("输入路径，会遍历文件夹及子文件夹。文件不要带两个以上的.点：")
    word = Dispatch('Word.Application') # WPS改为Kwps.Application
    powerpoint = Dispatch('Powerpoint.Application') # WPS改为Kwpp.Application
    excel = Dispatch('Excel.Application') # WPS改为Ket.Application
    doc_files = []
    # 对directory目录里的所有文件进行遍历
    for root, dirs, filenames in walk(directory):
        for file in filenames:
            # 忽略~$开头的临时文件，并根据后缀名判断文件类型
            if file.find("~$") == -1:
                if file.endswith(".doc") or file.endswith(".docx") or file.endswith(".DOC"):
                    doc2pdf(str(root + "\\" + file))
                elif file.endswith(".ppt") or file.endswith(".pptx") or file.endswith(".PPT"):
                    ppt2pdf(str(root + "\\" + file))
                elif file.endswith(".xls") or file.endswith(".xlsx") or file.endswith(".XLS"):
                    xls2pdf(str(root + "\\" + file))
                    
    word.Quit() # 挪过来主过程，避免频繁调用导致rpc失败
    powerpoint.Quit()
    excel.Quit()
