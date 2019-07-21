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
listB.pack()                    # 将小部件放置到主窗口中

def Call_Entry():
	commitment = text.get(1.0, END)
	commitment = commitment.split('\n')[0]
	selectList = []
	for i in listB.curselection():
		selectList.append(fileList[i])
	if len(selectList) <= 0 or len(commitment) <= 1:
		return
	print selectList
	uploadString = ''
	for fileName in selectList:
		uploadString += '\"'
		uploadString += fileName
		uploadString += '\"'
		uploadString += ' '
	print uploadString
	changePath = "{disk}\ncd {path}\n".format(disk = disk, path = path)
	commandLine = "git add {uploadfile}\ngit commit -m\"{commitment}\"\ngit push origin master\n".format(uploadfile = uploadString, commitment = commitment)
	commandLine = changePath + commandLine
	print commandLine
	os.system(commandLine)

uploadBtn = Button(root,text='Upload', command=Call_Entry, width=10)
uploadBtn.pack()
root.mainloop()                 # 进入消息循环