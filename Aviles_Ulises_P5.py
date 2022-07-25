from time import sleep
from keyboard import is_pressed
from random import randint, seed
from os import system
system('cls')
seed()
deckShuf = []
money = 500


def shuffle():
    deckOrd = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q',
               'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
    global deckShuf
    deckShuf = []
    for i in deckOrd:
        while True:
            pos = randint(0, 51)
            if deckOrd[pos] != '':
                deckShuf.append(deckOrd[pos])
                deckOrd[pos] = ''
                break


def Sum(hand=[]):
    r = 0
    NAs = 0
    for i in hand:
        if i == 'A':
            NAs += 1
        elif i in ['2', '3', '4', '5', '6', '7', '8', '9']:
            r += int(i)
        elif i in ['X', 'J', 'Q', 'K']:
            r += 10
    for i in range(NAs):
        if (r+11) > 21:
            r += 1
        else:
            r += 11
    return r


class Player:
    def __init__(self, deckShuffled=[], bet1=500):
        self.Hand1 = []
        self.Hand2 = []
        self.Hand3 = []
        self.Hand4 = []
        self.Dealler = []
        for i in range(len(deckShuffled)):
            if i < 10:
                self.Hand1.append(deckShuffled[i])
            elif i > 10 and i < 20:
                self.Hand2.append(deckShuffled[i])
            elif i > 20 and i < 30:
                self.Hand3.append(deckShuffled[i])
            elif i > 30 and i < 40:
                self.Hand4.append(deckShuffled[i])
            elif i > 40 and i < 50:
                self.Dealler.append(deckShuffled[i])
        self.Hands = [[self.Hand1, [self.Hand1[0], self.Hand1[1]], bet1, []], [self.Hand2, [], 0, []], [
            self.Hand3, [], 0, []], [self.Hand4, [], 0, []], [self.Dealler, [self.Dealler[0], ' ']]]
        self.NHands = 1

    def Read(self):
        for i in range(self.NHands):
            self.Hands[i][3].clear()
            if len(self.Hands[i][1]) == 2:
                self.Hands[i][3].append('X')
            if Sum(self.Hands[i][1]) < 21:
                self.Hands[i][3].append('H')
            if len(self.Hands[i][1]) == 2 and Sum(self.Hands[i][1]) != 21 and money >= (2*self.Hands[i][2]):
                self.Hands[i][3].append('D')
            if len(self.Hands[i][1]) == 2 and self.Hands[i][1][0] == self.Hands[i][1][1] and money >= (self.Hands[0][2]+self.Hands[1][2]+self.Hands[2][2]+self.Hands[3][2]):
                # if len(self.Hands[i][1])==2 and money>(self.Hands[0][2]+self.Hands[1][2]+self.Hands[2][2]+self.Hands[3][2]):
                self.Hands[i][3].append('2')
            if self.Hands[4][1][0] == 'A':
                self.Hands[i][3].append('I')

    def Hit(self, hand=0):
        a = self.Hands[hand][0][len(self.Hands[hand][1])]
        sleep(0.2)
        self.Hands[hand][1].append(a)

    def split(self, NHand):
        self.Hands[self.NHands][1].append(self.Hands[self.NHands][0][0])
        self.Hands[self.NHands][1].append(self.Hands[self.NHands][0][1])
        a = self.Hands[self.NHands][1][0]
        self.Hands[self.NHands][1][0] = self.Hands[NHand][1][1]
        self.Hands[NHand][1][1] = a
        self.NHands += 1


def setBet(case=True):
    global money
    if case == True:
        bet = input(
            '\033[1;37;48mYou have : \033[1;33;48m {} \033[1;37;48m Cetys Dollars\nAmount to bet: '.format(money))
        try:
            if int(bet) <= money and int(bet) > 0:
                return int(bet)
        except:
            pass
    else:
        a = money-player.Hands[0][2]-player.Hands[1][2] - \
            player.Hands[2][2]-player.Hands[3][2]
        bet = input(
            '\033[1;37;48mYou have : \033[1;33;48m {} \033[1;37;48m Cetys Dollars\nAmount to bet: '.format(a))
        try:
            if int(bet) <= a and int(bet) > 0:
                return int(bet)
        except:
            pass


