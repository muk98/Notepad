import tkinter as tk
from tkinter import *
import os
from tkinter.filedialog import *
from tkinter.messagebox import *


class editor:
	__gui = Tk()
	__textArea = Text(__gui,width = 1000,height=500,bg='grey')
	__textArea.pack()
	__menu = Menu(__gui)
	__gui.config(menu=__menu)
	__filemenu = Menu(__menu,tearoff=0)
	__editmenu = Menu(__menu,tearoff=0)
	__helpmenu = Menu(__menu,tearoff=0)
 
	__file = None

	def __init__(self):

		self.__gui.title('Untitled - MK EDITOR')

		self.__menu.add_cascade(label='File',menu=self.__filemenu)
		# self.__menu.add_cascade(label='Help',menu=self.__helpmenu)
		self.__filemenu.add_command(label='New',command = self.__new_file)
		self.__filemenu.add_command(label='Open...',command = self.__open_file)
		self.__filemenu.add_command(label='Save As',command = self.__save_file)
		self.__filemenu.add_separator()
		self.__filemenu.add_command(label='Exit',command = self.__exit)


		self.__menu.add_cascade(label='Edit',menu=self.__editmenu)
		self.__editmenu.add_command(label='Copy',accelerator="Ctrl+C",command = lambda: self.__textArea.event_generate('<<Copy>>') )
		self.__editmenu.add_command(label='Paste',accelerator="Ctrl+V",command = lambda: self.__textArea.event_generate('<<Paste>>') )
		self.__editmenu.add_command(label='Cut',accelerator="Ctrl+X",command = lambda: self.__textArea.event_generate('<<Cut>>'))



		self.__menu.add_cascade(label='Help',menu=self.__helpmenu)
		self.__helpmenu.add_command(label='About')
		
	
	def __open_file(self):
		self.__file = askopenfilename(defaultextension='.txt',filetypes = [("ALL Files","*.*"),("Text Documents","*.txt")])

		if self.__file == "":
			self.__file = None
		else:

			self.__gui.title(self.__file)
			self.__textArea.delete(1.0,END)
			
			file = open(self.__file,'r')
			self.__textArea.insert(1.0,file.read())
			file.close()
 
		

	def __new_file(self):
		self.__gui.title('Untitled - MK EDITOR')
		self.__file = None
		self.__textArea.delete(1.0,END)


	def __save_file(self):

		if self.__file == None:
			self.__file = asksaveasfilename(initialfile="Untitled.txt",defaultextension='.txt',
												filetypes = [("ALL Files","*.*"),("Text Documents","*.txt")])

			if self.__file == "":
				self.file = None
			else:
				file = open(self.__file,'w')
				file.write(self.__textArea.get(1.0,END))
				file.close()

				self.__gui.title(os.path.basename(self.__file) + ' - MK EDITOR')

		else:
			file = open(self.__file,'w')
			file.write(self.__textArea.get(1.0,END))
			file.close()



	def __exit(self):
		self.__gui.destroy()
		

	def run(self):
		self.__gui.mainloop()



app = editor()
app.run()

