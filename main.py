import time
from Bot import Bot
import math
import winsound
from sendmail import *
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


class Tipo:

    def __init__(self, mail, con, vidas=6, patron=0, acc=87):
        self.lose = self.baseb = self.racha = 0
        nombres = ["rrrr", "rbrb", "rrbr", "rbbb"]
        self.nombre = nombres[patron]
        patrones = [[0, 0, 0, 0], [0, 2], [0,0,2,0,0], [0,0,2,2], [0,2,2,2]]
        self.rb = ['d', 'n', 'k']
        self.actual = Bot(mail, con)
        self.mail = mail
        self.con = con
        self.acc = acc
        self.divisor = math.pow(2, vidas)-1
        # print(self.divisor)
        self.logica()

    def logica(self):
        time.sleep(6)
        acc = self.actual.getacc()
        fakeacc = acc
        print(acc, "accpasado")
        lose = 0
        win = False
        self.baseb = self.setbase(acc)
        b = 0
        self.wait()
        maxacc = acc
        anterior = self.color()
        print(acc, 'holaacc', acc > 0)
        while acc > 0:
            print("Nuevo Roll con: ", acc)
            b = self.setb(b, lose, self.baseb)
            fakeacc -= b
            # maxb = self.ismax(b, maxb)
            # elec = self.patron[pasada]
            # pasada += 1
            # pasada %= len(self.patron)
            elec = anterior
            if acc > 499:
                self.sendmail("Pasar a safer", "GANO")
                win = True
                break
            print("-> con ", acc, " aposto ", b, " al color: ", self.rb[elec], " acc actual: ", acc-b)
            self.bet(b, elec)
            self.wait()  # waits the result of the bet
            result = self.color()  # obtains the position of the color result
            print("salio: ", self.rb[result])
            if elec == result:
                fakeacc += b*2
                print("gano ", self.nombre, " despues de ", lose, " loses y acc actual: ", acc)
                lose = 0
            else:
                lose += 1
                print("perdio ", self.nombre, " acc actual: ", acc)
            if result == 1:
                result = anterior
            anterior = result
            acc = self.actual.getacc()
            if acc > maxacc:
                maxacc = acc
            if not fakeacc == acc:
                self.sendmail("Error de acc", f"acc = {acc}, fakeacc = {fakeacc}")
                fakeacc = acc
        if not win:
            self.sendmail(f"Perdio, {self.mail}, maxacc= {maxacc}", "hola con safer 7 min")
        winsound.Beep(frequency, duration)  # Hace un ruido

    def sendmail(self, subj, body):
        Mail(subj, body)

    def color(self):
        busc = self.actual.driver.find_elements_by_xpath("//div[@class='bonus-game-state back']")
        divs = busc[0].find_elements_by_tag_name("div")
        clase = divs[3].get_attribute("className")
        color = clase[len(clase)-1]
        if color == 'n' or color == 'o':
            return 1
        return self.conv(color)  # pasa a convertir a 0 o 2

    def wait(self):
        print("Waiting for new roll")
        time.sleep(6)
        counter = self.actual.getcounter()
        while counter != 21 and counter != 20:
            time.sleep(0.5)
            counter = self.actual.getcounter()
        print("Enough wait")

    def waitNewRoll(self):

        print("waiting new roll: ")
        sum = 0
        while sum == 0:
            # print(sum, 'suma')
            boxes = self.actual.driver.find_elements_by_xpath("//li[@data-bet-type]")
            box1 = self.getval(boxes[0])
            box2 = self.getval(boxes[1])
            box3 = self.getval(boxes[2])
            sum = box1 + box2 + box3
        while not sum == 0:
            sum = 0
            time.sleep(1)
            # print(sum, 'suma2')
            boxes = self.actual.driver.find_elements_by_xpath("//li[@data-bet-type]")
            for i in boxes:
                sum += self.getval(i)
        self.wait()
        print("Done waiting")

    def getval(self, box):

        box = box.text
        cut = box[1:]  # cuts the $ off the text to convet to float
        return int(float(cut)*100)  # converts the cut to float then to cents

    def setb(self, b, lose, baseb):  # todo basebes un self entonces se puede simplificar esta funcion
        acc = self.actual.getacc()
        if lose == 0:
            if baseb+1 == self.setbase(acc):
                print("++aumento, b = ", baseb+1)
                self.baseb += 1
                return baseb+1
            else:
                print("b queda igual")
                return baseb
        # elif lose == 1:  # safe-guard mode, gives an extra bet so that the algortihm can support one more bet, the downside is that most of the time it does not generates earnings with tiny not bets, the bright side is that you will wish to have this when you over bet, but when the bad 8 comes theres nothing you can do
        #     return baseb  # only wins with 3 in
        else:
            if b*2 <= acc:
                print("se duplica b: ", b)
                return b*2
            else:
                return 1

    def setbase(self, acc):

        # r = math.trunc(acc/127)
        # if r == 0:
        #     return 1
        return math.trunc(acc/self.divisor)

    def conv(self, b):
        return self.rb.index(b)

    def ismax(self, inp, max):
        if inp > max:
            return inp
        else:
            return max

    def bet(self, bet, elec):
        # sets b on the bet amount
        bet = str(float(bet/100))
        time.sleep(1)
        searchBar = self.actual.driver.find_elements_by_xpath("//input[@type='number']")
        betBar = searchBar[0]  # takes the element from searchBar
        betBar.clear()  # clears the bar
        betBar.send_keys(bet)  # places the bet amount

        self.actual.randwait(2)
        btn = self.actual.driver.find_elements_by_xpath("//li[@data-bet-type]")
        btn = btn[elec]
        btn.click()

        print("apostado b: ", bet)


if __name__ == "__main__":

    mail = input("mail: ")
    con = input("con: ")
    n = Tipo(mail, con)
    n.wait()
    n.logica()
