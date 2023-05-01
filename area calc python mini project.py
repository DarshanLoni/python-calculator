from tkinter import *
import math
root=Tk()
root.geometry("1000x1000")
root.title("Area Calculator")
root.configure(bg="#a0cfde")
def choice():
    c=int(e1.get())
   
    if c==1:
        def c1():
            s=se1.get()
            s=int(s)
            area=s*s
            sl2=Label(root,text=area,bg="#a0cfde",font=("times new roman",12))
            sl2.grid(row=9,column=1)
            l1empty=Label(root,text="",bg="#a0cfde")

            sal=Label(root,text="Area of square is  :",bg="#a0cfde",font=("times new roman",12))
            sal.grid(row=9 ,column=0)
            
        sl1=Label(root, text="Enter the side of square :",bg="#a0cfde",font=("times new roman",12))
        se1=Entry(root,text="sideenter")
        sb1=Button(root,text="Submit",command=c1, bg="green", fg="white",width=12)
        l1empty=Label(root,text="",bg="#a0cfde")
        l1empty.grid(row=8,column=0)




        sl1.grid(row=6,column=0)
        se1.grid(row=6,column=1)
        sb1.grid(row=7,column=1)
        b1.config(state='disable',disabledforeground="Black")
        
        

        

    elif c==2:
        def c1():
            l=re1.get()
            l=int(l)
            b=re2.get()
            b=int(b)
            area=l*b
            ral=Label(root,text="Area of Rectangle is  :",bg="#a0cfde",font=("times new roman",12))
            ral.grid(row=10 ,column=0)
            rl2=Label(root,text=area,bg="#a0cfde",font=("times new roman",12))
            rl2.grid(row=10,column=1)
            l2empty=Label(root,text="",bg="#a0cfde")
            l2empty.grid(row=9,column=0)
            

        rl1=Label(root, text="Enter the length of rectangle :",bg="#a0cfde",font=("times new roman",12))
        rl2=Label(root, text="Enter the breadth of Rectangle :",bg="#a0cfde",font=("times new roman",12))
        re1=Entry(root,text="k")
        re2=Entry(root,text="l")
        rb2=Button(root,text="Submit", command=c1, bg="green", fg="white",width=12)

        rl1.grid(row=6,column=0)
        rl2.grid(row=7,column=0)
        re1.grid(row=6,column=1)
        re2.grid(row=7,column=1)
        rb2.grid(row=8,column=1)
        b1.config(state='disable',disabledforeground="Black")


    elif c==3:
        def c1():
            r=ce1.get()
            r=int(r)
            area=r*r*math.pi
            cl2=Label(root,text=area,bg="#a0cfde",font=("times new roman",12))
            cl2.grid(row=9,column=1)
            ccal=Label(root,text="Area of Circle is  :",bg="#a0cfde",font=("times new roman",12))
            ccal.grid(row=9 ,column=0)
            l3empty=Label(root,text="",bg="#a0cfde")
            l3empty.grid(row=8,column=0)
            
            
        cl1=Label(root, text="Enter the radius of circle :",bg="#a0cfde",font=("times new roman",12))
        cb1=Button(root,text="Submit",command=c1, bg="green", fg="white",width=12)
        ce1=Entry(root,text="rad")


        cl1.grid(row=6,column=0)
        cb1.grid(row=7,column=1)
        ce1.grid(row=6,column=1)
        b1.config(state='disable',disabledforeground="Black")

    elif c==4:
        def c1():
            h=Te1.get()
            h=int(h)
            b=Te2.get()
            b=int(b)
            area=0.5*h*b
            Tl2=Label(root,text=area,bg="#a0cfde",font=("times new roman",12))
            Tl2.grid(row=10,column=1)
            tal=Label(root,text="Area of Triangle is  :",bg="#a0cfde",font=("times new roman",12))
            tal.grid(row=10 ,column=0)
            l2empty=Label(root,text="",bg="#a0cfde")
            l2empty.grid(row=9,column=0)

        Tl1=Label(root, text="Enter the Height of Triangle :",bg="#a0cfde",font=("times new roman",12))
        Tl2=Label(root, text="Enter the Base of Triangle :",bg="#a0cfde",font=("times new roman",12))
        Tb2=Button(root,text="Submit", command=c1, bg="green", fg="white",width=12)
        Te1=Entry(root,text="k")
        Te2=Entry(root,text="l")


        Tl1.grid(row=6,column=0)
        Tl2.grid(row=7,column=0)

        Te1.grid(row=6,column=1)
        Te2.grid(row=7,column=1)
        Tb2.grid(row=8,column=1)
        b1.config(state='disable',disabledforeground="Black")

    elif c==5:
        def c1():
            s=ce1.get()
            s=int(s)
            area=s*s*6
            cl2=Label(root,text=area,bg="#a0cfde",font=("times new roman",12))
            cl2.grid(row=9,column=1)
            cual=Label(root,text="Area of Cube is  :",bg="#a0cfde",font=("times new roman",12))
            cual.grid(row=9 ,column=0)
            l5empty=Label(root,text="",bg="#a0cfde")
            l5empty.grid(row=8,column=0)
            
            
        cs1=Label(root, text="Enter the side of Cube :",bg="#a0cfde",font=("times new roman",12))
        ce1=Entry(root,text="sideenter")
        cb1=Button(root,text="Submit",command=c1, bg="green", fg="white",width=12)

        cs1.grid(row=6,column=0)
        ce1.grid(row=6,column=1)
        cb1.grid(row=7,column=1)
        b1.config(state='disable',disabledforeground="Black")

        
    # else:
    #     li=Label(root,text="Enter Valid number",font=("Arial",12),bg="#a0cfde")
    #     li.grid(row=4 , column=2)
            




l1=Label(root,text="Area Calculator",font=("Times New Roman",25),bg="yellow")
lr=Label(root,text='''1.Square   2.Rectangle   3.Circle  4.Triangle  5.Cube''',font=("Arial",13),bg="#a0cfde")
ler=Label(root,text='''Enter the choice from the above''',bg="#a0cfde",font=("times new roman",12),padx=10)
lempty=Label(root,text="",bg="#a0cfde")
b1=Button(root,text="Submit", command=choice,bg="green", fg="white",width=12)
e1=Entry(root,text="entry")

l1.grid(row=0 , column=2)
lr.grid(row=1 , column=2)
ler.grid(row=4, column=0)
lempty.grid(row=3,column=0)
b1.grid(row=5 ,column=1)
e1.grid(row=4, column=1)


root.mainloop()