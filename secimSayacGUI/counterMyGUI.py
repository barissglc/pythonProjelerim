import customtkinter as ctk
from random import choice

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)

        self.pos = self.start_pos
        self.in_start_pos = True

        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True


def buton_move():
    global buton_x
    buton_x += 0.001
    buton.place(relx=buton_x, rely=0.5, anchor='center')

    if buton_x < 0.9:
        window.after(10, buton_move)


def sayac():
    global sayi
    sayi += 1
    print(sayi)
    window.after(1000, sayac)


def vote(aday):
    global aday1_oy, aday2_oy
    if aday == 1:
        aday1_oy += 1
        aday1_oy_sayisi.configure(text=f"Kemal Kılıçdaroğlu Oy Sayısı: {aday1_oy}")
    elif aday == 2:
        aday2_oy += 1
        aday2_oy_sayisi.configure(text=f"Recep Tayyip Erdoğan Oy Sayısı: {aday2_oy}")

def geri_al_aday1():
    global aday1_oy
    if aday1_oy > 0:
        aday1_oy -= 1
        aday1_oy_sayisi.configure(text=f"Kemal Kılıçdaroğlu Oy Sayısı: {aday1_oy}")

def geri_al_aday2():
    global aday2_oy
    if aday2_oy > 0:
        aday2_oy -= 1
        aday2_oy_sayisi.configure(text=f"Recep Tayyip Erdoğan Oy Sayısı: {aday2_oy}")

def reset_oy_sayilari():
    global aday1_oy, aday2_oy
    aday1_oy = 0
    aday2_oy = 0
    aday1_oy_sayisi.configure(text="Kemal Kılıçdaroğlu Oy Sayısı: 0")
    aday2_oy_sayisi.configure(text="Recep Tayyip Erdoğan Oy Sayısı: 0")

def infinite_print():
    global buton_x
    buton_x += 0.5
    if buton_x < 10:
        print('infinite')
        print(buton_x)
        window.after(100, infinite_print)


window = ctk.CTk()
window.title('Seçim Pusulası')
window.geometry('600x400')

aday1_oy = 0
aday2_oy = 0

animated_panel = SlidePanel(window, 1.0, 0.7)
ctk.CTkLabel(animated_panel, text='Kemal Kılıçdaroğlu').pack(expand=True, fill='both', padx=2, pady=10)
ctk.CTkButton(animated_panel, text='Oy Ver', fg_color= 'red' ,corner_radius=0, command=lambda: vote(1)).pack(expand=True, fill='both',
                                                                                            pady=10)
ctk.CTkLabel(animated_panel, text='Recep Tayyip Erdoğan').pack(expand=True, fill='both', padx=2, pady=10)
ctk.CTkButton(animated_panel, text='Oy Ver',fg_color= 'orange', corner_radius=0, command=lambda: vote(2)).pack(expand=True, fill='both',
                                                                                            pady=10)
ctk.CTkTextbox(animated_panel, fg_color=('#dbdbdb', '#2b2b2b')).pack(expand=True, fill='both', pady=10)
reset_button = ctk.CTkButton(animated_panel, text="Oy Sayılarını Sıfırla", command=reset_oy_sayilari)
reset_button.place(relx=0.52, rely=0.80, anchor='center')

geri_al_aday1_button = ctk.CTkButton(animated_panel, text=" - ", fg_color="red", command=geri_al_aday1,
                                     corner_radius=0, width=30, height=30)
geri_al_aday1_button.place(relx=0.27, rely=0.64, anchor='center')

geri_al_aday2_button = ctk.CTkButton(animated_panel, text=" - ", fg_color="orange", command=geri_al_aday2,
                                     corner_radius=0, width=30, height=30)
geri_al_aday2_button.place(relx=0.72, rely=0.64, anchor='center')



buton_x = 0.5
buton = ctk.CTkButton(window, text='Oy Verme Ekranı için Bas', command=animated_panel.animate)
buton.place(relx=buton_x, rely=0.5, anchor='center')
#Aday 1
aday1_oy_sayisi = ctk.CTkLabel(window, text="Kemal Kılıçdaroğlu Oy Sayısı: 0")
aday1_oy_sayisi.place(relx=0.5, rely=0.8, anchor='center')
#Aday 2
aday2_oy_sayisi = ctk.CTkLabel(window, text="Recep Tayyip Erdoğan Oy Sayısı: 0")
aday2_oy_sayisi.place(relx=0.5, rely=0.9, anchor='center')




window.mainloop()
