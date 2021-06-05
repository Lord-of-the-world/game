import requests as rq
import tkinter as tk
import random
import _thread
import time


class Visuals_Entry:
    def __init__(self):
        self.root = tk.Tk()
        self.enter_l = tk.Label(text = 'Введите ваш ник')
        self.nick = tk.Entry(width=24)
        self.enter = tk.Button(text='Вход', width=20)
        self.enter.bind("<Button-1>", self.new_player) 
        self.enter_l.pack(side=tk.TOP)
        self.nick.pack(side=tk.TOP)
        self.enter.pack(side=tk.TOP)
        
        
    def incorrect_nickname(self):
        self.enter_l['text'] = 'Имя пользователя занято'
        self.enter_l['fg'] = 'red'

    def inncorrect_room_key(self):
        self.room_l['text'] = 'Неверный ключ'
        self.room_l['fg'] = 'red'

    def new_player(self, event):
        nick = self.nick.get()
        entry.nickname(nick)

    def welcome(self):
        self.nick.pack_forget()
        self.enter.pack_forget()
        self.w_l = tk.Label(text='Добро пожаловать в "Lord of the world"')
        self.w_e = tk.Button(text='Вход в комнату')
        self.w_e.bind("<Button-1>", self.entry_room_v)
        self.w_c = tk.Button(text='Создание комнаты')
        self.w_c.bind("<Button-1>", entry.new_room)
        self.w_l.pack()
        self.w_e.pack()
        self.w_c.pack()

    def welcome_back(self, event):
        self.room_id_v.pack_forget()
        self.room_enter_v.pack_forget()
        self.w_back.pack_forget()
        self.room_l.pack_forget()
        self.welcome()

    def entry_room_v(self, event):
        self.w_l.pack_forget()
        self.w_e.pack_forget()
        self.w_c.pack_forget()
        self.room_l = tk.Label(text = 'Введите ключ')
        self.room_id_v = tk.Entry()
        self.room_enter_v = tk.Button(text = 'Вход')
        self.room_enter_v.bind("<Button-1>", self.entry_room_s)
        self.w_back = tk.Button(text='Назад')
        self.w_back.bind("<Button-1>", self.welcome_back)
        self.room_l.pack()
        self.room_id_v.pack()
        self.room_enter_v.pack()
        self.w_back.pack()

    def entry_room_s(self, event):
        key = self.room_id_v.get()
        entry.entry_room(key)





    # def lobby(self, pl):
    #     players = tk.Label(text = pl)
        



        


class Entry:
    def __init__(self):
        pass
    def nickname(self, nick):
        self.nicknames = nick
        req = rq.get(f'http://sham13namo.pythonanywhere.com/n_p?login={self.nicknames}')
        answer = req.text
        print(answer)
        if answer == '0':
            visual_entry.enter_l.pack_forget()
            visual_entry.nick.pack_forget()
            visual_entry.enter.pack_forget()
            visual_entry.welcome()
        else:
            visual_entry.incorrect_nickname()
            print('Nickname already used')
        


    def entry_room(self, key):
        self.room_key = key
        req = rq.get(f'http://sham13namo.pythonanywhere.com/c_g?login={self.nicknames}&id_room={self.room_key}')
        answer = req.text
        print(answer)
        if answer == '0':
            print('Done')
            # visual_entry.lobby()
        else:
            print('Incorrect room key')     
            visual_entry.inncorrect_room_key()


    def new_room(self):
        while True:
            key = random.randrange(1000, 10000)
            req = rq.get(f'http://sham13namo.pythonanywhere.com/n_r?id={key}')
            answer = req.text
            print(answer)
            if answer == '0':
                print('Incorrect room key')
            else:
                print(answer)
                # visual_entry.lobby()
                break


    # def game_start(self):
    #     visual_gameplay.root.mainloop()

    # def get_players(self):
    #     while True:
    #         req = rq.get(f'http://sham13namo.pythonanywhere.com/g_p?id={key}')
    #         self.pl = req.text
                

             


    # def team_room(self):
    #     while True:
    #         self.team = input('team>> ')
    #         req = rq.get(f'http://sham13namo.pythonanywhere.com/c_t?team={self.team}')
    #         answer = req.text
    #         print(answer)
    #         if answer == '0':
    #             print('Done')
    #             break
    #         else:
    #             print('Team is full')







