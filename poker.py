import random
import time
# Cards
cardPile = []
tableCards = []
ComputerCards = []
PlayerCards = []
rounds = 1

# - Test Zone
#testCards = []
#c10_1 = {"value": 10, "type": "♢", "name": "10", "img": "🂪"}
#c11_1 = {"value": 11, "type": "♢", "name": "J", "img": "🂫"}
#c12_1 = {"value": 12, "type": "♢", "name": "Q", "img": "🂬"}
#c13_1 = {"value": 13, "type": "♢", "name": "K", "img": "🂮"}
#c14_1 = {"value": 14, "type": "♢", "name": "A", "img": "🂾"}
#testCards.append(c10_1)
#testCards.append(c11_1)
#testCards.append(c12_1)
#testCards.append(c13_1)
#testCards.append(c14_1)


# --------------------------------------------------------------#
def startingHandComputer():
    ComputerCards.clear()
    newCard(ComputerCards), newCard(ComputerCards)


# --------------------------------------------------------------#
def startingHandPlayer():
    PlayerCards.clear()
    newCard(PlayerCards), newCard(PlayerCards)


# --------------------------------------------------------------#
def setupTableCards():
    tableCards.clear()
    newCard(tableCards), newCard(tableCards), newCard(tableCards)


# --------------------------------------------------------------#
def newCard(deck):  # Grab a new card - Remove - Give from the pile

    index = random.randint(0, len(cardPile))
    if index == len(cardPile):
        index = index - 1

    card = cardPile[index]
    cardPile.remove(cardPile[index])
    deck.append(card)


# --------------------------------------------------------------#
def showCards(deck):
    index = 0
    counter = 1
    while index < len(deck):
        print("{}:{}{}{}".format(counter, deck[index]['name'], deck[index]['type'], deck[index]['img']))
        index = index + 1
        counter = counter + 1


# --------------------------------------------------------------#
def showAll():
    print("Table")
    showCards(tableCards)
    print(" ______ ______ ______ ______ ______ ______ ______")
    time.sleep(3)  # Sleep for 3 seconds
    print("Computer")
    showCards(ComputerCards)
    print(" ______ ______ ______ ______ ______ ______ ______")
    time.sleep(3)  # Sleep for 3 seconds
    print("Player")
    showCards(PlayerCards)
    print(" ______ ______ ______ ______ ______ ______ ______")
    time.sleep(5)  # Sleep for 3 seconds



# --------------------------------------------------------------#
def showAllAfter():
    print("Table")
    showCards(tableCards)
    print(" ______ ______ ______ ______ ______ ______ ______")
    print("Computer")
    showCards(ComputerCards)
    print(" ______ ______ ______ ______ ______ ______ ______")
    print("Player")
    showCards(PlayerCards)
    print(" ______ ______ ______ ______ ______ ______ ______")
    time.sleep(5)  # Sleep for 3 seconds


def space():
    index = 0
    while index <= 15:
        print(" ")
        index += 1


