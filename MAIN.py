from tkinter import *
from tkinter import ttk
# Display
window = Tk()
window.geometry("720x480")
window.resizable(width=0, height=0)
window.iconbitmap("LOGO.ico")
window.configure(bg="#8C8F82")
window.title("Login")
frame2 = Frame(window, bg="#0B297B", width=720, height=80, bd=20, relief="sunken")
frame2.place(x=0, y=0)
TITILE1 = Label(window, text="Convert Manager", fg="white", bg="#0B297B", font=("Arial", 20, "bold")).place(x=260, y=30)
frame1 = Frame(window, bg="#8C8F82", width=720, height=380, bd=20, relief="sunken")
frame1.place(x=0, y=90)
def decimal_octal(n):
    rem = 0
    i = 1
    octal = 0
    while n!=0:
        rem = n%8
        n = n//8
        octal += rem * i
        i *=10
    return octal
def change():
    x = nmbr1_name.get()
    nmbr1_name.set(nmbr2_name.get())
    nmbr2_name.set(x)

def Convert():
    Vn1 = nmbr1_name.get()
    Vn2 = nmbr2_name.get()

    n1 = nmbr1_value.get()
    nmbr2_value.get()
    if Vn1 == 'Decimale' and Vn2 == 'Binaire':
        nmbr2_value.set(bin(int(n1)).replace("0b",""))

    if Vn1 == 'Binaire' and Vn2 == 'Decimale':
        nmbr2_value.set(int(n1, 2))

    if Vn1 == 'Hexadecimale' and Vn2 == 'Decimale':
        nmbr2_value.set(int(n1, 16))

    if Vn1 == 'Decimale' and Vn2 == 'Hexadecimale':
        rep = hex(int(n1)).split('x')[-1]
        nmbr2_value.set(rep)

    if Vn1 == 'Octale' and Vn2 == 'Decimale':
        rep2 = int(n1, 8)
        nmbr2_value.set(rep2)

    if Vn1 == 'Decimale' and Vn2 == 'Octale':
        rep2 = decimal_octal(int(n1))
        nmbr2_value.set(rep2)

    if Vn1 == 'Binaire' and Vn2 == 'Hexadecimale':
        rp1 = int(n1, 2)
        rp2 = hex(int(rp1)).split('x')[-1]
        nmbr2_value.set(rp2)

    if Vn1 == 'Hexadecimale' and Vn2 == 'Binaire':
        rp1 = int(n1, 16)
        rp2 = bin(int(rp1)).replace("0b", "")
        nmbr2_value.set(rp2)

    if Vn1 == 'Binaire' and Vn2 == 'Octale':
        rp1 = int(n1, 2)
        rp2 = oct(rp1)
        nmbr2_value.set(rp2)

    if Vn1 == 'Octale' and Vn2 == 'Binaire':
        rep2 = int(n1, 8)
        nmbr2_value.set(bin(int(rep2)).replace("0b", ""))

    if Vn1 == 'Hexadecimale' and Vn2 == 'Octale':
        rp1 = int(n1, 16)
        rep2 = decimal_octal(int(rp1))
        nmbr2_value.set(rep2)

    if Vn1 == 'Octale' and Vn2 == 'Hexadecimale':
        rep2 = int(n1, 8)
        rep = hex(int(rep2)).split('x')[-1]
        nmbr2_value.set(rep)
LabelA = Label(frame1, text="From: ",bd=6, fg="white", bg="#0B297B",font=("calibre",16, "bold")).place(x=10, y=50)
nmbr1_name = StringVar()
cmb1 = ttk.Combobox(frame1,justify="center", width=15, textvariable=nmbr1_name, font=('calibre', 16, 'bold'))
cmb1['values'] = ('Binaire', 'Decimale', 'Hexadecimale', 'Octale')
cmb1.place(x=100, y=50)
cmb1.current()
nmbr1_value = StringVar()
entry1 = Entry(frame1, width=20, textvariable=nmbr1_value,bd=6, fg='white', bg='#0B297B', font=('calibre', 16, 'bold'))
entry1.place(x=400, y=50)
LabelB = Label(frame1, text="To: ",bd=6, bg="white", fg="#0B297B",font=("calibre",16, "bold")).place(x=10, y=100)
nmbr2_name = StringVar()
cmb2 = ttk.Combobox(frame1,justify="center",width=15,textvariable=nmbr2_name, font=('calibre', 16, 'bold'))
cmb2['values'] = ('Binaire', 'Decimale', 'Hexadecimale', 'Octale')
cmb2.place(x=100, y=100)
cmb2.current()
nmbr2_value = StringVar()
entry2 = Entry(frame1, width=20, textvariable=nmbr2_value, state=DISABLED,bd=6, fg='white', bg='#0B297B', font=('calibre', 16, 'bold'))
entry2.place(x=400, y=100)
ima = PhotoImage(file="change.png")
change = Button(frame1,image=ima,command=change,bg="#8C8F82").place(x=330, y=70)
conv_btn = Button(frame1,width=15, text='Convert',command=Convert,fg="white", bg='#0B297B', bd=6, font=("calibre",13, "bold")).place(x=260, y=190)
conv_btn = Button(frame1,width=15, text='QUITER',command=quit,fg="#0B297B", bg='white', bd=6, font=("calibre",13, "bold")).place(x=260, y=240)
credit = Label(frame1, text="By EL HADDIOUI MOHAMED",bg='#8C8F82',fg="#0B297B",font=("calibre",12, "bold"),bd=6).place(x=240, y=300)

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': '#0B297B',
                                       'fieldbackground': '#0B297B',
                                       'background': '#8C8F82'
                                       }}}
                         )
# ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
combostyle.theme_use('combostyle')
window.mainloop()