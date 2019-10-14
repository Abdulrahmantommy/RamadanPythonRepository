from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage 
import os, sys  
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror, askyesno

class ResizeImages(Frame):
	def __init__(self, parent=None, **options):
		super(ResizeImages, self).__init__(parent, **options)
		self.pack(expand=YES, fill=BOTH)
		self.master.title("Resize Pictures")
		self.config(bg="lightblue")
		self.filepath=StringVar()
		self.width = StringVar()
		self.height = StringVar()
		self.create_title()
		self.create_entries()

	def create_title(self):
		self.titleContainer=Frame(bg="lightblue")

		self.titleContainer.pack(side=TOP, fill=X)
		self.lblTitle=Label(self.titleContainer, text="RESIZE YOUR IMAGES FAST", font=("arial", 26, "bold"))
		self.lblTitle.pack(fill=X)
		self.lblTitle.config(bg="blue", fg="yellow", padx=5, pady=5, bd=5, relief=GROOVE)
		self.lblseparator=Label(self.titleContainer, text="this text", font=("arial", 1))
		self.lblseparator.pack(fill=X)
		self.lblseparator.config(bg="lightblue", fg="lightblue", padx=5, pady=5)

	def create_entries(self):
		self.entContainer=Frame(bg="lightblue")
		self.lblPath=Label(self.entContainer, text="Image file name:", font=("arial", 12, "bold"))
		self.lblPath.grid(row=0, column=0, sticky=W)
		self.lblPath.config(width=14)
		self.entPath=Entry(self.entContainer, textvariable=self.filepath, font=("arial", 12), width=28)
		self.entPath.grid(row=0, column=1, columnspan=2, sticky=W)
		self.btnSearch=Button(self.entContainer, text="Choose file", font=("arial", 12, "bold"), command=self.choose_file)
		self.btnSearch.grid(row=0, column=3, sticky=W)
		self.lblWidth=Label(self.entContainer, text="Choose width:", font=("arial", 12, "bold"), width=14)
		self.lblWidth.grid(row=1, column=0, sticky=W)
		self.entWidth=ttk.Combobox(self.entContainer, textvariable=self.width, font=("arial", 12), width=14)
		self.entWidth["values"]=[x for x in range(100, 1001)]
		self.entWidth.current(0)
		self.entWidth.grid(row=1, column=1, sticky=W)
		self.lblHeight=Label(self.entContainer, text="Choose width:", font=("arial", 12, "bold"), width=14)
		self.lblHeight.grid(row=1, column=2, sticky=W)
		self.entHeight=ttk.Combobox(self.entContainer, textvariable=self.height, font=("arial", 12), width=14)
		self.entHeight["values"]=[x for x in range(100, 1001)]
		self.entHeight.current(0)
		self.entHeight.grid(row=1, column=3, sticky=W)
		
		self.resizeImage = Button(self.entContainer, text="Resize and Save", width=14,font=("arial", 12, "bold"), command=self.resize_image)
		self.resizeImage.grid(row=2, column=0, sticky=W)

		self.clearEntries = Button(self.entContainer, text="Clear entries", width=14, font=("arial", 12, "bold"), command=self.clear_entries)
		self.clearEntries.grid(row=2, column=2, sticky=W)

		self.exitprogram = Button(self.entContainer, text="End program", width=14, font=("arial", 12, "bold"), command=self.quitpro)
		self.exitprogram.grid(row=2, column=3, sticky=W)

		self.entContainer.pack(side=TOP, fill=X)
		labels = [self.lblPath, self.lblWidth, self.lblHeight]
		for lbl in labels:
			lbl.config(width=14, bg="orange", fg="blue", bd=3, relief=GROOVE, anchor=W)

		buttons = [self.btnSearch, self.resizeImage, self.clearEntries, self.exitprogram]
		for btn in buttons:
			btn.config(width=14, bg="#493254", fg="#ffffff", bd=3, relief=GROOVE)

		entries = [self.entPath, self.entWidth, self.entHeight]
		
		entries[0].config(bd=3, relief=SUNKEN)

		self.entPath.focus()
		for child in self.entContainer.winfo_children():
			child.grid_configure(padx=3, pady=3)

	def resize_image(self):
		try:
			filename = self.filepath.get()
			if not os.path.exists(filename):
				showerror("File Error!", "File name does not exist.")
				return
			self.file=os.path.basename(filename)
			width = self.width.get()
			height = self.height.get()
			size = (int(width), int(height))
			targetdir="C:\\Users\\Ramadan Metwally\\Desktop\\resizedImages\\"
			newPath = os.path.join(targetdir, self.file)
			img = Image.open(filename)
			img.thumbnail(size, Image.ANTIALIAS)
			img.save(newPath)
			
		except Exception as e: 
			showerror("Error!", e)
			return

		else: 
			img.show()
		
		

	def quitpro(self):
		choice = askyesno("Quit!", "Do you want to end this session?")
		if choice: 
			sys.exit()
		 

	def clear_entries(self):
		self.entPath.delete(0, END)
		self.entWidth.current(0)
		self.entHeight.current(0)
		self.entPath.focus() 

	def choose_file(self):
		img_file=askopenfilename()
		self.filepath.set(img_file)
		





if __name__ == '__main__':
	win = ResizeImages()
	win.mainloop()