# --------------------------------------------------------------#
def winner():
    deckStatsOfPlayer = checkDeckStats(PlayerCards)
    deckStatsOfComputer = checkDeckStats(ComputerCards)
    #testDeck = checkDeckStats(testCards)
    print("Comp: Hand Value: {}".format(deckStatsOfComputer['HandValue']))
    print("Play: Hand Value: {}".format(deckStatsOfPlayer['HandValue']))
    print(" ______ ______ ______ ______ ______ ______ ______")
    #print(testDeck['HandValue'])


    if deckStatsOfPlayer['HandValue'] > deckStatsOfComputer['HandValue']:
        print("__     __                   __          __  _           _   ")
        print("\ \   / /                   \ \        / / (_)         | |  ")
        print(" \ \_/ /    ___    _   _     \ \  /\  / /   _   _ __   | |  ")
        print("  \   /    / _ \  | | | |     \ \/  \/ /   | | | '_ \  | |  ")
        print("   | |    | (_) | | |_| |      \  /\  /    | | | | | | |_|  ")
        print("   |_|     \___/   \__,_|       \/  \/     |_| |_| |_| (_)  ")

    elif deckStatsOfPlayer['HandValue'] < deckStatsOfComputer['HandValue']:
        print(" __     __                    _                             _  ")
        print(" \ \   / /                   | |                           | | ")
        print("  \ \_/ /    ___    _   _    | |        ___    ___    ___  | | ")
        print("   \   /    / _ \  | | | |   | |       / _ \  / __|  / _ \ | | ")
        print("    | |    | (_) | | |_| |   | |____  | (_) | \__ \ |  __/ |_| ")
        print("    |_|     \___/   \__,_|   |______|  \___/  |___/  \___| (_) ")

    else:
        if deckStatsOfPlayer['HighCard'] > deckStatsOfComputer['HighCard']:
            print("__     __                   __          __  _           _   ")
            print("\ \   / /                   \ \        / / (_)         | |  ")
            print(" \ \_/ /    ___    _   _     \ \  /\  / /   _   _ __   | |  ")
            print("  \   /    / _ \  | | | |     \ \/  \/ /   | | | '_ \  | |  ")
            print("   | |    | (_) | | |_| |      \  /\  /    | | | | | | |_|  ")
            print("   |_|     \___/   \__,_|       \/  \/     |_| |_| |_| (_)  ")
        elif deckStatsOfPlayer['HighCard'] < deckStatsOfComputer['HighCard']:
            print(" __     __                    _                             _  ")
            print(" \ \   / /                   | |                           | | ")
            print("  \ \_/ /    ___    _   _    | |        ___    ___    ___  | | ")
            print("   \   /    / _ \  | | | |   | |       / _ \  / __|  / _ \ | | ")
            print("    | |    | (_) | | |_| |   | |____  | (_) | \__ \ |  __/ |_| ")
            print("    |_|     \___/   \__,_|   |______|  \___/  |___/  \___| (_) ")
        else:
            print("  _______   _          _  ")
            print(" |__   __| (_)        | | ")
            print("    | |     _    ___  | | ")
            print("    | |    | |  / _ \ | | ")
            print("    | |    | | |  __/ |_| ")
            print("    |_|    |_|  \___| (_) ")


# --------------------------------------------------------------#
def flushCheck(totalList):
    index = 0
    numberOfDiamonds = 0
    numberOfHearts = 0
    numberOfSpades = 0
    numberOfClubs = 0
    isAFlush = False

    while index < len(totalList):
        if totalList[index]['type'] == '♢':
            numberOfDiamonds += 1
        elif totalList[index]['type'] == '♡':
            numberOfHearts += 1
        elif totalList[index]['type'] == '♠':
            numberOfSpades += 1
        elif totalList[index]['type'] == '♣':
            numberOfClubs += 1
        index += 1

    if numberOfDiamonds >= 5:
        isAFlush = True
    elif numberOfHearts >= 5:
        isAFlush = True
    elif numberOfSpades >= 5:
        isAFlush = True
    elif numberOfClubs >= 5:
        isAFlush = True

    return isAFlush


# --------------------------------------------------------------#
def checkStraight(totalList):
    isAStraight = False
    pastCard = 0
    counter = 1

    for index in totalList:

        if pastCard != 0:
            b = (pastCard['value'])
            a = (index['value'] - 1)

            if a == b:
                counter += 1
                pastCard = index
                if counter >= 5:
                    isAStraight = True
                    return isAStraight
            else:
                counter = 0
                pastCard = index

        else:
            pastCard = index

    if counter >= 5:
        isAStraight = True

    return isAStraight


# --------------------------------------------------------------#
def checkAmountOfSameCard(totalList, card):
    counter = 0

    for index in totalList:
        if index['value'] == card['value']:
            counter += 1

    Card = {"value": card['value'], "numberOfSameCardInDeck": counter}  # Used in Checking Decks
    return Card


