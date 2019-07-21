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

		self.f = Frame(self.root)
		self.f.pack(side = "bottom")
		
		Label(self.f, text = "commit").pack(side = "left")
		
		self.text = Text(self.f,width=44, height=4, font=('conslon', 14), foreground='black')
		self.text.pack()

		self.listB  = Listbox(self.root, selectmode = MULTIPLE)
		self.ShowFileList(self.fileList)

		self.uploadBtn = Button(self.root,text='Upload', command=self.UpLoad, width=10)
		self.uploadBtn.pack()

	def ShowFileList(self, fileList):
		for item in fileList:
			self.listB.insert(0,item)
		self.listB.pack()
		fileList.reverse()

	
	def UpLoad(self):
		uploadString = ''

		self.SetWorkPath()

		commitment = self.GetCommitment()

		selectList = self.GetSelectFileList()

		try:
			self.CheckInvaildOperation(commitment, selectList)
		except InvalidOperation as e:
			return

		uploadString = self.SetUpLoadFileString(selectList)

		self.GitAdd(uploadString)

		self.GitCommit(commitment)
		
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

	def GitPush(self):
		commandLine = "git push origin master"
		os.system(commandLine)

def GetPathFileList():
	path = os.getcwd()
	fileList = os.listdir(path)
	return fileList

def main():

	fList = GetPathFileList()

	gitGUI = GitGUI(Tk(), fList)
	gitGUI.initialGUI()
	
	gitGUI.root.mainloop()

if __name__ == '__main__':
	main()