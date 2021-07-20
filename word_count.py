import tkinter as tk
import threading
from tkinter import ttk

root=tk.Tk()
root.geometry("500x500+480+180")
root.title("Word Counter(Ashirwad TechnoCraft)")
root.resizable(0,0)
root.configure(bg='#51D0FB')
p1=tk.PhotoImage(file="icon.png")
root.iconphoto(False,p1)

s=0
m=0
word=0
sec=0
min=0
f1=tk.StringVar()
f2=tk.StringVar()

def enter():
    from tkinter import messagebox as msg
    global s,m,sec,min,word
    word=0
    try:
        sec = int(f2.get())
        min = int(f1.get())
        if((sec==0)and(min==0)):
            ques = msg.showinfo('Warning','Input something to continue')
        else:
            s = sec
            m = min
            if(s==0):
                s = 60
                m = m - 1
            e1.config(state='disabled')
            e2.config(state='disabled')
            text.delete(1.0,'end')
            timer()
    except:
        msg.showinfo('Warning','Input something to continue')

def timer():
    global s,m
    s = s - 1
    if(s==0):
        m = m - 1
        s = 60
    if(((s==60)and(m==-1))==False):
        f1.set('%i'%(m))
        f2.set('%i'%(s))
        threading.Timer(1.0,timer).start()
    else:
        stop()
        
def stop():
    global word,sec,min
    f2.set(0)
    l=text.get(1.0,'end').split(' ')
    try:
        l.remove('\n')
    except:
        pass
    word = len(l)
    sec = (60*min)+sec
    word = (word/sec)*60
    word = round(word)
    lbl.config(text=str(word)+" WpM")
    e1.config(state='normal')
    e2.config(state='normal')
                    

tk.Label(root,text="Timer:",bg='#51D0FB',font=("new times roman",10,"italic","bold")).place(x=10,y=12)

tk.Label(root,text='Minute:',bg='#51D0FB',font=("new times roman",8,"italic")).place(x=70,y=14)
e1 = tk.Entry(root,text=f1,width=5,justify=tk.RIGHT,relief=tk.FLAT)
e1.place(x=120,y=14)
tk.Label(root,text='Second:',bg='#51D0FB',font=("new times roman",8,"italic")).place(x=170,y=14)
e2 = tk.Entry(root,text=f2,width=5,justify=tk.RIGHT,relief=tk.FLAT)
e2.place(x=220,y=14)

tk.Label(root,text="Speed:",bg='#51D0FB',font=("new times roman",10,"italic","bold")).place(x=260,y=14)
lbl = tk.Label(root,text=str(word)+" WpM",bg='#51D0FB',font=("new times roman",8,"italic"))
lbl.place(x=310,y=16)

tk.Button(root,text='Start',bg='white',fg='black',width=10,relief=tk.FLAT,command=enter,font=("new times roman",10,"italic")).place(x=400,y=10)

st=ttk.Style()
st.theme_use('clam')
st.configure('Vertical.TScrollbar',orient='vertical',background='#029D9D',bordercolor='white',troughcolor='#6FE9F2',lightcolor='#02EAEA',
                    darkcolor='#02EAEA',arrowcolor='white',gripcount=0)
fm = tk.Frame(root,bd=5,bg='white')
fm.place(x=5,y=40,width=490,height=420)
title = tk.Label(fm,text="Text Area",fg='blue',bg='yellow',width=20,font=("new times roman",15,"italic","bold")).pack(fill=tk.X)
tk.Label(fm,width=1,bg='white').pack(fill=tk.X)
scrol_y = ttk.Scrollbar(fm,style='Vertical.TScrollbar')
text = tk.Text(fm,bg='#CEF8FB',wrap=tk.WORD,padx=5,pady=5,yscrollcommand=scrol_y.set)
scrol_y.pack(padx=4,side=tk.RIGHT,fill=tk.Y)
scrol_y.config(command=text.yview)
text.pack(fill=tk.BOTH,expand=1)

tk.Label(root,text="Give one space after each word,comma and fullstop",bg='#51D0FB',font=("new times roman",8,"italic")).place(x=10,y=470)
tk.Label(root,text="--A project by Alik Dey",bg='#51D0FB',font=("new times roman",10,"italic","bold")).place(x=330,y=470)

root.mainloop()
