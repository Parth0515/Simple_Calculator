import tkinter as tk


e = ""
large_font = ('Verdana',30)

def click(num):
    e = ""
    e = e + str(num)
    tk.Entry.insert(entry, tk.END, e)
    

def clear():
    tk.Entry.delete(entry, 0, tk.END)

def equals():
    try:
        result = str(eval(tk.Entry.get(entry)))
        clear()
        tk.Entry.insert(entry,0,result)
    except:
        clear()
        tk.Entry.insert(entry, 0, "Error")

root = tk.Tk()
#Adds the title
root.title("Calculator v0")

root.iconbitmap('tkinter/images/cal_icon.ico')

#default size for window
root.minsize(width=300, height = 400)

#entry window
entry = tk.Entry(root, width=10, font = large_font )
entry.grid(row=0,column=0,columnspan=6,padx=20,pady=15)

#initalize the button
btn1 = tk.Button(root, text="1", padx=20, pady= 20, command=lambda : click(1))
btn2 = tk.Button(root, text="2", padx=20, pady= 20, command=lambda : click(2))
btn3 = tk.Button(root, text="3", padx=20, pady= 20, command=lambda : click(3))
btn4 = tk.Button(root, text="4", padx=20, pady= 20, command=lambda : click(4))
btn5 = tk.Button(root, text="5", padx=20, pady= 20, command=lambda : click(5))
btn6 = tk.Button(root, text="6", padx=20, pady= 20, command=lambda : click(6))
btn7 = tk.Button(root, text="7", padx=20, pady= 20, command=lambda : click(7))
btn8 = tk.Button(root, text="8", padx=20, pady= 20, command=lambda : click(8))
btn9 = tk.Button(root, text="9", padx=20, pady= 20, command=lambda : click(9))
btn0 = tk.Button(root, text="0", padx=20, pady= 20, command=lambda : click(0))
btn_c = tk.Button(root, text="CE", padx=20, pady= 20, command=lambda : clear())
btn_eq = tk.Button(root, text="=", padx=20, pady= 20, command=equals)
btn_add = tk.Button(root, text="+", padx=20, pady= 20, command=lambda : click("+"))
btn_sub = tk.Button(root, text="-", padx=20, pady= 20, command=lambda : click("-"))
btn_mul= tk.Button(root, text="X", padx=20, pady= 20, command=lambda : click("*"))
btn_div= tk.Button(root, text="/", padx=20, pady= 20, command=lambda : click("/"))


#Setup their location on window
btn_eq.grid(row=4, column=3, padx=5,pady=5)
btn_c.grid(row=4, column=1, padx=5, pady=5)
btn0.grid(row=4, column=2, padx=5,pady=5)
btn_div.grid(row=4, column=4, padx=5,pady=5)

btn1.grid(row=3, column=1, padx=5,pady=5)
btn2.grid(row=3, column=2, padx=5,pady=5)
btn3.grid(row=3, column=3, padx=5,pady=5)
btn_mul.grid(row=3, column=4, padx=5,pady=5)

btn4.grid(row=2, column=1, padx=5,pady=5)
btn5.grid(row=2, column=2, padx=5,pady=5)
btn6.grid(row=2, column=3, padx=5,pady=5)
btn_sub.grid(row=2, column=4, padx=5,pady=5)

btn7.grid(row=1, column=1, padx=5,pady=5)
btn8.grid(row=1, column=2, padx=5,pady=5)
btn9.grid(row=1, column=3, padx=5,pady=5)
btn_add.grid(row=1, column=4, padx=5,pady=5)



root.mainloop()