# ---------------------------------------------------------------#
def checkIfSpecificCardInDeck(totalList, cardValue):
    containsCard = False

    for index in totalList:
        if index['value'] == cardValue:
            containsCard = True

    return containsCard


# ---------------------------------------------------------------#
def checkFourOfAKind(listOfAllCardsInDeckSimplified):
    containsFourOfAKind = False

    for index in listOfAllCardsInDeckSimplified:
        if index['numberOfSameCardInDeck'] == 4:
            containsFourOfAKind = True

    return containsFourOfAKind


# ---------------------------------------------------------------#
def checkThreeOfAKind(listOfAllCardsInDeckSimplified):
    containsThreeOfAKind = False

    for index in listOfAllCardsInDeckSimplified:
        if index['numberOfSameCardInDeck'] == 3:
            containsThreeOfAKind = True

    return containsThreeOfAKind


# ---------------------------------------------------------------#
def checkPair(listOfAllCardsInDeckSimplified):
    containsPair = False


    for index in listOfAllCardsInDeckSimplified:
        if index['numberOfSameCardInDeck'] == 2:
            containsPair = True

    return containsPair


# ---------------------------------------------------------------#
def checkTwoPair(listOfAllCardsInDeckSimplified):
    containsTwoPair = False
    counter = 0

    for index in listOfAllCardsInDeckSimplified:
        if index['numberOfSameCardInDeck'] == 2:
            counter += 1

    if counter >= 2:
        containsTwoPair = True

    return containsTwoPair


# ---------------------------------------------------------------#
def checkHighCard(listOfAllCardsInDeckSimplified):
    highCardValue = 0

    for index in listOfAllCardsInDeckSimplified:
        currentCardValue = index['value']

        if highCardValue < currentCardValue:
            highCardValue = currentCardValue

    return highCardValue


# ---------------------------------------------------------------#

def checkDeckValue(listOfAllCardsInDeckSimplified, totalList):

    isAFlush = flushCheck(totalList)  # Check if it's a Flush
    isAStraight = checkStraight(listOfAllCardsInDeckSimplified)  # Check if it's a Straight

    #for index in listOfAllCardsInDeckSimplified:
        #print(index)

    

    isAceInDeck = checkIfSpecificCardInDeck(listOfAllCardsInDeckSimplified, 14)  # Check if Ace in deck
    isKingInDeck = checkIfSpecificCardInDeck(listOfAllCardsInDeckSimplified, 13)  # Check if King in deck
    isQueenInDeck = checkIfSpecificCardInDeck(listOfAllCardsInDeckSimplified, 12)  # Check if Queen in deck
    isJackInDeck = checkIfSpecificCardInDeck(listOfAllCardsInDeckSimplified, 11)  # Check if Jack in deck
    is10InDeck = checkIfSpecificCardInDeck(listOfAllCardsInDeckSimplified, 10)  # Check if 10 in deck
    isFourOfAKind = checkFourOfAKind(listOfAllCardsInDeckSimplified)  # Check Four of a kind
    isThreeOfAKind = checkThreeOfAKind(listOfAllCardsInDeckSimplified)  # Check Three of a kind
    isTwoPair = checkTwoPair(listOfAllCardsInDeckSimplified)  # Check if Two Pair
    isPair = checkPair(listOfAllCardsInDeckSimplified)  # Check Pair
    highCard = checkHighCard(listOfAllCardsInDeckSimplified)  # Check High Card


    if isAStraight and isAFlush and isAceInDeck and isKingInDeck and isQueenInDeck and isJackInDeck and is10InDeck:
        deckValue = 10  # Royal Flush - Checked

    elif isAStraight and isAFlush:
        deckValue = 9  # Straight Flush - Checked

    elif isFourOfAKind:
        deckValue = 8  # Four of a kind - Checked

    elif isThreeOfAKind and isPair:
        deckValue = 7  # Full House - Checked

    elif isAFlush:
        deckValue = 6  # Flush - Checked

    elif isAStraight:
        deckValue = 5  # Straight - Checked

    elif isThreeOfAKind:
        deckValue = 4  # Three of a kind - Checked

    elif isTwoPair:
        deckValue = 3  # Two Pair - Checked

    elif isPair:
        deckValue = 2  # One Pair - Checked

    else:
        deckValue = 1  # HighCard - Needs to be extended

    deckStats = {'HandValue': deckValue, 'Flush': isAFlush, 'Straight': isAStraight, 'HighCard': highCard}
    return deckStats