def display():
    system('cls')
    print(
        '\033[1;33;48m       |Casino Cetys|\033[1;37;48m\n============Dealer===========')
    if len(player.Hands[4][1]) == 2:
        print(' ___   ___\n|   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___|\n'.format(
            player.Hands[4][1][0], player.Hands[4][1][1]))
    elif len(player.Hands[4][1]) == 3:
        print(' ___   ___   ___\n|   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___|\n'.format(
            player.Hands[4][1][0], player.Hands[4][1][1], player.Hands[4][1][2]))
    elif len(player.Hands[4][1]) == 4:
        print(' ___   ___   ___   ___ \n|   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___|\n'.format(
            player.Hands[4][1][0], player.Hands[4][1][1], player.Hands[4][1][2], player.Hands[4][1][3]))
    elif len(player.Hands[4][1]) == 5:
        print(' ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___|'.format(
            player.Hands[4][1][0], player.Hands[4][1][1], player.Hands[4][1][2], player.Hands[4][1][3], player.Hands[4][1][4]))
    elif len(player.Hands[4][1]) == 6:
        print(' ___   ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___| |___|'.format(
            player.Hands[4][1][0], player.Hands[4][1][1], player.Hands[4][1][2], player.Hands[4][1][3], player.Hands[4][1][4], player.Hands[4][1][5]))
    elif len(player.Hands[4][1]) == 7:
        print(' ___   ___   ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___| |___| |___|'.format(
            player.Hands[4][1][0], player.Hands[4][1][1], player.Hands[4][1][2], player.Hands[4][1][3], player.Hands[4][1][4], player.Hands[4][1][5], player.Hands[4][1][6]))
    elif len(player.Hands[4][1]) == 8:
        print(' ___   ___   ___   ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___| |___| |___| |___|'.format(
            player.Hands[4][1][0], player.Hands[4][1][1], player.Hands[4][1][2], player.Hands[4][1][3], player.Hands[4][1][4], player.Hands[4][1][5], player.Hands[4][1][6], player.Hands[4][1][7]))
    elif len(player.Hands[4][1]) == 9:
        print(' ___   ___   ___   ___   ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___| |___| |___| |___| |___|'.format(
            player.Hands[4][1][0], player.Hands[4][1][1], player.Hands[4][1][2], player.Hands[4][1][3], player.Hands[4][1][4], player.Hands[4][1][5], player.Hands[4][1][6], player.Hands[4][1][7], player.Hands[4][1][8]))
    elif len(player.Hands[4][1]) == 10:
        print(' ___   ___   ___   ___   ___   ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   | |   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___| |___| |___| |___| |___| |___|'.format(
            player.Hands[4][1][0], player.Hands[4][1][1], player.Hands[4][1][2], player.Hands[4][1][3], player.Hands[4][1][4], player.Hands[4][1][5], player.Hands[4][1][6], player.Hands[4][1][7], player.Hands[4][1][8], player.Hands[4][1][9]))
    print(
        '\n============Player============\n\033[1;33;48m${}\033[1;37;48mCetysDollars'.format(money))
    for i in range(player.NHands):
        print('Deck {}({}) Bet: {}'.format(
            i+1, Sum(player.Hands[i][1]), player.Hands[i][2]))
        if len(player.Hands[i][1]) == 2:
            print(' ___   ___\n|   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___|\n'.format(
                player.Hands[i][1][0], player.Hands[i][1][1]))
        elif len(player.Hands[i][1]) == 3:
            print(' ___   ___   ___\n|   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___|\n'.format(
                player.Hands[i][1][0], player.Hands[i][1][1], player.Hands[i][1][2]))
        elif len(player.Hands[i][1]) == 4:
            print(' ___   ___   ___   ___ \n|   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___|\n'.format(
                player.Hands[i][1][0], player.Hands[i][1][1], player.Hands[i][1][2], player.Hands[i][1][3]))
        elif len(player.Hands[i][1]) == 5:
            print(' ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___|'.format(
                player.Hands[i][1][0], player.Hands[i][1][1], player.Hands[i][1][2], player.Hands[i][1][3], player.Hands[i][1][4]))
        elif len(player.Hands[i][1]) == 6:
            print(' ___   ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___| |___|'.format(
                player.Hands[i][1][0], player.Hands[i][1][1], player.Hands[i][1][2], player.Hands[i][1][3], player.Hands[i][1][4], player.Hands[i][1][5]))
        elif len(player.Hands[i][1]) == 7:
            print(' ___   ___   ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___| |___| |___|'.format(
                player.Hands[i][1][0], player.Hands[i][1][1], player.Hands[i][1][2], player.Hands[i][1][3], player.Hands[i][1][4], player.Hands[i][1][5], player.Hands[i][1][6]))
        elif len(player.Hands[i][1]) == 8:
            print(' ___   ___   ___   ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___| |___| |___| |___|'.format(
                player.Hands[i][1][0], player.Hands[i][1][1], player.Hands[i][1][2], player.Hands[i][1][3], player.Hands[i][1][4], player.Hands[i][1][5], player.Hands[i][1][6], player.Hands[i][1][7]))
        elif len(player.Hands[i][1]) == 9:
            print(' ___   ___   ___   ___   ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___| |___| |___| |___| |___|'.format(
                player.Hands[i][1][0], player.Hands[i][1][1], player.Hands[i][1][2], player.Hands[i][1][3], player.Hands[i][1][4], player.Hands[i][1][5], player.Hands[i][1][6], player.Hands[i][1][7], player.Hands[i][1][8]))
        elif len(player.Hands[i][1]) == 10:
            print(' ___   ___   ___   ___   ___   ___   ___   ___   ___   ___\n|   | |   | |   | |   | |   | |   | |   | |   | |   | |   |\n| \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m | | \033[1;33;48m{}\033[1;37;48m |\n|___| |___| |___| |___| |___| |___| |___| |___| |___| |___|'.format(
                player.Hands[i][1][0], player.Hands[i][1][1], player.Hands[i][1][2], player.Hands[i][1][3], player.Hands[i][1][4], player.Hands[i][1][5], player.Hands[i][1][6], player.Hands[i][1][7], player.Hands[i][1][8], player.Hands[i][1][9]))


