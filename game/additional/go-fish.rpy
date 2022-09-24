init python:

    class HumanPlayer(object):
        def __init__(self,deck):
            self.hand = defaultdict(int)
            self.book = []
            self.deck = deck #making a copy of deck, all changes within
                            #this class should affect the global deck
            self.score = 0
            self.name = raw_input('Name yourself: ')
    
        def Draw(self): #assuming that deck is a global
            cardDrawn = self.deck.pop() #removes the last card from deck
            self.hand[cardDrawn] += 1 #adds card to hand
            print '%s drew %s.' % (self.name,cardDrawn)
            self.checkForBooks()
    
        def checkForBooks(self):
    #       Removes all items of which are 4.
            for key,val in self.hand.items(): #can't use iteritems() because we are modifying hand in loop
                if val == 4: #completed a book
                    self.book.append(key)
                    print '%s completed the book of %s\'s.' % (self.name,key)
                    self.score += 1
                    del self.hand[key]
            self.emptyCheck()
    
        def emptyCheck(self):
            if len(self.deck)!=0 and len(self.hand)==0: #checks if deck/hand is empty
                self.Draw()
        def displayHand(self): #Displays current hand, cards separated by spaces
            return ' '.join(key for key,val in self.hand.items()
                            for i in range(val)) #meh, make it prettier
    
        def makeTurn(self):
            print '%s\'s hand: %s' % (self.name,self.displayHand())
            chooseCard = raw_input('What card do you ask for? ').strip()
            if chooseCard == 'quit':
                sys.exit(0)
            if chooseCard not in self.hand:
                print 'You don\'t have that card. Try again! (or enter quit to exit)'
                chooseCard = self.makeTurn()
            return chooseCard
    
        def fishFor(self,card):
            if card in self.hand: # if card in hand, returns count and removes the card from hand
                val = self.hand.pop(card)
                self.emptyCheck()
                return val
            else:
                return False
        def gotCard(self,card,amount):
            self.hand[card] += amount
            self.checkForBooks()
    
    
    
    class Computer(HumanPlayer):
        def __init__(self,deck):
            self.name = 'Sayori'
            self.hand = defaultdict(int)
            self.book = []
            self.deck = deck
            self.opponentHas = set()
            self.score = 0
    
        def Draw(self): #assuming that deck is a global
            cardDrawn = self.deck.pop() #removes the last card from deck
            self.hand[cardDrawn] += 1 #adds card to hand
            print '%s drew a card.' % (self.name)
            self.checkForBooks()
    
        ##AI: guesses cards that knows you have, then tries cards he has at random.
        ##Improvements: remember if the card was rejected before, guess probabilities
        def makeTurn(self):
    #        print self.displayHand(),self.opponentHas
            candidates = list(self.opponentHas & set(self.hand.keys())) #checks for cards in hand that computer knows you have
            if not candidates:
                candidates = self.hand.keys() #if no intersection between those two, random guess
            move = random.choice(candidates)
            print '%s fishes for %s.' % (self.name,move)
            return move
    
        def fishFor(self,card): #Same as for humans players, but adds the card fished for to opponentHas list.
            self.opponentHas.add(card)
            if card in self.hand: # if card in hand, returns count and removes the card from hand
                val = self.hand.pop(card)
                self.emptyCheck()
                return val
            else:
                return False
    
        def gotCard(self,card,amount):
            self.hand[card] += amount
            self.opponentHas.discard(card)
            self.checkForBooks()
    
    class PlayGoFish(object):
        def __init__(self):
            self.deck = ('2 3 4 5 6 7 8 9 10 J Q K A '*4).split(' ')
            self.deck.remove('')
            self.player = [HumanPlayer(self.deck),Computer(self.deck)] #makes counting turns easier
    
        def endOfPlayCheck(self):#checks if hands/decks are empty using the any method
                return self.deck or self.player[0].hand or self.player[1].hand
    
        def play(self):
            random.shuffle(self.deck)
            for i in xrange(9): # Deal the first cards
                self.player[0].Draw()
                self.player[1].Draw()
            turn = 0
            while self.endOfPlayCheck():
                print '\nTurn %d (%s:%d %s:%d) %d cards remaining.' % (turn,self.player[0].name,
                        self.player[0].score,self.player[1].name,self.player[1].score,len(self.deck))
                whoseTurn = turn%2
                otherPlayer = (turn+1)%2
                while True: #loop until player finishes turn
                    cardFished = self.player[whoseTurn].makeTurn()
                    result = self.player[otherPlayer].fishFor(cardFished)
                    if not result: #Draws and ends turn
                        self.player[whoseTurn].Draw()
                        break
                    print '%s got %d more %s.' % (self.player[whoseTurn].name,result, cardFished)
                    self.player[whoseTurn].gotCard(cardFished,result)
                    if not self.endOfPlayCheck(): break
                turn+=1
            print '\nScores: \n%s: %d\n%s: %d\n' % (self.player[0].name,self.player[0].score,
                                            self.player[1].name,self.player[1].score)
            if self.player[0].score>self.player[1].score:
                print self.player[0].name,'won!'
            elif self.player[0].score==self.player[1].score:
                print 'Draw!'
            else:
                print self.player[1].name,'won!'