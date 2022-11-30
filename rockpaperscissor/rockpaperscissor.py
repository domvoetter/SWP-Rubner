import random

import sqlite3
from sqlite3 import Error

def save(name, option, result):
    connection = sqlite3.connect('rockpaperscissor/data/rockpaperscissor.sqlite3')
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
    
    
def game(x, name):
    player = 0
    bot = 0
    for i in range(x):
        options = createOptions()
        print("Stein, Papier, Schere, Echse oder Spock?")

        optionPlayer = input("Ihre Wahl: ").lower()
        optionBot = random.choice(options)
        print("Der Computer wählt: " + optionBot)

        if optionPlayer == optionBot:
            print("Unentschieden")
            save(name, optionPlayer, "draw")
            save("bot", optionBot, "draw")
        elif playerWins(optionPlayer, optionBot):
            print("Sie haben gewonnen")
            player += 1
            save(name, optionPlayer, "win")
            save("bot", optionBot, "lost")
        elif not playerWins(optionPlayer, optionBot):
            print("Sie haben verloren")
            bot += 1
            save(name, optionPlayer, "lost")
            save("bot", optionBot, "win")
    print("Score: \n Player: " + str(player) + "     Bot: " + str(bot))

def printStats():
    connection = sqlite3.connect('rockpaperscissor/data/rockpaperscissor.sqlite3')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM stats")

    print("Alle Daten:")
    print(cursor.fetchall())

    cursor.execute("SELECT COUNT(result) FROM stats WHERE name = 'Dominik' AND result = 'win';")
    userWins = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(result) FROM stats WHERE name = 'Dominik' AND result = 'lost';")
    userLosts = cursor.fetchone()[0]
    print("\nDominik hat " + str(userWins) + " mal gewonnen und " + str(userLosts) + " mal verloren")

    cursor.execute("SELECT COUNT(result) FROM stats WHERE name = 'bot' AND result = 'win';")
    botWins = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(result) FROM stats WHERE name = 'bot' AND result = 'lost';")
    botLosts = cursor.fetchone()[0]
    print("Der Computer hat " + str(botWins) + " mal gewonnen und " + str(botLosts) + " mal verloren")
    cursor.execute("SELECT COUNT(result) FROM stats WHERE result = 'draw';")
    draw = cursor.fetchone()[0]
    print("Es wurde " + str(draw) + " mal untentschieden gespielt\n")

    cursor.execute("SELECT COUNT(*) as anz, option FROM stats WHERE name = 'Dominik' GROUP BY option ORDER BY anz DESC;")
    userMostPlayedOption = cursor.fetchone()[1]
    print("Dominik hat am öftesten " + str(userMostPlayedOption) + " gespielt")
    cursor.execute("SELECT COUNT(*) as anz, option FROM stats WHERE name = 'bot' GROUP BY option ORDER BY anz DESC;")
    botMostPlayedOption = cursor.fetchone()[1]
    print("Der Computer hat am öftesten " + str(botMostPlayedOption) + " gespielt")

    connection.close()

def startGame():
    mode = input("Was wollen Sie tun? (spielen oder stats): ")
    if mode == "stats":
        printStats()
    elif mode == "spielen":
        name = input("Bitte geben Sie einen Namen ein: ")
        x = input("Wie viele Runden wollen Sie spielen? ")
        game(int(x), name)
    else:
        print("Ungültige eingabe")



if __name__ == "__main__":
    startGame()