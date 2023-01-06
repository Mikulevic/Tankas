import random
class Tankas():

    def __init__(self, x_kord, y_kords, kriptys="i siaure", suviai=0, suviu_siaure=0, suviu_vakarai=0, suviu_pietus=0, suviu_rytai=0, degalai=100):
        self.kriptys = kriptys
        self.suviai = suviai
        self.suviu_siaure = suviu_siaure
        self.suviu_vakarai = suviu_vakarai
        self.suviu_pietus = suviu_pietus
        self.suviu_rytai = suviu_rytai
        self.x_kords = x_kord
        self.y_kords = y_kords
        self.degalai = degalai

    def pirmyn(self):
        self.y_kords += 1
        self.kriptys = "i siaure"


    def atgal(self):
        self.y_kords -= 1
        self.kriptys = "i pietus"

    def kairen(self):
        self.x_kords -= 1
        self.kriptys = "i vakarus"


    def desinen(self):
        self.x_kords += 1
        self.kriptys = "i rytus"


    def shoot(self, target):
        print(f"Boom! Saunama {self.kriptys}")
        self.suviai += 1

        if self.kriptys == "i siaure" and self.x_kords == target.h_kord and self.y_kords < target.v_kord:
            print("Pataikei")
            tankas.degalai += 10
            self.suviu_siaure += 1
            return True


        elif self.kriptys == "i pietus" and self.x_kords == target.h_kord and self.y_kords > target.v_kord:
            print("Pataikei")
            tankas.degalai += 10
            self.suviu_rytai += 1
            return True

        elif self.kriptys == "i vakarus" and self.y_kords == target.v_kord and self.x_kords > target.h_kord:
            print("Pataikei")
            tankas.degalai += 10
            self.suviu_vakarai += 1
            return True

        elif self.kriptys == "i rytus" and self.y_kords == target.v_kord and self.x_kords < target.h_kord:
            print("Pataikei")
            tankas.degalai += 10
            self.suviu_rytai += 1
            return True

        else:
            print("Nepataikei")


    def info(self):
        return print(f"""Tanko koordinates:(x:{self.x_kords}, y:{self.y_kords})
Tanko kriptys: {self.kriptys}
Atlikta suviu: {self.suviai}
Suviu i siaure: {self.suviu_siaure}
Suviu i rytus: {self.suviu_rytai}
Suviu i vakarus: {self.suviu_vakarai}
Suviu i pietus: {self.suviu_pietus}
Degalu likutis: {self.degalai}
""")

class Target():
    def __init__(self):
        self.h_kord = random.randint(0, 10)
        self.v_kord = random.randint(0, 10)

    def inf(self):
        print(f"""Taikinys: (x:{self.h_kord}, y:{self.v_kord}) """)


tankas = Tankas(0, 0)
target = Target()


while True:


    target.inf()
    tankas.info()

    veiksmas = input("Pasirinkite veiksma(w, s, a, d) ")
    suvis = input("Ar norite sauti? (y/n) ")


    if veiksmas == "w":
        tankas.pirmyn()
        tankas.degalai -= 10
    if veiksmas == "s":
        tankas.atgal()
        tankas.degalai -= 10
    if veiksmas == "a":
        tankas.kairen()
        tankas.degalai -= 10
    if veiksmas == "d":
        tankas.desinen()
        tankas.degalai -= 10
    if suvis == "y":
        if tankas.shoot(target) == True:
            target = Target()
    if suvis == "n":
        pass
    if tankas.degalai == 0:
        print("Degalai pasibaige")
        tankas.info()
        break