def displayOptions(NHand=0):
    player.Read()
    print('\nOptions for Hand{}'.format(NHand+1))
    print('[1] Rules\n[X] Surrender\n[S] Stand')
    for i in player.Hands[NHand][3]:
        if i == 'H':
            print('[H] Hit')
        if i == 'D':
            print('[D] Double Down')
        if i == '2':
            print('[2] Split')
        if i == 'I':
            print('[I] Insurance')


def opc():
    while True:
        if is_pressed('1'):
            return '1'
        elif is_pressed('X'):
            return 'X'
        elif is_pressed('S'):
            return 'S'
        elif is_pressed('H'):
            return 'H'
        elif is_pressed('D'):
            return 'D'
        elif is_pressed('2'):
            return '2'
        elif is_pressed('I'):
            return 'I'


def gameEnded():
    a = 0
    for i in range(player.NHands):
        if Sum(player.Hands[i][1]) > 21:
            a += 1
    if a < player.NHands:
        player.Hands[4][1][1] = player.Hands[4][0][1]
        while Sum(player.Hands[4][1]) < 17:
            player.Hit(4)


def displayResults():
    global money
    global player
    a = money
    for i in range(player.NHands):
        if surrender[i] == True:
            print('\033[1;31;48m Deck{} lost {} vs the dealer\033[1;37;48m'.format(
                i+1, ((player.Hands[i][2])*0.5)))
            money -= ((player.Hands[i][2])*0.5)
        else:
            if Sum(player.Hands[i][1]) > 21:
                print('\033[1;31;48m Deck{} lost {} vs the dealer\033[1;37;48m'.format(
                    i+1, player.Hands[i][2]))
                money -= player.Hands[i][2]
            else:
                if Sum(player.Hands[i][1]) > Sum(player.Hands[4][1]) or Sum(player.Hands[i][1]) <= 21 and Sum(player.Hands[4][1]) > 21:
                    print('\033[1;32;48m Deck{} won {} vs the dealer!\033[1;37;48m'.format(
                        i+1, player.Hands[i][2]))
                    money += player.Hands[i][2]
                elif Sum(player.Hands[i][1]) < Sum(player.Hands[4][1]) and Sum(player.Hands[4][1]) <= 21:
                    print('\033[1;31;48m Deck{} lost {} vs the dealer\033[1;37;48m'.format(
                        i+1, player.Hands[i][2]))
                    money -= player.Hands[i][2]
                elif Sum(player.Hands[i][1]) == Sum(player.Hands[4][1]):
                    print(
                        '\033[1;33;48m Deck{} has drew vs the dealer\033[1;37;48m'.format(i+1))
        if insuranceBet > 0:
            if len(player.Hands[4][1]) == 2 and Sum(player.Hands[4][1]) == 21:
                money += (insuranceBet*2)
            else:
                money -= (insuranceBet)
    if (a-money) < 0:
        print('You had \033[1;33;48m{}\033[1;37;48m, now you have \033[1;32;48m{}\033[1;37;48m'.format(
            a, money))
    elif (a-money) > 0:
        print('You had \033[1;33;48m{}\033[1;37;48m, now you have \033[1;31;48m{}\033[1;37;48m'.format(
            a, money))
    elif (a-money) == 0:
        print('You had \033[1;33;48m{}\033[1;37;48m, now you have \033[1;33;48m{}\033[1;37;48m'.format(
            a, money))
    if money <= 0:
        print("\033[1;31;48mYou cant play without cash\033[1;37;48m")
        exit(0)