class Visuals_Gameplay:
    def __init__(self):
        self.team = 'ru'
        self.root = tk.Tk()
        
        

        # countries -----------

        
        self.money_v = tk.Label(text='деньги: 500')
        self.bomb_v = tk.Label(text='бомбы: 0')
        self.money_v.grid(row=0, column=1)
        self.bomb_v.grid(row=1, column=1)
        self.countries_f = tk.Frame(bg= '#fff86e')
        self.countries = tk.Label(master= self.countries_f, text = 'Страны', bg= '#fff86e')
        self.russia = tk.Label(master= self.countries_f, text = 'Россия', bg= '#fff86e')
        self.russia_1 = tk.Label(master= self.countries_f, text= 'Москва', bg= '#fff86e')
        self.russia_2 = tk.Label(master= self.countries_f, text= 'Санкт-Петербург', bg= '#fff86e')
        self.russia_3 = tk.Label(master= self.countries_f, text= 'Новосибирск', bg= '#fff86e')
        self.usa = tk.Label(master= self.countries_f, text= 'Америка', bg= '#fff86e')
        self.usa_1 = tk.Label(master= self.countries_f, text= 'Вашингтон', bg= '#fff86e')
        self.usa_2 = tk.Label(master= self.countries_f, text= 'Нью-Йорк', bg= '#fff86e')
        self.usa_3 = tk.Label(master= self.countries_f, text= 'Лос-Анджелис', bg= '#fff86e')
        self.german = tk.Label(master= self.countries_f, text= 'Германия', bg= '#fff86e')
        self.german_1 = tk.Label(master= self.countries_f, text= 'Берлин', bg= '#fff86e')
        self.german_2 = tk.Label(master= self.countries_f, text= 'Гамбург', bg= '#fff86e')
        self.german_3 = tk.Label(master= self.countries_f, text= 'Мюнхен', bg= '#fff86e')
        self.countries_f.grid()


        self.countries.grid(row=0, column=1)
        self.russia.grid(row=1, column=0)
        self.russia_1.grid(row=2, column=0)
        self.russia_2.grid(row=3, column=0)
        self.russia_3.grid(row=4, column=0)
        self.usa.grid(row=1, column=1)
        self.usa_1.grid(row=2, column=1)
        self.usa_2.grid(row=3, column=1)
        self.usa_3.grid(row=4, column=1)
        self.german.grid(row=1, column=2)
        self.german_1.grid(row=2, column=2)
        self.german_2.grid(row=3, column=2)
        self.german_3.grid(row=4, column=2)

        # upgrade -------------

        self.up = tk.Label(text= 'Улучшения')
        if self.team == 'ru':
            self.up_1 = tk.Button(text= 'Москва') 
            self.up_2 = tk.Button(text= 'Санкт-Петербург')
            self.up_3 = tk.Button(text= 'Новосибирск')
        elif self.team == 'usa':
            self.up_1 = tk.Button(text= 'Вашингтон') 
            self.up_2 = tk.Button(text= 'Нью-Йорк')
            self.up_3 = tk.Button(text= 'Лос-Анджелис')       
        else:
            self.up_1 = tk.Button(text= 'Берлин')
            self.up_2 = tk.Button(text= 'Гамбург')
            self.up_3 = tk.Button(text= 'Мюнхен')

        self.up_1.bind('<Button-1>', lambda event, text=1: gameplay.upgrade(event, text))
        self.up_2.bind('<Button-1>', lambda event, text=2: gameplay.upgrade(event, text))
        self.up_3.bind('<Button-1>', lambda event, text=3: gameplay.upgrade(event, text))
        self.up.grid(row=6, column=0)
        self.up_1.grid(row=7, column=0)
        self.up_2.grid(row=8, column=0)
        self.up_3.grid(row=9, column=0)

        # Bomb open ----------

        self.open = tk.Button(text= 'открытие бомбы')
        self.open.bind('<Button-1>', gameplay.bomb_open)
        self.open.grid(row=7, column=2)

        # Shields -----------

        self.shield = tk.Label(text = 'Защитить город')
        if self.team == 'ru':
            self.shield_1 = tk.Button(text = 'Москва')
            self.shield_2 = tk.Button(text = 'Санкт-Петербург')
            self.shield_3 = tk.Button(text = 'Новосибирск')
        elif self.team == 'usa':
            self.shield_1 = tk.Button(text = 'Вашингтон')
            self.shield_2 = tk.Button(text = 'Нью-Йорк')
            self.shield_3 = tk.Button(text = 'Лос_Анджелис')
        else:
            self.shield_1 = tk.Button(text = 'Берлин')
            self.shield_2 = tk.Button(text = 'Гамбург')
            self.shield_3 = tk.Button(text = 'Мюнхен')
        self.shield_1.bind('<Button-1>', lambda event, text=1: gameplay.shield_create(event, text))
        self.shield_2.bind('<Button-1>', lambda event, text=2: gameplay.shield_create(event, text))
        self.shield_3.bind('<Button-1>', lambda event, text=3: gameplay.shield_create(event, text))
        self.shield.grid(row=6, column=1)
        self.shield_1.grid(row=7, column=1)        
        self.shield_2.grid(row=8, column=1)
        self.shield_3.grid(row=9, column=1)


        timer = 3600
        self.time_label = tk.Label(self.root, font=('',15))
        current_time = time.time()
        _thread.start_new_thread(self.update,(current_time, current_time, timer))

        self.time_label.grid(row=9, column=9)

    
    def change(self):
        self.open['text'] = 'создание бомбы'
        self.open.bind('<Button-1>', gameplay.bobm_create)

    def attack(self):
        self.choise = tk.Label(text='Выберите город для уничтожения')
        if self.team == 'ru':
            self.attack_1 = tk.Button(text= 'Вашингтон', command=lambda: gameplay.bomb_use('4'))
            self.attack_2 = tk.Button(text= 'Нью-Йорк', command=lambda: gameplay.bomb_use('5'))
            self.attack_3 = tk.Button(text= 'Лос-Анджелис', command=lambda: gameplay.bomb_use('6'))
            self.attack_4 = tk.Button(text= 'Берлин', command=lambda: gameplay.bomb_use('7'))
            self.attack_5 = tk.Button(text= 'Гамбург', command=lambda: gameplay.bomb_use('8'))
            self.attack_6 = tk.Button(text= 'Мюнхен', command=lambda: gameplay.bomb_use('9'))
        elif self.team == 'usa':
            self.attack_1 = tk.Button(text= 'Москва', command=lambda: gameplay.bomb_use('1'))
            self.attack_2 = tk.Button(text= 'Санкт-Петербург', command=lambda: gameplay.bomb_use('2'))
            self.attack_3 = tk.Button(text= 'Новосибирск', command=lambda: gameplay.bomb_use('3'))
            self.attack_4 = tk.Button(text= 'Берлин', command=lambda: gameplay.bomb_use('7'))
            self.attack_5 = tk.Button(text= 'Гамбург', command=lambda: gameplay.bomb_use('8'))
            self.attack_6 = tk.Button(text= 'Мюнхен', command=lambda: gameplay.bomb_use('9'))
        else:
            self.attack_1 = tk.Button(text= 'Москва', command=lambda: gameplay.bomb_use('1'))
            self.attack_2 = tk.Button(text= 'Санкт-Петербург', command=lambda: gameplay.bomb_use('2'))
            self.attack_3 = tk.Button(text= 'Новосибирск', command=lambda: gameplay.bomb_use('3'))
            self.attack_4 = tk.Button(text= 'Вашингтон', command=lambda: gameplay.bomb_use('4'))
            self.attack_5 = tk.Button(text= 'Нью-Йорк', command=lambda: gameplay.bomb_use('5'))
            self.attack_6 = tk.Button(text= 'Лос-Анджелис', command=lambda: gameplay.bomb_use('6'))
        self.choise.grid(row=6, column=3)
        self.attack_1.grid(row=7, column=3)        
        self.attack_2.grid(row=8, column=3)
        self.attack_3.grid(row=9, column=3)
        self.attack_4.grid(row=7, column=4)
        self.attack_5.grid(row=8, column=4)
        self.attack_6.grid(row=9, column=4)


    def shield_v(self):
        if gameplay.city1['shield'] == '1':
            if self.team == 'ru':
                self.shield_1['text'] = 'Москва(щит)'
            elif self.team == 'usa':
                self.shield_1['text'] = 'Вашингтон(щит)'
            else:
                self.shield_1['text'] = 'Берлин(щит)'
        if gameplay.city2['shield'] == '1':
            if self.team == 'ru':
                self.shield_2['text'] = 'Санкт-Петербург(щит)'
            elif self.team == 'usa':
                self.shield_2['text'] = 'Нью-Йорк(щит)'
            else:
                self.shield_2['text'] = 'Гамбург(щит)'
        if gameplay.city3['shield'] == '1':
            if self.team == 'ru':
                self.shield_3['text'] = 'Новосибирск(щит)'
            elif self.team == 'usa':
                self.shield_3['text'] = 'Лос-Анджелис(щит)'
            else:
                self.shield_3['text'] = 'Мюнхен(щит)'

    def bombs_hide(self):
        self.choise.grid_forget()
        self.attack_1.grid_forget()        
        self.attack_2.grid_forget()
        self.attack_3.grid_forget()
        self.attack_4.grid_forget()
        self.attack_5.grid_forget()
        self.attack_6.grid_forget()


    def money_change(self, money):
        self.money_v['text'] = f'деньги: {money}'
    def bombs_change(self, bombs):
        self.bomb_v['text'] = f'бомбы: {bombs}'

    def convert(self, seconds):
        min, sec = divmod(seconds, 60)

        hour, min = divmod(min, 60)

        return "%d:%02d:%02d" % (hour, min, sec)

    def update(self, start_time, current_time, timer):
        timer_now = timer
        while current_time <= timer+start_time:
            now = time.time()
            if now-current_time >= 1:
                self.time_label['text'] = str(self.convert(timer_now))
                current_time = now
                timer_now -= 1
                gameplay.money += 10
                money = gameplay.money
                self.money_change(money)
        else:
            self.time_label['text'] = 'ALARM!!!!!'


    



    


