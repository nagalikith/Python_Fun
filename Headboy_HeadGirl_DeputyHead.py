from Tkinter import *
import tkMessageBox
c=0
counthb1=0
counthb2=0
counthb3=0
counthb4=0
counthb5=0

counthg1=0
counthg2=0
counthg3=0
counthg4=0
counthg5=0

countdh1=0
countdh2=0
countdh3=0
countdh4=0
countdh5=0

root=Tk()
root.title('NPS ELECTION 2017-2018')
root.iconbitmap('logo.ico')

def close():
        tkMessageBox.showwarning('Warning!',
                                 'The Elections are not over')
root.protocol('WM_DELETE_WINDOW', close)

leftframe = Frame(root)
leftframe.pack( side = LEFT )

rightframe = Frame(root)
rightframe.pack( side = RIGHT )

topframe = Frame(root)
topframe.pack(side = TOP)

downframe = Frame(root)
downframe.pack(side = BOTTOM)

image = PhotoImage(file="logo.gif")
imgl=Label(root,image=image)


def final():
    a=myvar.get()
    if a=='123456789':
        root.destroy()
    else:
        myvar.set('')

def check():
    global c
    c=c+1
    a1=v1.get() #Cand-1 Vote
    b1=v2.get() #Cand-2 Vote
    c1=v3.get() #Cand-3 Vote
    d1=v4.get() #Cand-4 Vote
    e1=v5.get() #Cand-5 Vote
    
    if a1==1 and b1==0 and c1==0 and d1==0 and e1==0:
         global counthb1
         counthb1=counthb1+1
    elif a1==0 and b1==1 and c1==0 and d1==0 and e1==0:
        global counthb2
        counthb2=counthb2+1
    elif a1==0 and b1==0 and c1==1 and d1==0 and e1==0:
        global counthb3
        counthb3=counthb3+1
    elif a1==0 and b1==0 and c1==0 and d1==1 and e1==0:
        global counthb4
        counthb4=counthb4+1
    elif a1==0 and b1==0 and c1==0 and d1==0 and e1==1:
        global counthb5
        counthb5=counthb5+1
    else:
       tkMessageBox.showinfo('Error Head-Boy','Choose Atleast One option')


    a2=v6.get() #Cand-6 Vote
    b2=v7.get() #Cand-7 Vote
    c2=v8.get() #Cand-8 Vote
    d2=v9.get() #Cand-9 Vote
    e2=v10.get() #Cand-10 Vote
    
    if a2==1 and b2==0 and c2==0 and d2==0 and e2==0:
         global counthg1
         counthg1=counthg1+1
    elif a2==0 and b2==1 and c2==0 and d2==0 and e2==0:
        global counthg2
        counthg2=counthg2+1
    elif a2==0 and b2==0 and c2==1 and d2==0 and e2==0:
        global counthg3
        counthg3=counthg3+1
    elif a2==0 and b2==0 and c2==0 and d2==1 and e2==0:
        global counthg4
        counthg4=counthg4+1
    elif a2==0 and b2==0 and c2==0 and d2==0 and e2==1:
        global counthg5
        counthg5=counthg5+1
    else:
       tkMessageBox.showinfo('Error Head-Girl','Choose Atleast One option')

    a3=v11.get() #Cand-1 Vote
    b3=v12.get() #Cand-2 Vote
    c3=v13.get() #Cand-3 Vote
    d3=v14.get() #Cand-4 Vote
    e3=v15.get() #Cand-5 Vote
    
    if a3==1 and b3==0 and c3==0 and d3==0 and e3==0:
         global countdh1
         countdh1=countdh1+1
    elif a3==0 and b3==1 and c3==0 and d3==0 and e3==0:
        global countdh2
        countdh2=countdh2+1
    elif a3==0 and b3==0 and c3==1 and d3==0 and e3==0:
        global countdh3
        countdh3=countdh3+1
    elif a3==0 and b3==0 and c3==0 and d3==1 and e3==0:
        global countdh4
        countdh4=countdh4+1
    elif a3==0 and b3==0 and c3==0 and d3==0 and e3==1:
        global countdh5
        countdh5=countdh5+1
    else:
       tkMessageBox.showinfo('Error Deputy Head','Choose Atleast One option')
    tkMessageBox.showinfo('Nps Elections','Thank you for voting')
    tx.set(c)



    
    v1.set(0)
    v2.set(0)
    v3.set(0)
    v4.set(0)
    v5.set(0)
    v6.set(0)
    v7.set(0)
    v8.set(0)
    v9.set(0)
    v10.set(0)
    v11.set(0)
    v12.set(0)
    v13.set(0)
    v14.set(0)
    v15.set(0)
        

thelabel = Label(topframe,text='NPS Elections',font=("AR CHRISTY", 26),fg='blue') #Change the text To Change date

tx=IntVar()
c1= Label(root,textvariable=tx,font=("AR CHRISTY", 10))



hblabel= Label(leftframe,text='Head Boy',font=("AR CHRISTY", 20),height=3)


hglabel= Label(rightframe,text='Head Girl',font=("AR CHRISTY", 20),height=3)


dplabel= Label(root,text='Deputy Head',font=("AR CHRISTY", 20),height=3)


##### ONLY CHANGE THE THINGS IN GREEN FROM HERE