def logic(key=' '):
    global gameOver
    global player
    global counter
    global insuranceBet
    if key in player.Hands[counter][3] or key in ['s', 'S', '1']:
        if key == 'H':
            player.Hit(counter)
        elif key == '1':
            system('cls')
            input("\033[1;33;48mInstrucciones:\033[1;37;48m\nEl juego de blackjack consiste en lograr que tus\ncartas sumen 21, donde X, J, Q y K equivalen a 10\ny A puede ser 1 o 11 según sea conveniente.\n\n\033[1;33;48mLos posibles movimientos son:\n\033[1;37;48m[H] Pedir otra carta.\n[S] Ya no pedir más cartas.\n[D] Duplicar la apuesta y quedarse con la\n    siguiente carta.\n[2] Partir las dos cartas en 2 manos con apuestas\n    independientes.\n[I] Apostar a que el dealer tiene BlackJack.\n[X] Rendirse.\n\n\nPresione 'Enter' Para continuar")
        elif key == 'X':
            surrender[counter] = True
            counter += 1
            sleep(0.25)
        elif key == 'S':
            counter += 1
            sleep(0.25)
        elif key == 'D':
            player.Hands[counter][2] *= 2
            player.Hit(counter)
            counter += 1
        elif key == '2':
            player.Hands[player.NHands][2] = setBet(False)
            player.split(counter)
        elif key == 'I':
            insuranceBet = setBet(False)
    if Sum(player.Hands[counter][1]) >= 21:
        counter += 1
    if counter >= player.NHands:
        gameOver = True


while True:
    shuffle()
    player = Player(deckShuf, setBet())
    gameOver = False
    insuranceBet = 0
    surrender = [False, False, False, False]
    while gameOver == False:
        counter = 0
        while counter < player.NHands:
            if len(player.Hands[counter][1]) == 0:
                break
            display()
            displayOptions(counter)
            logic(opc())
    gameEnded()
    display()
    displayResults()
    input("Press 'Enter' to continue")
    system('cls')
