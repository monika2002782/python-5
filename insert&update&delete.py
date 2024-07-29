import tkinter
from tkinter import*
from tkinter import ttk, font, messagebox
from PIL import  Image
from PIL.ImageTk import PhotoImage
import pymysql as mysql
import requests




def click(r):

      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="skyblue1")
      f=Frame(r,width=1500,height=50,bg="dark slate blue").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="dark slate blue",fg="white")
      x.place(relx=0.4,rely=0.01)

     
      f=Frame(r,width=1500,height=1500,bg="skyblue1")
      img1=PhotoImage(Image.open("delete1.jpg"))
      x=Label(f,image=img1).place(relx=0.270,rely=0.1)

      f.pack()
      

      b=Button (r,text="Delete",font=lf,bg="dark slate blue",fg="white").place(relx=0.390,rely=0.780)
      b=Button (r,text="Next",font=lf,bg="dark slate blue",fg="white").place(relx=0.520,rely=0.780)
     
      f=Frame(r,width=1500,height=51,bg="dark slate blue").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="dark slate blue",fg="white").place(relx=0.4,rely=0.94)
      r.mainloop()

def Next2(r):

      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="cadetblue1")
      f=Frame(r,width=1500,height=50,bg="black").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="black",fg="white")
      x.place(relx=0.4,rely=0.01)

     
      f=Frame(r,width=1500,height=1500,bg="cadetblue1")
      img1=PhotoImage(Image.open("update.jpg"))
      x=Label(f,image=img1).place(relx=0.290,rely=0.180)

      f.pack()
       



      b=Button (r,text="Insert",font=lf,bg="black",fg="white").place(relx=0.360,rely=0.7)
      b=Button (r,text="Next",font=lf,bg="black",fg="white",command=lambda:click(r)).place(relx=0.5,rely=0.7)
     
      f=Frame(r,width=1500,height=51,bg="black").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="black",fg="white").place(relx=0.4,rely=0.94)
      r.mainloop()




def time(r):

      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="cadetblue1")
      f=Frame(r,width=1500,height=50,bg="black").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="black",fg="white")
      x.place(relx=0.4,rely=0.01)

     
      f=Frame(r,width=1500,height=1500,bg="cadetblue1")
      img1=PhotoImage(Image.open("update.jpg"))
      x=Label(f,image=img1).place(relx=0.290,rely=0.180)

      f.pack()
       


      b=Button (r,text="Update",font=lf,bg="black",fg="white").place(relx=0.360,rely=0.7)
      b=Button (r,text="Next",font=lf,bg="black",fg="white",command=lambda:get(r)).place(relx=0.5,rely=0.7)
     
      f=Frame(r,width=1500,height=51,bg="black").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="black",fg="white").place(relx=0.4,rely=0.94)
      r.mainloop()


def set(r):
      
      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="skyblue1")
      f=Frame(r,width=1500,height=50,bg="dark slate blue").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="dark slate blue",fg="white")
      x.place(relx=0.4,rely=0.01)

     
      f=Frame(r,width=1500,height=1500,bg="skyblue1")
      img1=PhotoImage(Image.open("insert.jpg"))
      x=Label(f,image=img1).place(relx=0.270,rely=0.1)

      f.pack()
      

      b=Button (r,text="Insert",font=lf,bg="dark slate blue",fg="white").place(relx=0.390,rely=0.780)
      b=Button (r,text="Next",font=lf,bg="dark slate blue",fg="white",command=lambda:time(r)).place(relx=0.520,rely=0.780)
     
      f=Frame(r,width=1500,height=51,bg="dark slate blue").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="dark slate blue",fg="white").place(relx=0.4,rely=0.94)
      r.mainloop()



def get(r):

      r.destroy()
      r=Tk()
      r.geometry("1000x1000")
      r.attributes('-fullscreen', True)
      r.configure(bg="skyblue1")
      f=Frame(r,width=1500,height=50,bg="dark slate blue").pack()
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="METRO BOOKING",font=lf,bg="dark slate blue",fg="white")
      x.place(relx=0.4,rely=0.01)

     
      f=Frame(r,width=1500,height=1500,bg="skyblue1")
      img1=PhotoImage(Image.open("delete1.jpg"))
      x=Label(f,image=img1).place(relx=0.270,rely=0.1)

      f.pack()
      

      b=Button (r,text="Delete",font=lf,bg="dark slate blue",fg="white").place(relx=0.390,rely=0.780)
      b=Button (r,text="Next",font=lf,bg="dark slate blue",fg="white").place(relx=0.520,rely=0.780)
     
      f=Frame(r,width=1500,height=51,bg="dark slate blue").place(relx=0,rely=0.940)
      lf=font.Font(weight="bold",family="Times New Roman",size=25 )
      x=Label(f,text="@EXPRESS 3/28",font=lf,bg="dark slate blue",fg="white").place(relx=0.4,rely=0.94)
      r.mainloop()



