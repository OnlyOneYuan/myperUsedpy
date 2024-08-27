from tkinter import *
from tkinter import Tk
from url_cookies import Ucookies
from os import popen

root = Tk()
root.title = '资管一键数据导出'
root.geometry("300x200+374+182")
cook = Ucookies()
def DesPassword():
    strName = username_text.get()
    passWord = password_text.get()
    if strName == '' or passWord == '':
        print('no words')
        return
    cmd = 'node -e "require(\\"%s\\").init(%s)"' % ('.\\\desTolok',"\'maowl12\'")
    des = popen(cmd)
    print(des.read())
    

username = Label(root,text='username',padx=15,pady=10)
password = Label(root,text='password',padx=15,pady=10)
username_text = Entry(root)
password_text = Entry(root)
print(username_text.get())
submit = Button(root,text='submit',command=DesPassword)

username.grid(row=0,column=0)
password.grid(row=1,column=0)
username_text.grid(row=0,column=1)
password_text.grid(row=1,column=1)
submit.grid(row=2,column=1)




root.mainloop()