# ---------------------------------------------------------------#
def checkDeckStats(deck):
    sorted_deck = sorted(deck, key=lambda x: x['value'])
    totalList = tableCards.copy()
    sorted_TotalList = totalList
    sorted_TotalList.extend(sorted_deck)
    sorted_TotalList = sorted(totalList, key=lambda x: x['value'])


    listOfAllCardsInDeckSimplified = []

    # Make a list all Cards and the amount of Same Cards
    for index in sorted_TotalList:
        listOfAllCardsInDeckSimplified.append(checkAmountOfSameCard(totalList, index))

    sorted_TotalListSimplified = sorted(listOfAllCardsInDeckSimplified, key=lambda x: x['value'])

    pastCard = 0
    counter = 0
    indexPointerList = []

    # Deleting Replicas in Simplified list (1st List)
    for index in sorted_TotalListSimplified:
        if pastCard != 0:
            if pastCard['value'] == index['value']:
                indexPointerList.append(index)
            else:
                pastCard = index
        else:
            pastCard = index
        counter += 1

    if len(indexPointerList) != 0:
        for index in indexPointerList:
            sorted_TotalListSimplified.remove(index)

    deckStats = checkDeckValue(sorted_TotalListSimplified, sorted_TotalList)

    deckStatsData = {'HandValue': deckStats['HandValue'], 'Flush': deckStats['Flush'],
                     'Straight': deckStats['Straight'], 'HighCard': deckStats['HighCard']}  # Reset
    return deckStatsData


# ---------------------------------------------------------------#
def newCardsPile():
    cardPile.clear()  # Reset

    cardPile.append(c2_1), cardPile.append(c3_1), cardPile.append(c4_1)  # Diamonds
    cardPile.append(c5_1), cardPile.append(c6_1), cardPile.append(c7_1)
    cardPile.append(c8_1), cardPile.append(c9_1), cardPile.append(c10_1)
    cardPile.append(c11_1), cardPile.append(c12_1), cardPile.append(c13_1)
    cardPile.append(c14_1)

    cardPile.append(c2_2), cardPile.append(c3_2), cardPile.append(c4_2)  # Hearts
    cardPile.append(c5_2), cardPile.append(c6_2), cardPile.append(c7_2)
    cardPile.append(c8_2), cardPile.append(c9_2), cardPile.append(c10_2)
    cardPile.append(c11_2), cardPile.append(c12_2), cardPile.append(c13_2)
    cardPile.append(c14_2)

    cardPile.append(c2_3), cardPile.append(c3_3), cardPile.append(c4_3)  # Spades
    cardPile.append(c5_3), cardPile.append(c6_3), cardPile.append(c7_3)
    cardPile.append(c8_3), cardPile.append(c9_3), cardPile.append(c10_3)
    cardPile.append(c11_3), cardPile.append(c12_3), cardPile.append(c13_3)
    cardPile.append(c14_3)

    cardPile.append(c2_4), cardPile.append(c3_4), cardPile.append(c4_4)  # Clubs
    cardPile.append(c5_4), cardPile.append(c6_4), cardPile.append(c7_4)
    cardPile.append(c8_4), cardPile.append(c9_4), cardPile.append(c10_4)
    cardPile.append(c11_4), cardPile.append(c12_4), cardPile.append(c13_4)
    cardPile.append(c14_4)