class Gameplay:
    def __init__(self):
        self.team = 'ru'
        self.money = 500
        self.bombs = 0
        self.technology = 0
        self.city1 = {'be': '1', 'lvl': 1, 'shield': '0'}
        self.city2 = {'be': '1', 'lvl': 1, 'shield': '0'}
        self.city3 = {'be': '1', 'lvl': 1, 'shield': '0'}

    def upgrade(self, event, text):
        if text == 1:
            if self.money < self.city1['lvl'] * 100:
                print("Don't enough money")
            else:
                self.money -= self.city1['lvl'] * 100
                self.city1['lvl'] += 1 
                rq.get(f"http://sham13namo.pythonanywhere.com/sdt_in?level={self.city1['lvl']}&shield={self.city1['shield']}")
        elif text == 2:
            if self.money < self.city2['lvl'] * 100:
                print("Don't enough money")
            else:
                self.money -= self.city2['lvl'] * 100
                self.city2['lvl'] += 1
                rq.get(f"http://sham13namo.pythonanywhere.com/sdt_in?level={self.city2['lvl']}&shield={self.city2['shield']}")
        else:
            if self.money < self.city3['lvl'] * 100:
                print("Don't enough money")
            else:
                self.money -= self.city3['lvl'] * 100
                self.city3['lvl'] += 1
                rq.get(f"http://sham13namo.pythonanywhere.com/sdt_in?level={self.city3['lvl']}&shield={self.city3['shield']}")
        money = self.mone     

    def bomb_open(self, event):
        if self.money < 300:
            print("Don't enough money")
        else:
            self.money -= 300
            
            self.technology = 1
            rq.get(f"http://sham13namo.pythonanywhere.com/sd_in?money={self.money}&bombs={self.bombs}&city={'0'}&country={self.team}&isopen={self.technology}")
            visual_gameplay.change()
            print('Done')

    def bobm_create(self, event):
        if self.money < 200:
            print("Don't enough money")
        else:
            self.money -= 200
            self.bombs += 1
            
            
            bombs = self.bombs
            visual_gameplay.bombs_change(bombs)
            rq.get(f"http://sham13namo.pythonanywhere.com/sd_in?money={self.money}&bombs={self.bombs}&city={'0'}&country={self.team}&isopen={self.technology}")
            visual_gameplay.attack()
            print('Done')

    def bomb_use(self, text):
        if self.bombs < 1:
            print("Don't enough bombs")
        else:
            self.bombs -= 1
            bombs = self.bombs
            visual_gameplay.bombs_change(bombs)
            if bombs < 1:
                visual_gameplay.bombs_hide()
            rq.get(f"http://sham13namo.pythonanywhere.com/sd_in?money={self.money}&bombs={self.bombs}&city={'0'}&country={self.team}&isopen={self.technology}")
            rq.get(f"http://sham13namo.pythonanywhere.com/b_u?city={text}")
            print('Done')  
    
    def shield_create(self, event, text):
        print(text)
        if self.money < 150:
            print("Don't enough money")
        else:
            if text == 1:
                if self.city1['shield'] == '1':
                    print("Yo've already have a shield")
                else:
                    self.money -= 150                   
                    self.city1['shield'] = '1'
                    visual_gameplay.shield_v()
                    rq.get(f"http://sham13namo.pythonanywhere.com/sdt_in?level={self.city1['lvl']}&shield={self.city1['shield']}")
            elif text == 2:
                if self.city2['shield'] == '1':
                    print("Yo've already have a shield")
                else:
                    self.money -= 150
                    self.city2['shield'] = '1'
                    visual_gameplay.shield_v()
                    rq.get(f"http://sham13namo.pythonanywhere.com/sdt_in?level={self.city2['lvl']}&shield={self.city2['shield']}")
            else:
                if self.city3['shield'] == '1':
                    print("Yo've already have a shield")
                else:
                    self.money -= 150
                    self.city3['shield'] = '1'
                    visual_gameplay.shield_v()
                    rq.get(f"http://sham13namo.pythonanywhere.com/sdt_in?level={self.city3['lvl']}&shield={self.city3['shield']}")




entry = Entry()
visual_entry = Visuals_Entry()
visual_entry.root.mainloop()

gameplay = Gameplay()
visual_gameplay = Visuals_Gameplay()
visual_gameplay.root.mainloop()