v1= IntVar()
cand1= Checkbutton(leftframe,text='Vote for Candidate  1 --head boy',variable=v1,offvalue=0,onvalue=1)#type canidate name instead of canidate 1
v2= IntVar()
cand2= Checkbutton(leftframe,text='Vote for Candidate  2 --head boy',variable=v2,offvalue=0,onvalue=1)#type canidate name instead of canidate 2
v3= IntVar()
cand3= Checkbutton(leftframe,text='Vote for Candidate  3 --head boy',variable=v3,offvalue=0,onvalue=1)#type canidate name instead of canidate 3
v4= IntVar()
cand4= Checkbutton(leftframe,text='Vote for Candidate  4 --head boy',variable=v4,offvalue=0,onvalue=1)#type canidate name instead of canidate 4
v5= IntVar()
cand5= Checkbutton(leftframe,text='Vote for Candidate  5 --head boy',variable=v5,offvalue=0,onvalue=1)#type canidate name instead of canidate 5


v6= IntVar()
cand6= Checkbutton(rightframe,text='Vote for Candidate  1 --head girl',variable=v6,offvalue=0,onvalue=1)#type canidate name instead of canidate 1
v7= IntVar()
cand7= Checkbutton(rightframe,text='Vote for Candidate  2 --head girl',variable=v7,offvalue=0,onvalue=1)#type canidate name instead of canidate 2
v8= IntVar()
cand8= Checkbutton(rightframe,text='Vote for Candidate  3 --head girl',variable=v8,offvalue=0,onvalue=1)#type canidate name instead of canidate 3
v9= IntVar()
cand9= Checkbutton(rightframe,text='Vote for Candidate  4 --head girl',variable=v9,offvalue=0,onvalue=1)#type canidate name instead of canidate 4
v10= IntVar()
cand10= Checkbutton(rightframe,text='Vote for Candidate 5 --head girl',variable=v10,offvalue=0,onvalue=1)#type canidate name instead of canidate 5

v11= IntVar()
cand11= Checkbutton(root,text='Vote for Candidate  1 --deputy head',variable=v11,offvalue=0,onvalue=1)#type canidate name instead of canidate 1
v12= IntVar()
cand12= Checkbutton(root,text='Vote for Candidate  2 --deputy head',variable=v12,offvalue=0,onvalue=1)#type canidate name instead of canidate 2
v13= IntVar()
cand13= Checkbutton(root,text='Vote for Candidate  3 --deputy head',variable=v13,offvalue=0,onvalue=1)#type canidate name instead of canidate 3
v14= IntVar()
cand14= Checkbutton(root,text='Vote for Candidate  4 --deputy head',variable=v14,offvalue=0,onvalue=1)#type canidate name instead of canidate 4
v15= IntVar()
cand15= Checkbutton(root,text='Vote for Candidate  5 --deputy head',variable=v15,offvalue=0,onvalue=1)#type canidate name instead of canidate 5





#DONT TOUCH!!!!!!!!!!

submit= Button(root,text='Submit',command=check)
quit1= Button(root,text='Quit',command= final)
myvar=StringVar()
w= Entry(downframe,show='*',textvariable=myvar)





#MAIN PACKING HERE
imgl.pack()
thelabel.pack(fill=BOTH)#Main Nps Election 2017-2018
hblabel.pack(side=TOP,anchor=N) # position of Headboy
hglabel.pack(side=TOP,anchor=N) # position of HeadGirl
dplabel.pack(side=TOP,anchor=CENTER) # position of Deputy Head



cand1.pack(side=TOP) # position of Head-BOY cand-1
cand2.pack(side=TOP) # position of Head-BOY cand-2
cand3.pack(side=TOP)  # position of Head-BOY cand-3
cand4.pack(side=TOP)  # position of Head-BOY cand-4
cand5.pack(side=TOP)  # position of Head-BOY cand-5



cand6.pack(side=TOP)  # position of Head-Girl cand-1
cand7.pack(side=TOP)  # position of Head-Girl cand-2
cand8.pack(side=TOP)  # position of Head-Girl cand-3
cand9.pack(side=TOP)  # position of Head-Girl cand-4
cand10.pack(side=TOP)  # position of Head-Girl cand-5

cand11.pack(side=TOP)  # position of Deputy-Head cand-1
cand12.pack(side=TOP)  # position of Deputy-Head cand-2
cand13.pack(side=TOP)  # position of Deputy-Head cand-3
cand14.pack(side=TOP)  # position of Deputy-Head cand-4
cand15.pack(side=TOP)  # position of Deputy-Head cand-5

c1.pack(side=RIGHT,anchor=S)
w.pack(side=RIGHT)
quit1.pack(side=BOTTOM)
submit.pack(side=BOTTOM) # position of submit

root.mainloop()

print"election result for head boy post"

print "canidate 1-->",counthb1
print "canidate 2-->",counthb2
print "canidate 3-->",counthb3
print "canidate 4-->",counthb4
print "canidate 5-->",counthb5

print"election result for head girl post"


print "canidate 1-->",counthg1
print "canidate 2-->",counthg2
print "canidate 3-->",counthg3
print "canidate 4-->",counthg4
print "canidate 5-->",counthg5

print"election result for deputy head post"

print "canidate 1-->",countdh1
print "canidate 2-->",countdh2
print "canidate 3-->",countdh3
print "canidate 4-->",countdh4
print "canidate 5-->",countdh5