# Cards
c2_1 = {"value": 2, "type": "♢", "name": "2", "img": "🃂"}
c3_1 = {"value": 3, "type": "♢", "name": "3", "img": "🃃"}
c4_1 = {"value": 4, "type": "♢", "name": "4", "img": "🃄"}
c5_1 = {"value": 5, "type": "♢", "name": "5", "img": "🃅"}
c6_1 = {"value": 6, "type": "♢", "name": "6", "img": "🂦"}
c7_1 = {"value": 7, "type": "♢", "name": "7", "img": "🂧"}
c8_1 = {"value": 8, "type": "♢", "name": "8", "img": "🂨"}
c9_1 = {"value": 9, "type": "♢", "name": "9", "img": "🂩"}
c10_1 = {"value": 10, "type": "♢", "name": "10", "img": "🂪"}
c11_1 = {"value": 11, "type": "♢", "name": "J", "img": "🂫"}
c12_1 = {"value": 12, "type": "♢", "name": "Q", "img": "🂬"}
c13_1 = {"value": 13, "type": "♢", "name": "K", "img": "🂮"}
c14_1 = {"value": 14, "type": "♢", "name": "A", "img": "🂾"}

c2_2 = {"value": 2, "type": "♡", "name": "2", "img": "🂲"}
c3_2 = {"value": 3, "type": "♡", "name": "3", "img": "🂳"}
c4_2 = {"value": 4, "type": "♡", "name": "4", "img": "🂳"}
c5_2 = {"value": 5, "type": "♡", "name": "5", "img": "🂴"}
c6_2 = {"value": 6, "type": "♡", "name": "6", "img": "🂶"}
c7_2 = {"value": 7, "type": "♡", "name": "7", "img": "🂷"}
c8_2 = {"value": 8, "type": "♡", "name": "8", "img": "🂸"}
c9_2 = {"value": 9, "type": "♡", "name": "9", "img": "🂹"}
c10_2 = {"value": 10, "type": "♡", "name": "10", "img": "🂺"}
c11_2 = {"value": 11, "type": "♡", "name": "J", "img": "🂫"}
c12_2 = {"value": 12, "type": "♡", "name": "Q", "img": "🂻"}
c13_2 = {"value": 13, "type": "♡", "name": "K", "img": "🂽"}
c14_2 = {"value": 14, "type": "♡", "name": "A", "img": "🂾"}

c2_3 = {"value": 2, "type": "♠", "name": "2", "img": "🂢"}
c3_3 = {"value": 3, "type": "♠", "name": "3", "img": "🂳"}
c4_3 = {"value": 4, "type": "♠", "name": "4", "img": "🂴"}
c5_3 = {"value": 5, "type": "♠", "name": "5", "img": "🂵"}
c6_3 = {"value": 6, "type": "♠", "name": "6", "img": "🂶"}
c7_3 = {"value": 7, "type": "♠", "name": "7", "img": "🂷"}
c8_3 = {"value": 8, "type": "♠", "name": "8", "img": "🂸"}
c9_3 = {"value": 9, "type": "♠", "name": "9", "img": "🂹"}
c10_3 = {"value": 10, "type": "♠", "name": "10", "img": "🂺"}
c11_3 = {"value": 11, "type": "♠", "name": "J", "img": "🂫"}
c12_3 = {"value": 12, "type": "♠", "name": "Q", "img": "🂻"}
c13_3 = {"value": 13, "type": "♠", "name": "K", "img": "🂽"}
c14_3 = {"value": 14, "type": "♠", "name": "A", "img": "🂾"}

