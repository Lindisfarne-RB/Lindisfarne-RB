#install pil (python image library
from tkinter import *
from PIL import ImageTk, Image
class Root(Tk):
   def __init__(self):
      super(Root, self).__init__()
      self.title("Tkinter adding image to canvas RB")
      self.minsize(640,400)
      self.wm_iconbitmap("d:/icon2.ico")
      self.configure(background="#00AAA0")
      self.createCanvasImage()

   def createCanvasImage(self):
      canvas=Canvas(self,bg="black", height=250, width=300)
      canvas.pack(expand=YES, fill=BOTH)
      img= Image.open("logo.png")
      canvas.image=ImageTk.PhotoImage(img)
      canvas.create_image(0,0,image=canvas.image, anchor='nw')
#https://www.youtube.com/watch?v=UZX5kH72Yx4 creating exe of your py file

if __name__ == "__main__":
    root=Root()
    root.mainloop()
