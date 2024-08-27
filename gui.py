from tkinter import Frame, Label, LabelFrame, Menu, Radiobutton, Tk, Toplevel, filedialog,Button
import tkinter

app = Tk()
app.title("自动办公")


#手动选择文件
def opendir():
    app.withdraw
    path = filedialog.askdirectory()
#切换页面
def switchWin(oldWin:Toplevel):
    oldWin.destroy()
    newWin = Toplevel(app)

#菜单
bar  = Menu(app)
menu = Menu(bar,cursor='spider',tearoff=False)
menu.add_command(label="file",command=None)
menu.add_command(label="dir",command=None) 
bar.add_cascade(label="文件",menu=menu)
bar.add_command(label="退出",command=app.destroy)

#主界面+多frame
frame1 = LabelFrame(height = 100,width = 800,text="ok")
radio1 = Radiobutton(frame1,text="qinq",indicatoron=False,value=1,variable=getVar)
radio2 = Radiobutton(frame1,text="koe tj e ",indicatoron=False)

frame1.pack(side=tkinter.LEFT,expand=tkinter.YES,fill=tkinter.X)
radio1.pack(side=tkinter.LEFT,expand=tkinter.YES,fill=tkinter.X)
radio2.pack(side=tkinter.LEFT,expand=tkinter.YES,fill=tkinter.X)

print()

app.config(menu=bar)
app.mainloop()
