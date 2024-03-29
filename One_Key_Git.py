#!/usr/bin/python
# -*- coding: UTF-8 -*-


################使用说明#####################
# 将该文件放在已经与仓库建立好连接的文件夹下   #
# 运行后选中所需要上传的文件。                #
# 一定要写提交说明                          #
# 点击Upload 即可上传                      #
##########################################
from Tkinter import *
import os
import ctypes

path = ''
disk = ''

class InvalidOperation(Exception):
	def __init__(self, message):
		ctypes.windll.user32.MessageBoxW(0, message, u'提示', 0)

class GitGUI(object):
	def __init__(self,root, fileList):
		self.root = root
		self.fileList = fileList

	def initialGUI(self):    
		self.root.geometry('500x500')

		self.top = Frame(self.root, height = 50, width = 400)
		self.top.pack(anchor = 'n', fill = 'x')

		self.middle = Frame(self.root, height = 20, width = 400)
		self.middle.pack(anchor = 'center', pady = 10)

		self.bottom = Frame(self.root, height = 250, width = 400)
		self.bottom.pack(anchor = 'center', pady = 30, fill = 'x')
		
		Label(self.bottom, text = "commit").pack(side = "left", padx = 10)
		
		self.text = Text(self.bottom, width=40, height=4, font=('conslon', 14), foreground='black')
		self.text.pack(side = 'left', fill = 'x', expand = True)

		self.listB  = Listbox(self.top, selectmode = MULTIPLE)
		self.ShowFileList(self.fileList)

		self.uploadBtn = Button(self.middle,text='Upload', command=self.UpLoad, width=10)
		self.uploadBtn.pack(side = 'left', padx = 5)

		self.uploadAllBtn = Button(self.middle,text='UploadAll', command=self.UpLoadAll, width=10)
		self.uploadAllBtn.pack(side = 'left', padx = 5)

		self.deleteBtn = Button(self.middle,text='Delete', command=self.Delete, width=10)
		self.deleteBtn.pack(side = 'left', padx = 5)

	def ShowFileList(self, fileList):
		for item in fileList:
			self.listB.insert(0,item)
		self.listB.pack(expand = True, fill = 'both')
		fileList.reverse()

	
	def UpLoad(self):
		uploadString = ''
		commitment = ''
		
		try:
			uploadString, commitment = self.GetUpdateInof()
		except InvalidOperation as e:
			return

		self.GitAdd(uploadString)

		self.GitCommit(commitment)
		
		self.GitPush()

	def Delete(self):
		uploadString = ''
		commitment = ''
		
		try:
			uploadString, commitment = self.GetUpdateInof()
		except InvalidOperation as e:
			return
		for i in self.listB.curselection():
			self.listB.delete(i)
		self.GitRemove(uploadString)

		self.GitCommit(commitment)
		
		self.GitPush()

	def UpLoadAll(self):

		self.GitAdd('. *')

		self.GitCommit("update All file")
		
		self.GitPush()

	def GetCommitment(self):
		return self.text.get(1.0, END).split('\n')[0]

	def GetSelectFileList(self):
		selectList = []
		for i in self.listB.curselection():
			selectList.append(self.fileList[i])
		return selectList

	def CheckInvaildOperation(self, commitment, selectList):
		message = ""

		if len(selectList) <= 0:
			message = u'至少选择一个文件'

		if len(commitment) <= 1:
			message = u'需要提交更新日志'
		
		if message != "":
			raise InvalidOperation(message)

	def SetUpLoadFileString(self, selectList):
		uploadString = ''
		for fileName in selectList:
			uploadString += '\"{fileName}\" '.format(fileName = fileName)
		return uploadString

	def GetUpdateInof(self):
		uploadString = ''

		self.SetWorkPath()

		commitment = self.GetCommitment()

		selectList = self.GetSelectFileList()

		self.CheckInvaildOperation(commitment, selectList)
		
		uploadString = self.SetUpLoadFileString(selectList)

		return uploadString, commitment

	def SetWorkPath(self):				
		disk = path.split('\\')[0]
		changePath = "{disk}\ncd {path}\n".format(disk = disk, path = path)
		os.system(changePath)

	def GitAdd(self, uploadString):
		commandLine = "git add {uploadfile}\n".format(uploadfile = uploadString)
		os.system(commandLine)

	def GitCommit(self, commitment):
		commandLine = "git commit -m\"{commitment}\"".format(commitment = commitment)
		os.system(commandLine)

	def GitRemove(self, uploadString):
		commandLine = "git rm -r {uploadfile}\n".format(uploadfile = uploadString)
		os.system(commandLine)

	def GitPush(self):
		commandLine = "git push origin master"
		os.system(commandLine)

def GetPathFileList():
	fileList = []
	for root, dirs, files in os.walk(".", topdown=True):
		if '.\\.git' in root:
			continue
		for file in files:
			fileList.append(os.path.join(root,file))

	return fileList
import copy
def main():

	fList = GetPathFileList()

	gitGUI = GitGUI(Tk(), copy.copy(fList))
	gitGUI.initialGUI()
	
	gitGUI.root.mainloop()

if __name__ == '__main__':
	main()