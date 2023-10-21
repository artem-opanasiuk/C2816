import random
import logging
logging.basicConfig(level=logging.DEBUG)
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None,hobby=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.hobby = hobby
        self.health = 0


    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
        
    def get_hobby(self):
        self.hobby = Hobby(hobby_list)
        
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 10
        
    def to_get_hobby(self):
        self.gladness += self.hobby.gladness_plus
        self.satiety -= 10
        self.health += 10
        self.money -= 20
        
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "sweets":
            print("Yummy yummy!")
            self.money -= 15
            self.satiety += 2
            self.gladness += 10

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        self.health -= 10

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name} 's life "
        print(f"{day:=^50}", "\n")
        logging.info("Info:")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
        hobby_indexes = "Hobby indexes"
        print(f"{hobby_indexes:^50}", "\n")
        print(f"Health - {self.hobby.health}")
        print(f"Gladness_plus - {self.hobby.gladness_plus}")

    def is_alive(self):
        if self.gladness < 30:
            print("Depression…")
            logging.critical("Depression")
            return False
        if self.satiety < 40:
            print("Died of hunger")
            logging.critical("Died of hunger")
            return False
        if self.money < 70:
            print("Bankrupt…")
            logging.critical("Bankrupt…")
            return False
        if self.health < -10:
            print("I am weak")
            logging.critical("I am weak")
            return False
        
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with salary {self.job.salary}")
        if self.hobby is None:
            self.get_hobby()
            print(f"I am not fit so i am gonna play {self.hobby.hobby}")
           
           
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…\n So I will clean the house ")
                self.clean_home()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.health < 0:
            self.get_hobby()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="sweets")


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}

}


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car can not move")
            return False


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1}
}


class Job:
    def __init__(self, list_of_jobs):
        self.job = random.choice(list(list_of_jobs))
        self.salary = list_of_jobs[self.job]["salary"]
        self.gladness_less = list_of_jobs[self.job]["gladness_less"]

hobby_list = {
    "tennis": {"health":20, "gladness_plus":10},
    "basketball": {"health":40, "gladness_plus":20},
    "voleyball": {"health":50, "gladness_plus":30},
    "footbal": {"health":30, "gladness_plus":15}
    }
class Hobby:
    def __init__(self, hobby_list):
        self.hobby = random.choice(list(hobby_list))
        self.health = hobby_list[self.hobby]["health"]
        self.gladness_plus = hobby_list[self.hobby]["gladness_plus"]
        
nick = Human(name="Nick")
for day in range(1, 8):
    if nick.live(day) == False:
        break
    elif day == 7:
        print("=========================================================")
        print("Congratulations, you have successfully completed the game.")
        logging.debug("Congratulations")
