import os
import win32com.client

destdir = ''

def list_pdfs_in_directory(directory):
    """列出指定目录下的所有PDF文件"""
    pdf_files = []
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            pdf_files.append(os.path.join(directory, filename))
    return pdf_files

def merge_pdfs(pdf_files, current_directory):
    """使用win32com调用Adobe Acrobat合并PDF文件"""
    global destdir
    pages = 0
    try:
        # 创建Adobe Acrobat的COM对象
        acrobat = win32com.client.Dispatch("AcroExch.App")
        # 可见性设置为False，以便在后台运行
        # acrobat.Visible = False

        # 打开一个新的AvDoc对象（代表一个PDF文档）
        avdoc = win32com.client.Dispatch("AcroExch.PDDoc")
        temp_avdoc = win32com.client.Dispatch("AcroExch.PDDoc")
        # 创建一个新的PDF文档
        avdoc.Create()
        
        for pdf_file in pdf_files:
            temp_avdoc.Open(pdf_file)
            avdoc.InsertPages(avdoc.GetNumPages()-1, temp_avdoc, 0, temp_avdoc.GetNumPages(), 1) # 本文件页数，他文件，他文件起始页码-1，复制页数，1
            pages = avdoc.GetNumPages() # 放在后面记录，数据会准
            print(avdoc.GetNumPages())
            # 关闭临时文档，不保存更改
            temp_avdoc.Close()
            
        destdir = os.path.join(current_directory, r"merge-" + str(pages) + r".pdf")

        avdoc.save(1, destdir)  # 1 表示完整保存 文件名移到这里是为了记录页码
        avdoc.Close()

        # 退出Adobe Acrobat应用程序
        acrobat.Exit()
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":        
    while 1:
        # 获取当前目录
        current_directory = str(input("请输入pdf所在文件夹："))#os.getcwd()

        # 列出当前目录下的所有PDF文件
        pdf_files = list_pdfs_in_directory(current_directory)

        # 指定输出文件

        # 合并PDF文件
        merge_pdfs(pdf_files, current_directory)



        print(f"PDF文件已合并到：{destdir}")
