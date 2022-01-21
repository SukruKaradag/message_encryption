from tkinter import *
from tkcalendar import DateEntry
Gui= Tk()
canvas= Canvas(Gui, height=450, width=750)
canvas.pack()

ust_frame= Frame(Gui, bg="cyan")
ust_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)


altsol_frame= Frame(Gui, bg="cyan")
altsol_frame.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)


sagalt_frame= Frame(Gui, bg="cyan")
sagalt_frame.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)


hatirlatma_etiket= Label(ust_frame, bg= "cyan", text ="hatırlatma_tipi", font="Verdana 12 bold")

hatirlatma_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_opsiyon= StringVar(ust_frame)
hatirlatma_opsiyon.set("Seçiniz")
hatirlatma_acılırmenu=OptionMenu(
    ust_frame, 
    hatirlatma_opsiyon,
    "mesajını şifrele",
    "şifreli mesajını çevir" ) 
hatirlatma_acılırmenu.pack(padx=10, pady=10, side=LEFT)


hatırlatma_tarih_secici=DateEntry(ust_frame, width=12, background="orange", foreground="black", borderwidth=1, locale="de_DE" )
hatırlatma_tarih_secici._top_cal.overrideredirect(False)
hatırlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)

hatirlatma_tarihi= Label(ust_frame, bg= "cyan", text ="hatırlatma_tarihi", font="Verdana 12 bold")

hatirlatma_tarihi.pack(padx=10, pady=10, side=LEFT)


#part II
Label(altsol_frame, text="hatırlatma yöntemi", bg="cyan", font="Verdana 10 bold").pack(padx=10, pady=10, anchor=NW)




Gui.mainloop()

