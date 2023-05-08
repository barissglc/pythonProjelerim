import time #Pomodro uygulamamıza zaman eklemek için bunu ekledik
import threading # threadler sayesinde kodlarımızı ardaşıl olarak yürütmek yerine eş zamanlı olarak yürütebiliriz 
"""yani program çalışırken alt tab yaptığımızda bile program calısmaya devam eder. Hatta calısırken kullanıcı arayüzünde
değişiklikler yapabiliriz"""
import tkinter as tk   #GUI OLUSTURMAMIZA YARAR
from tkinter import ttk, PhotoImage #ttk ise tkinterin daha gelişmiş halidir.PhotoImage ise resim eklememize yarar

class PomodroTimer: #PomodroTimer adında bir class oluşturduk
    running = False #running adında bir değişken oluşturduk ve bunu False olarak ayarladık

    def __init__(self):
        self.pomodros = 0 #pomodros adında bir değişken oluşturduk ve bunu 0 olarak ayarladık
        #tkinter ile kullanıcı arayüzübü (GUI) oluşturduk) 
        self.root =tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Pomodro Timer")
        self.root.tk.call('wm','iconphoto', self.root._w, PhotoImage(file="coffee.png"))

        self.s = ttk.Style() 
        self.s.configure("TNotebook.Tab", font=("Ubuntu",16)) #Sekmelerin fontunu ayarladık
        self.s.configure("TButton", font=("Ubuntu",16))       #Butonların fontunu ayarladık

        self.tabs = ttk.Notebook(self.root) #Sekmeleri oluşturduk
        self.tabs.pack(fill="both",pady=10, expand=True) #Sekmeleri yerleştirdik
        
        #Sekmelerin boyutunu ayarlıyoruz
        self.tab1 = ttk.Frame(self.tabs,width=600,height=100) 
        self.tab2 = ttk.Frame(self.tabs,width=600,height=100)
        self.tab3 = ttk.Frame(self.tabs,width=600,height=100)

        self.pomodro_timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu",48)) #Burada sekmelerin içine label ekliyoruz
        #Label : etiket veya düğmenin üzerinde ne yazacağını gösterir
        self.pomodro_timer_label.pack(pady=20) 
        
        self.short_break_timer_label = ttk.Label(self.tab2, text="05:00", font=("Ubuntu",48))
        self.short_break_timer_label.pack(pady=20) #pady : labelin yukarıdan aşağıya olan uzaklığını ayarlar
        
        
        self.long_break_timer_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu",48))
        self.long_break_timer_label.pack(pady=20)

        self.tabs.add(self.tab1,text="Pomodoro") #Sekme yazısını ekledik
        self.tabs.add(self.tab2,text="Kisa Ara")
        self.tabs.add(self.tab3,text="Uzun ara")

        self.grid_layout = ttk.Frame(self.root) #Butonları eklemek için bir grid oluşturduk
        #grid yönteminde satırlar ve sutunlar ızgara gibi bölünüyor
        self.grid_layout.pack(pady=10)
        self.start_button = ttk.Button(self.grid_layout, text="Başla", command=self.start_timer_thread)
        self.start_button.grid(row=0,column=0)

        self.skip_button = ttk.Button(self.grid_layout, text="Geç", command=self.skip_clock)
        self.skip_button.grid(row=0,column=1)
        
        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.reset_clock)
        self.reset_button.grid(row=0,column=2)

        self.pomodro_counter_label = ttk.Label(self.grid_layout, text="Pomodro Sayisi:0", font=("Ubuntu",16))
        self.pomodro_counter_label.grid(row=1,column=0,columnspan=3,pady=10)

        self.root.mainloop() #GUI yi çalıştırdık

    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True   
            
            


    def start_timer(self):
        self.stopped = False
        self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) +1

        if timer_id == 1 :
            toplamZaman = 60 * 25
            while toplamZaman > 0 and not self.stopped:
                dakika,saniye = divmod(toplamZaman, 60)
                self.pomodro_timer_label.configure(text=f"{dakika:02d}:{saniye:02d}")
                self.root.update()
                time.sleep(1)
                toplamZaman = toplamZaman -1
            if not self.stopped or self.skipped:
                self.pomodros = self.pomodros + 1
                self.pomodro_counter_label.config(text=f"Pomodro Sayisi:{self.pomodros}")
                if self.pomodros % 4 == 0:
                    self.tabs.select(2)
                else:
                    self.tabs.select(1)
                self.start_timer()
        elif timer_id == 2:
            toplamZaman = 60 * 5
            while toplamZaman > 0 and not self.stopped:
                dakika,saniye = divmod(toplamZaman, 60)
                self.short_break_timer_label.configure(text=f"{dakika:02d}:{saniye:02d}")
                self.root.update()
                time.sleep(1)
                toplamZaman = toplamZaman -1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
        elif timer_id == 3:
            toplamZaman = 60 * 15
            while toplamZaman > 0 and not self.stopped:
                dakika,saniye = divmod(toplamZaman, 60)
                self.long_break_timer_label.configure(text=f"{dakika:02d}:{saniye:02d}")
                self.root.update()
                time.sleep(1)
                toplamZaman = toplamZaman -1 
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
            else:
                print("Hata oluştu") 

    def reset_clock(self):
        self.stopped = True
        self.skipped = False
        self.pomodros = 0
        self.pomodro_counter_label.config(text=f"Pomodro Sayisi:{self.pomodros}")
        self.short_break_timer_label.config(text="05:00")
        self.long_break_timer_label.config(text="15:00")
        self.pomodro_counter_label.config(text="Pomodro Sayisi:0")
        self.running = False
    def skip_clock(self):
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.pomodro_timer_label.config(text="25:00")
        elif current_tab == 1:
            self.short_break_timer_label.config(text="05:00")
        elif current_tab == 2:
            self.long_break_timer_label.config(text="15:00")

        self.stopped = True
        self.skipped = True   

    def settings(self):
        pass


PomodroTimer() #PomodroTimer classını çalıştırıyoz