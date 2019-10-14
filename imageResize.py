from tkinter import *
from tkinter import ttk 
from tkinter.messagebox import showerror, showinfo, askyesno, askokcancel
from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfile
from PIL import Image
import os, sys

class ImageResize(Frame):
	def __init__(self, parent=None, **options):
		super(ImageResize, self).__init__(parent, **options)
		self.pack(expand=YES, fill=BOTH)
		self.master.title("Photo Resizer")
		self.config(bg="lightblue")
		self.sourceImage=StringVar()
		self.targetDir = StringVar()
		self.imgwidth=StringVar()
		self.imgheight=StringVar()
		self.create_title()
		self.create_entries()


	def create_title(self):
		self.titleContainer=Frame()
		self.lblTitle=Label(self.titleContainer, text="IMAGE FAST RESIZE")
		self.lblTitle.pack(side=TOP, fill=X)
		self.lblTitle.config(font=("arial", 25, "bold"))
		self.lblTitle.config(padx=5, pady=5, bd=5, relief=RIDGE)
		self.lblTitle.config(bg="#4a1d2f", fg="#dad1d5")
		self.titleContainer.pack(side=TOP, fill=X)
		self.sepContainer=Frame(bg="white")
		self.sep=Label(self.sepContainer, text="meme", font=("arial", 1, "normal"))
		self.sep.pack(fill=X)
		self.sep.config(bg="white", fg="white")
		self.sepContainer.pack(side=TOP, fill=X)

	def create_entries(self):
		self.entContainer=Frame(bg="lightblue")
		self.lblsource=Label(self.entContainer, text="Source File:")
		self.lblsource.grid(row=0, column=0, sticky=W)
		self.entsource=Entry(self.entContainer, textvariable=self.sourceImage)
		self.entsource.grid(row=1, column=0, columnspan=2, sticky="we")
		self.entsource.config(font=("arial", 12), bd=5, relief=SUNKEN, bg="#edf3cf")
		
		self.btnSearch=Button(self.entContainer, text="Search Image Files", command=self.search_file)
		self.btnSearch.grid(row=1, column=2, sticky="we")
		self.btnSearch.config(width=14, font=("arial", 10, "bold"))
		self.btnSearch.config(bg="#8de0d6")
		
		self.lblwidth = Label(self.entContainer, text="Select Width:")
		self.lblwidth.grid(row=2, column=0, sticky=E)		
		self.entWidth=ttk.Combobox(self.entContainer, textvariable=self.imgwidth)
		self.entWidth.grid(row=2, column=1, sticky="we")
		self.entWidth["values"]=[x for x in range(60, 1080)]
		self.entWidth.current(0)
		self.entWidth.config(width=12, font=("arial", 12))
		
		self.lblheight=Label(self.entContainer, text="Select Height:")
		self.lblheight.grid(row=2, column=2, sticky=E)
		self.entHeight=ttk.Combobox(self.entContainer, textvariable=self.imgheight)
		self.entHeight.grid(row=2, column=3, sticky="we")
		self.entHeight["values"]=[x for x in range(60, 1080)]
		self.entHeight.current(0)
		self.entHeight.config(width=12, font=("arial", 12))

		self.lbltarget=Label(self.entContainer, text="Target Directory:")
		self.lbltarget.grid(row=3, column=0, sticky=W)
		self.enttarget=Entry(self.entContainer, textvariable=self.targetDir)
		self.enttarget.grid(row=4, column=0, columnspan=2, sticky="we")
		self.enttarget.config(font=("arial", 12), bd=5, relief=SUNKEN, bg="#edf3cf")
		
		self.btnSearchDir=Button(self.entContainer, text="Choose a Directory", command=self.choose_directory)
		self.btnSearchDir.grid(row=4, column=2, sticky="we")
		# self.btnSearchDir["font"]=("arial", 10, "bold")
		# self.btnSearchDir["bg"]="#8de0d6"
		# self.btnSearchDir["width"]=14
		self.btnSearchDir.config(width=14, font=("arial", 10, "bold"), bg="#8de0d6")		
		
		self.btnResize=Button(self.entContainer, text="RESIZE & SAVE", command=self.resize_file)
		self.btnResize.grid(row=5, column=1, sticky="we")
		self.btnResize.config(width=12, font=("arial", 10, "bold"))

		self.btnClear=Button(self.entContainer, text="CLEAR SOURCE", command=self.clear_entry)
		self.btnClear.grid(row=5, column=2, sticky="we")
		self.btnClear.config(width=12, font=("arial", 10, "bold"))

		self.btnClose=Button(self.entContainer, text="QUIT PROGRAM", command=self.close_window)
		self.btnClose.grid(row=5, column=3, sticky="we")
		self.btnClose.config(width=12, font=("arial", 10, "bold"))

		buttons = [self.btnResize, self.btnClear, self.btnClose]
		for btn in buttons:
			btn.config(bg="#f9c09d", fg="#640eef")
			btn.config(bd=3, relief=GROOVE)

		labels= [self.lblsource, self.lblwidth, self.lblheight]
		for lbl in labels:
			lbl.config( bg="lightblue", fg="black")
			lbl.config(font=("arial", 10, "bold"))

		self.entsource.focus()

		for child in self.entContainer.winfo_children():
			child.grid_configure(padx=3, pady=3)

		self.entContainer.pack(side=TOP, fill=BOTH)
	
	def search_file(self):
		self.filename = askopenfilename()
		self.sourceImage.set(self.filename)

	def choose_directory(self):
		self.targetdir= askdirectory()
		self.targetDir.set(self.targetdir)

	
	def clear_entry(self):
		self.entsource.delete(0, END)
		self.entWidth.current(0)
		self.entHeight.current(0)
		self.entsource.focus()
	 

	def resize_file(self):
		try:
			self.imgfilename = self.sourceImage.get()
			if not os.path.exists(self.imgfilename):
				showerror("File Error!", "This file does not exist.")
				return
			self.imgfile = os.path.basename(self.imgfilename)
			print(self.imgfile)
			self.targetDirectory = self.targetDir.get()
			if not os.path.isdir(self.targetDirectory):
				showerror("Directory Error", "Please choose a valid directory!")
				return
			self.newWidth = self.imgwidth.get()
			self.newHeight=self.imgheight.get()
			self.newSize = (int(self.newWidth), int(self.newHeight))
			img = Image.open(self.imgfilename)
			img.thumbnail(self.newSize, Image.ANTIALIAS)
			newpah = os.path.join(self.targetDirectory, self.imgfile)
			img.save(newpah)

		except Exception as e:
			showerror("Error!", "Resize image failed!")
			return

		else: 
			img.show()

	  
	
	def close_window(self):
		choice = askyesno("Quit!", "Do you want to end this session?")
		if choice:
			sys.exit()


if __name__ == '__main__':
	window = ImageResize()
	window.mainloop()
