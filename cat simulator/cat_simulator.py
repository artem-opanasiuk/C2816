print("This is cat simulator")
a = input("Нажмите q если вы хотите выйти  или 1 если хотите начать:")
import random

class Cat:

    def __init__(self,name):
        self.name = name
        self.gladness = 0
        self.satiety = 0
        self.caught_mice = 0
        self.alive = True

    def to_eat(self):
        print("Я пойду покушаю")
        self.gladness += 5
        self.satiety += 5

    def to_sleep(self):
        print("Я пойду посплю")
        self.gladness += 5
        self.satiety -= 0.5

    def to_caught_mice(self):
        print("Я пойду ловить мышей")
        random_choice = random.randint(1,2)
        if random_choice == 1:
            print("==================")
            print("Ура я поймал мишку")
            self.caught_mice += 1
            self.gladness += 5
            self.satiety -= 0.5
        elif random_choice == 2:
            print("=================")
            print("Я не поймал мишку(")
            self.caught_mice += -1
            self.gladness -= 5
            self.satiety -= 0.5

    def to_pat_cat(self):
        print("Ура меня погладили")
        print("Мур мур мур мур")
        self.gladness += 5

    def is_alive(self):
        if self.gladness <= -20:
            print("Я умер от грусти...")
            self.alive = False
        elif self.satiety < -10:
            print("Я умер от голода...")
            self.alive = False
        elif self.caught_mice < -8:
            print("Я словил очень мало мишей.Я бесполезный...")
            self.alive = False
        elif self.satiety > 80:
            print("Я стал слишком толстым,вы меня перекоримили...")
            self.alive = False
        elif self.gladness > 250:
            print("Я самый радосный кот,спасибо что заботились обо мне...")
            self.alive = False
                    
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Caught mice = {self.caught_mice}")
        print(f"Satiety = {self.satiety}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + "'s life."
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_caught_mice()
        elif live_cube == 4:
            self.to_pat_cat()
        self.end_of_day()
        self.is_alive()
                
tom = Cat(name="Tom")
for day in range(365):
    try:
        if tom.alive == False:
            break
        elif str(a) == 'q':
            break
        elif int(a) == 1:
            tom.live(day)
    except ValueError:
        print("Error")
        break
    
                    
