#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter
import random


# In[14]:


colours=['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown','Golden','Silver']
score=0
time=45


# In[9]:


def nextColor():
    global score
    global time
    if time>0:
        e.focus_set()
        if e.get().lower()==colours[1].lower():
            score+=1
        e.delete(0,tkinter.END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scorelabel.config(text = "Score: " + str(score)) 


# In[15]:


def countdown():
    global time
    global score
    if time>0:
        time-=1
        timelabel.config(text='Time left:'+str(time))
        timelabel.after(1000,countdown)
    else:
        time=45
        score=0


# In[11]:


def startGame(event):
    if time==45:
        countdown()
    nextColor()


# In[16]:


root=tkinter.Tk()
root.title('COLOR-COLOR')
root.geometry('400x200')
instructions=tkinter.Label(root,text='Type in the colour of words!!! Not the words!!',font=('Helvetica',14))
instructions.pack()
scorelabel=tkinter.Label(root,text='Preds Enter to start',font=('Helvetica',14))
scorelabel.pack()
timelabel=tkinter.Label(root,text='Time left:'+str(time),font=('Helvetica',12))
timelabel.pack()
label=tkinter.Label(root,font=('Helvetica',80))
label.pack()
e=tkinter.Entry(root)
root.bind('<Return>',startGame)
e.pack()
e.focus_set()
root.mainloop()


# In[ ]:




