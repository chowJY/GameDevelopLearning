#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from Tkinter import *
import os


path = os.getcwd()
disk = path.split('\\')[0]
root = Tk()         
root.geometry('500x500')   

f = Frame(root)
f.pack(side = "bottom")
Label(f, text = "commit").pack(side = "left")
text = Text(f,width=44, height=4, font=('conslon', 14), foreground='black')
text.pack()
fileList = os.listdir(path)
listB  = Listbox(root, selectmode = MULTIPLE)          
for item in fileList:                 # 第一个小部件插入数据
    listB.insert(0,item)
fileList.reverse()
listB.pack()  
                  # 将小部件放置到主窗口中
import ctypes 
def Call_Entry():
	commitment = text.get(1.0, END)
	commitment = commitment.split('\n')[0]
	selectList = []
	for i in listB.curselection():
		selectList.append(fileList[i])
	if len(selectList) <= 0:
		ctypes.windll.user32.MessageBoxW(0, u'至少选择一个文件', u'提示', 0)
		# root.tk.messagebox.showinfo('Alert','请输入评论')
		return
	# if len(commitment) <= 1:
	# 	ctypes.windll.user32.MessageBoxW(0, u'需要提交更新日志', u'提示', 0)
	print selectList
	uploadString = ''
	for fileName in selectList:
		uploadString += '\"'
		uploadString += fileName
		uploadString += '\"'
		uploadString += ' '
	print uploadString
	changePath = "{disk}\ncd {path}\n".format(disk = disk, path = path)
	os.system(changePath)
	commandLine = "git add {uploadfile}\n".format(uploadfile = uploadString)
	os.system(commandLine)
	commandLine = "git commit -m\"{commitment}\"".format(commitment = commitment)
	os.system(commandLine)
	commandLine = "git push origin master"
	os.system(commandLine)
uploadBtn = Button(root,text='Upload', command=Call_Entry, width=10)
uploadBtn.pack()
root.mainloop()                 # 进入消息循环