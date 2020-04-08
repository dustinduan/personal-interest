import os
import shutil

def file_classify():
    formats={"音频":['.mp3','.wav'],
        "视频":['.mp4','.avi','.mov'],
        "图片":['.jpeg','.jpg','.png','.gif'],
        "文档":['.txt','.pdf','.doc','.docx'],
        "源程序":['.c','.cpp','.py'],
        "可执行文件":['.exe','.msi'],
        "压缩档":['.zip','.rar']}
    pp=input('请输入需要整理的文件路径')
    os.chdir(r"{0}".format(pp))
    for f in os.listdir():
        ext=os.path.splitext(f)[-1].lower()
        for d,exts in formats.items():
            if not os.path.isdir(d):
                os.mkdir(d)
            if ext in exts:
                shutil.move(f,'{0}/{1}'.format(d,f))
    print('整理完成!')

file_classify()
