import random
import requests

import sqlite3
from sqlite3 import Error
from matplotlib import pyplot as plt
import numpy as np

def save(name, option, result, link):
    connection = sqlite3.connect(link)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS stats
              (name TEXT, option TEXT, result TEXT)''')
    sqlite_insert_with_param = """INSERT INTO stats
                          (name, option, result) 
                          VALUES (?, ?, ?);"""

    data_tuple = (name, option, result)

    cursor.execute(sqlite_insert_with_param, data_tuple)
    connection.commit()
    #print("Erfolgreich hochgeladen")
    connection.close()

def createOptions():
    deck = ['stein', 'papier', 'schere', 'echse', 'spock']
    return deck

def playerWins(optionPlayer, optionBot):
    if(optionPlayer, optionBot) in [
        ("schere", "papier"),
        ("papier", "stein"),
        ("stein", "echse"),
        ("echse", "spock"),
        ("spock", "schere"),
        ("schere", "echse"),
        ("echse", "papier"),
        ("papier", "spock"),
        ("spock", "stein"),
        ("stein", "schere")
    ]:
        return True
    else:
        return False

    
def bestPlayer(name):
    connection = sqlite3.connect('rockpaperscissor/data/rockpaperscissor.sqlite3')
    cursor = connection.cursor()
    sql = "SELECT COUNT(*) as anz, name FROM stats WHERE result = 'win' GROUP BY name ORDER BY anz DESC;"
    cursor.execute(sql)
    bestUser = cursor.fetchall()
    print(bestUser)
    x = []
    y = []
    for u in bestUser:
        x.append(u[1])
        y.append(u[0])

    plt.bar(x, y, align="center")
    plt.show()
    #print("\n Die besten Spieler und die Anzahl von den Siegen:")
    #print(bestUser)
    #print("Die besten Spieler: \n")
    #i = 0
    #for u in bestUser:
    #    print(str(i) + ".: " + str(u[i][1]) + "\n")
    #    i += 1
    #print("Der beste Benutzer: " + bestUser)
    connection.close()
    startGame(name, True)



def completeRound(name, optionPlayer, optionBot, player, bot):
    print("Der Computer wählt: " + optionBot)
    if optionPlayer == optionBot:
        print("Unentschieden")
        save(name, optionPlayer, "draw", 'rockpaperscissor/data/rockpaperscissor.sqlite3')
        save("bot", optionBot, "draw", 'rockpaperscissor/data/rockpaperscissor.sqlite3')
        return player, bot
    elif playerWins(optionPlayer, optionBot):
        print("Sie haben gewonnen")
        save(name, optionPlayer, "win", 'rockpaperscissor/data/rockpaperscissor.sqlite3')
        save("bot", optionBot, "lost", 'rockpaperscissor/data/rockpaperscissor.sqlite3')
        player += 1
        return player, bot
    elif not playerWins(optionPlayer, optionBot):
        print("Sie haben verloren")
        save(name, optionPlayer, "lost", 'rockpaperscissor/data/rockpaperscissor.sqlite3')
        save("bot", optionBot, "win", 'rockpaperscissor/data/rockpaperscissor.sqlite3')
        bot += 1
        return player, bot


def normalGame(x, name):
    player = 0
    bot = 0
    for i in range(x):
        options = createOptions()
        print("Stein, Papier, Schere, Echse oder Spock?")

        optionPlayer = input("Ihre Wahl: ").lower()
        optionBot = random.choice(options)
        player, bot = completeRound(name,optionPlayer, optionBot, player, bot)
        print("Score: \n Player: " + str(player) + "     Bot: " + str(bot))
    startGame(name, True)


def getPlayerFavouriteOption(name, which):
    connection = sqlite3.connect('rockpaperscissor/data/rockpaperscissor.sqlite3')
    cursor = connection.cursor()
    args = []
    args.append(name)
    sql = "SELECT COUNT(*) as anz, option FROM stats WHERE name = ? GROUP BY option ORDER BY anz DESC;"
    cursor.execute(sql, args)
    answer = cursor.fetchall()

    if which == 1:
        return answer[0][1]
    elif which == 2:
        return answer[1][1]
    


def hardGame(anz, name):
    player = 0
    bot = 0
    for i in range(anz):
        userMostPlayedOption = getPlayerFavouriteOption(name, 1)
        userSecondPlayedOption = getPlayerFavouriteOption(name, 2)
        newoptions = []
        if userMostPlayedOption == "schere" or userSecondPlayedOption == "schere":
            #newoptions =["spock", "stein"]
            newoptions.append("spock")
            newoptions.append("stein")
        if userMostPlayedOption == "stein" or userSecondPlayedOption == "stein":
            #newoptions = ["papier", "spock"]
            newoptions.append("papier")
            newoptions.append("spock")
        if userMostPlayedOption == "papier" or userSecondPlayedOption == "papier":
            #newoptions = ["schere", "echse"]
            newoptions.append("schere")
            newoptions.append("echse")
        if userMostPlayedOption == "echse" or userSecondPlayedOption == "echse":
            #newoptions = ["stein", "schere"]
            newoptions.append("stein")
            newoptions.append("schere")
        if userMostPlayedOption == "spock" or userSecondPlayedOption == "spock":
            #newoptions = ["echse", "papier"]
            newoptions.append("echse")
            newoptions.append("papier")
        print(newoptions)
        optionBot = random.choice(newoptions)
        print("Stein, Papier, Schere, Echse oder Spock?")
        optionPlayer = input("Ihre Wahl: ").lower()
        player, bot = completeRound(name,optionPlayer, optionBot, player, bot)
        print("Score: \n Player: " + str(player) + "     Bot: " + str(bot))
    startGame(name, True)

def impossibleGame(anz, name):
    player = 0
    bot = 0
    for i in range(anz):
        print("Stein, Papier, Schere, Echse oder Spock?")
        optionPlayer = input("Ihre Wahl: ").lower()

        newoptions = []
        if optionPlayer == "schere":
            newoptions = ["spock", "stein"]
        elif optionPlayer == "stein":
            newoptions = ["papier", "spock"]
        elif optionPlayer == "papier":
            newoptions = ["schere", "echse"]
        elif optionPlayer == "echse":
            newoptions = ["stein", "schere"]
        elif optionPlayer == "spock":
            newoptions = ["echse", "papier"]
        optionBot = random.choice(newoptions)
        player, bot = completeRound(name,optionPlayer, optionBot, player, bot)
        print("Score: \n Player: " + str(player) + "     Bot: " + str(bot))
    startGame(name, True)
    

def upload(name):
    deck = createOptions()
    host = 'http://localhost:5000/upload'
    connection = sqlite3.connect('rockpaperscissor/data/rockpaperscissor.sqlite3')
    cursor = connection.cursor()
    for d in deck:
        sql = "SELECT COUNT(option) FROM stats WHERE name = ? AND option = ?;"
        args = (name, d)
        cursor.execute(sql, args)
        cnt = cursor.fetchone()[0]
        response = requests.put('%s/%s' % (host, name), data={'name' : name, 'symbol' : d, 'symbolanzahl' : cnt})
    print("Erfolgreich hochgeladen!")
    startGame(name, True)


def botVSbot(name):
    bot1 = 0
    bot2 = 0
    draw = 0
    options = createOptions()
    x = input("Wie viele Runden sollen sie spielen? ")
    for i in range(int(x)):
        bot1Answer = random.choice(options)
        bot2Answer = random.choice(options)
        if bot1Answer == bot2Answer:
            #print("Unentschieden")
            #print("Beide Computer sind dumm")
            draw += 1
        elif playerWins(bot1Answer, bot2Answer):
            #print("Computer 1 ist schlauer")
            bot1 += 1
        elif not playerWins(bot1Answer, bot2Answer):
            #print("Computer 2 ist schlauer")
            bot2 += 1
    print("Computer 1 hat " + str(bot1) + " mal gewonnen und Computer 2 hat " + str(bot2) + " mal")
    print("Es wurde " + str(draw) + " mal unentschieden gespielt")
    circle_values = np.array([bot1, bot2, draw])
    label = ["Computer 1", "Computer 2", "Draw"]
    plt.pie(circle_values, labels = label, autopct='%1.2f%%')
    plt.show()
    startGame(name, True)


def printStats(name):
    connection = sqlite3.connect('rockpaperscissor/data/rockpaperscissor.sqlite3')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stats")

    print("Alle Daten:")
    print(cursor.fetchall())
    args = []
    args.append(name)
    sql = "SELECT COUNT(result) FROM stats WHERE name = ? AND result = 'win';"
    cursor.execute(sql, args)
    userWins = cursor.fetchone()[0]
    sql = "SELECT COUNT(result) FROM stats WHERE name = ? AND result = 'lost';"
    cursor.execute(sql, args)
    userLosts = cursor.fetchone()[0]
    print("\n" + name + " hat " + str(userWins) + " mal gewonnen und " + str(userLosts) + " mal verloren")

    cursor.execute("SELECT COUNT(result) FROM stats WHERE name = 'bot' AND result = 'win';")
    botWins = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(result) FROM stats WHERE name = 'bot' AND result = 'lost';")
    botLosts = cursor.fetchone()[0]
    print("Der Computer hat " + str(botWins) + " mal gewonnen und " + str(botLosts) + " mal verloren")
    cursor.execute("SELECT COUNT(result) FROM stats WHERE result = 'draw';")
    draw = cursor.fetchone()[0]
    print("Es wurde " + str(draw) + " mal untentschieden gespielt\n")

    sql = "SELECT COUNT(*) as anz, option FROM stats WHERE name = ? GROUP BY option ORDER BY anz DESC;"
    cursor.execute(sql, args)
    userMostPlayedOption = cursor.fetchone()[1]
    print(name + " hat am öftesten " + str(userMostPlayedOption) + " gespielt")
    cursor.execute("SELECT COUNT(*) as anz, option FROM stats WHERE name = 'bot' GROUP BY option ORDER BY anz DESC;")
    botMostPlayedOption = cursor.fetchone()[1]
    print("Der Computer hat am öftesten " + str(botMostPlayedOption) + " gespielt")

    connection.close()
    startGame(name, True)

def startGame(name, namefertig):
    if not namefertig:
        name = input("Bitte geben Sie einen Namen ein: ")
    mode = input("Was wollen Sie tun? (spielen oder stats oder upload oder spezial): ")
    if mode == "stats":
        x = input("Statistik oder Bestenliste? ")
        if x.lower() == "statistik":
            printStats(name)
        elif x.lower() == "bestenliste":
            bestPlayer(name)
        else:
            print("Ungültige Eingabe!")
    elif mode == "spielen":
        x = input("Wie viele Runden wollen Sie spielen? ")
        modus = input("Wie wollen sie spielen? normal oder schwer oder unmoeglich: ")
        if modus == "normal": normalGame(int(x), name)
        if modus == "schwer": hardGame(int(x), name)
        if modus == "unmoeglich": impossibleGame(int(x), name)
    elif mode == "upload":
        upload(name)
    elif mode == "spezial":
        botVSbot(name)
    elif mode == "exit":
        return
    else:
        print("Ungültige Eingabe!")
        startGame(name, True)


if __name__ == "__main__":
    startGame("", False)