c2_4 = {"value": 2, "type": "♣", "name": "2", "img": "🂢"}
c3_4 = {"value": 3, "type": "♣", "name": "3", "img": "🂳"}
c4_4 = {"value": 4, "type": "♣", "name": "4", "img": "🂴"}
c5_4 = {"value": 5, "type": "♣", "name": "5", "img": "🂵"}
c6_4 = {"value": 6, "type": "♣", "name": "6", "img": "🂶"}
c7_4 = {"value": 7, "type": "♣", "name": "7", "img": "🂷"}
c8_4 = {"value": 8, "type": "♣", "name": "8", "img": "🂸"}
c9_4 = {"value": 9, "type": "♣", "name": "9", "img": "🂹"}
c10_4 = {"value": 10, "type": "♣", "name": "10", "img": "🂺"}
c11_4 = {"value": 11, "type": "♣", "name": "J", "img": "🂫"}
c12_4 = {"value": 12, "type": "♣", "name": "Q", "img": "🂻"}
c13_4 = {"value": 13, "type": "♣", "name": "K", "img": "🂽"}
c14_4 = {"value": 14, "type": "♣", "name": "A", "img": "🂾"}


# --------------------------------------------------------------#
def reset():  # Reset Game
    newCardsPile()
    startingHandPlayer()
    startingHandComputer()
    setupTableCards()


# ----------------------------------------------------------------#
def roundCounter(rounds):
    if rounds == 1:
        print("  _____                                _     __ ")
        print("|  __ \                              | |   /_ |")
        print("| |__) |   ___    _   _   _ __     __| |    | |")
        print("|  _  /   / _ \  | | | | | '_ \   / _` |    | |")
        print("| | \ \  | (_) | | |_| | | | | | | (_| |    | |")
        print("|_|  \_\  \___/   \__,_| |_| |_|  \__,_|    |_|")

        print( " ______ ______ ______ ______ ______ ______ ______")
        print( "|______|______|______|______|______|______|______|")

    elif rounds == 2:
        print("  _____                                _     ___  ")
        print("|  __ \                              | |   |__ \ ")
        print("| |__) |   ___    _   _   _ __     __| |      ) |")
        print("|  _  /   / _ \  | | | | | '_ \   / _` |     / / ")
        print("| | \ \  | (_) | | |_| | | | | | | (_| |    / /_ ")
        print("|_|  \_\  \___/   \__,_| |_| |_|  \__,_|   |____|")
        print( " ______ ______ ______ ______ ______ ______ ______")
        print( "|______|______|______|______|______|______|______|")

    elif rounds == 3:
        print("  _____                                _     ____ ")
        print("|  __ \                              | |   |___ \ ")
        print("| |__) |   ___    _   _   _ __     __| |     __) |")
        print("|  _  /   / _ \  | | | | | '_ \   / _` |    |__ < ")
        print("| | \ \  | (_) | | |_| | | | | | | (_| |    ___) |")
        print("|_|  \_\  \___/   \__,_| |_| |_|  \__,_|   |____/ ")
        print( " ______ ______ ______ ______ ______ ______ ______")
        print( "|______|______|______|______|______|______|______|")


# ----------------------------------------------------------------#
def game():
    print(" _____            _                  ")
    print("|  __ \          | |                 ")
    print("| |__) |   ___   | | __   ___   _ __ ")
    print("|  ___/   / _ \  | |/ /  / _ \ | '__|")
    print("| |      | (_) | |   <  |  __/ | |   ")
    print("|_|       \___/  |_|\_\  \___| |_|   ")
    print("______ ______ ______ ______ ______ __")

    reset()  # Reset Game
    print('Its all automatic, just press enter and WAIT!')
    input('Ready? ')
    space()
    roundCounter(1)
    time.sleep(3)  # Sleep for 3 seconds

    showAll()
    space()

    roundCounter(2)
    time.sleep(3)  # Sleep for 3 seconds
    newCard(tableCards)
    showAllAfter()
    space()

    roundCounter(3)
    time.sleep(3)  # Sleep for 3 seconds

    newCard(tableCards)
    showAllAfter()
    winner()


game()
