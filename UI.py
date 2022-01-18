from tkinter import *
Gui= Tk()
canvas= Canvas(Gui, height=450, width=750)
canvas.pack()

ust_frame= Frame(Gui, bg="cyan")
ust_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)


altsol_frame= Frame(Gui, bg="cyan")
altsol_frame.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)


sagalt_frame= Frame(Gui, bg="cyan")
sagalt_frame.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)


hatirlatma_etiket= Label(ust_frame, bg= "cyan", text ="ŞİFLEME", font="Verdana 12 bold")

hatirlatma_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_opsiyon= StringVar(ust_frame)
hatirlatma_opsiyon.set("Seçiniz")
hatirlatma_acılırmenu=OptionMenu(
    ust_frame, 
    hatirlatma_opsiyon,
    "mesajını şifrele",
    "şifreli mesajını çevir" )
hatirlatma_acılırmenu.pack(padx=10, pady=10, side=LEFT)





Gui.mainloop()

