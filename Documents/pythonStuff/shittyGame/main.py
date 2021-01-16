from extra import *
import random,sys

class Game():
    def __init__(self):
        self.name = "SHITTY GAME"

    def status(self):
        print(self.name + " IS INSTANTIATED")

    def grid(self,player):
        
        for room in rooms:
            if player.pos_x == room.pos_x and player.pos_y == room.pos_y:
                room.status()

    def options(self,player):
        #player.status()
        print("MOVE: (N), (S), (E), (W) | (C)HARACTERS | (I)NVENTORY | (M)ENU")
        ###   PLAYER USER INPUT
        user_input = player.user_input()
        
        if user_input == "N":
            player.pos_y += 1
        elif user_input == "S":
            player.pos_y -= 1
        elif user_input == "E":
           player.pos_x += 1
        elif user_input == "W":
           player.pos_x -= 1
        elif user_input == "C":
            for room in rooms:
                if player.pos_x == room.pos_x and player.pos_y == room.pos_y:
                    room.interact_npc(player)
        elif user_input == "I":
            for room in rooms:
                if player.pos_x == room.pos_x and player.pos_y == room.pos_y:
                    player.inventory(room)
        elif user_input == "M":
            self.main_menu()
        else:
           pass
        return
   
    def main_menu(self):    
        clear()
        fancy_text(self.name)
        print("(N)AME CHARACTER | (H)ELP | (P)LAY GAME | (Q)UIT")    
        print("──────────")    

        user_input = player.user_input()
        
        if user_input == "N":        
            print("WHAT IS YOUR NAME?")    
            user_input = player.user_input()    
            if len(str(user_input)) > 10 or len(str(user_input)) < 1:    
                print("INVALID NAME LENGTH")    
                user_input = player.user_input()
                self.main_menu()    
            else:
                player.name = user_input
                print("HELLO " + str(player.name))
                user_input = player.user_input()
                self.main_menu()

        elif user_input == "H":
            game.help()

        elif user_input == "P":
            if player.name == None:
                print("FINISH MAKING YOUR CHARACTER")
                user_input = player.user_input()
                self.main_menu()
        elif user_input == "Q":
            clear()
            sys.exit()
        else:
            self.main_menu()


    def help(self):
        clear()    
        fancy_text("HELP")
        print("OPTIONS HAVE THEIR LETTER IN PARENTHESIS")
        print("YOU MAY HAVE TO PRESS ENTER TO CONTIUNE")
        print("EXPLORE ALL THE OPTIONS AND HAVE FUN")
        print("──────────")

        user_input = player.user_input()
        self.main_menu()

    def dice_game(self,player,npc):
        if npc == wizard:
            print(npc.name + ": LET'S PLAY WITH THEM DICE LIKE YOUR MOM PLAYED WITH MY STAFF.\nI'LL TAKE YOUR COIN IF I WIN; I'LL EVEN WAGER MY HUGE STAFF.")
        if npc == goblin:
            print(npc.name + ": OOH DICE! IF I WIN, I GET A COIN.\nIF YOU CAN SOMEHOW WIN, YOU CAN KEEP DEEZ NUTZ. HAH! GOT EEM!")
            
        user_input = player.user_input()
        print("PLAY DICE GAME? (Y/N)")
        user_input = player.user_input()
        if user_input == "Y":
            die_sides = 20
            player_score = player.roll_die(die_sides)
            npc_score = npc.roll_die(die_sides)
            if npc_score < player_score:
                print("YOU WIN")
                for wager in npc.wager:
                    player.items.append(wager)
                    npc.items.remove(wager)
            elif player_score < npc_score:
                print("YOU LOSE")
                npc.items.append(player.wager)
                player.items.remove(player.wager)
            else:
                print("DRAW")
            user_input = player.user_input()
        else:
           return 

    def main_loop(self,player):
        self.status()
        self.main_menu()
        while True:
            clear()
            self.grid(player)
            player.status()
            self.options(player)
    

class Player():
    def __init__(self):
        self.name = None
        self.pos_x = 0
        self.pos_y = 0
        self.items = []
        self.wager = coin

    def status(self):
        print(str(self.name))
        print("POS X: " + str(self.pos_x))
        print("POS Y: " + str(self.pos_y))
        print("──────────")
        if len(self.items) > 0:
            print("YOU HAVE:")
        for item in self.items:
            print(item.name)
        if len(self.items) > 0:
            print("──────────")

    def user_input(self):
        user_input = input("> ").upper().strip()
        return user_input


    def create(self):    
        clear()
        fancy_text("MENU")
        player.status()    
        print("(N)AME CHARACTER | (H)ELP | (P)LAY GAME")    
        print("──────────")    

        user_input = self.user_input()
        
        if user_input == "N":        
            print("WHAT IS YOUR NAME?")    
            user_input = self.user_input()    
            if len(str(user_input)) > 10 or len(str(user_input)) < 1:    
                print("INVALID NAME LENGTH")    
                user_input = self.user_input()
                self.create()    
            else:    
                self.name = user_input
                self.create()

        elif user_input == "H":
            game.help()

        elif user_input == "P":
            if self.name == None:
                print("FINISH MAKING YOUR CHARACTER")
                user_input = self.user_input()
                self.create()
        else:
            self.create()


    def inventory(self,room):
    
        def pick_up(room_obj_list,player_obj_list):
            for obj in room_obj_list:  
                if obj in room_obj_list:
                    print("PICK UP " + obj.name + "? (Y/N)")
                    user_input = self.user_input()
                    if user_input == "Y":
                        print(self.name + " PICKS UP " + obj.name )
                        user_input = player.user_input()
                        room_obj_list.remove(obj)
                        player_obj_list.append(obj)
                    else:
                        pass
          

        def drop(room):
            if len(self.items) < 1:
                print("NO ITEMS IN INVENTORY")
                user_input = player.user_input()
            else:
                for item in self.items:
                    print("DROP " + item.name + "? (Y/N)")
                    user_input = player.user_input()
                    if user_input == "Y":
                        print("DROPPING " + item.name)
                        user_input = player.user_input()
                        self.items.remove(item)
                        room.items.append(item)
                    else:
                        pass

        def describe(player_obj_list):
            if len(player_obj_list) < 1:
                print("NO ITEMS IN INVENTORY")
                user_input = player.user_input()
            else:
                for obj in player_obj_list:
                    print(obj.name + ": " + obj.desc)
                    user_input = player.user_input()

        print("(P)ICK UP | (D)ROP | (L)OOK | (ENTER) TO RETURN")
        user_input = self.user_input()

        if user_input == "P":
            pick_up(room.items,self.items)
        elif user_input == "D":
            drop(room)
        elif user_input == "L":
            describe(self.items)
        else:
            print("GOING BACK TO MOVEMENT MENU")

    def roll_die(self,die):
        roll = random.randint(1,die)
        print(self.name + " ROLLS: " + str(roll))
        user_input = player.user_input()
        return roll


class Room():
    def __init__(self,name,desc,pos_x,pos_y,npcs,items):
        self.name = name
        self.desc = desc
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.npcs = npcs
        self.items = items
        print("──────────")

    def status(self):
        fancy_text(self.name)
        print(self.desc)
        print("──────────")

        print("YOU SEE:")
        for npc in self.npcs:
            print(npc.name)
#           for item in npc.items:
#               print(item.name)
        for item in self.items:
            print(item.name)
        if len(self.npcs) + len(self.items) > 0:
            print("──────────")

    def interact_npc(self,player):

        def look_npc(self):
            if len(self.npcs) > 0:
                for npc in self.npcs:
                    if len(npc.items) > 0:
                        print("THERE IS " + npc.name + " WITH:")
                        for item in npc.items:
                            print(item.name)
                        user_input = player.user_input()
                    else:
                        print("THERE IS " + npc.name)
                        user_input = player.user_input()
        
        def talk_npc(self,player):
                          
            def no_wager():
                for npc in self.npcs:
                    if npc == witch and note in player.items:
                        player.items.remove(note)
                        npc.items.append(note)
                        print(npc.name + ": YOU HAVE A NOTE FROM DICK?\nOH, HE WANTS THIS. HERE TAKE IT, BUT BE CAREFUL.")
                        npc.items.remove(egg)
                        player.items.append(egg)
                        user_input = player.user_input()
                    elif npc == dick_fetch and note in npc.items:
                        print(npc.name + (": I HAVE A QUEST FOR YOU!\nI WANT YOU TO GET ME A VERY SPECIAL ITEM FROM THE WITCH JUST WEST OF HERE.\nI'LL GIVE YOU MY AXE IF YOU GET IT FOR ME.\nWILL YOU DO IT? (Y/N)"))
                        user_input = player.user_input()
                        if user_input == "Y":
                            npc.items.remove(note)
                            player.items.append(note)
                    elif npc == dick_fetch and egg in player.items:
                        print(npc.name + ": YES! MY EGG! THANK YOU SO MUCH, TAKE MY AXE.")
                        player.items.remove(egg)
                        npc.items.remove(axe)
                        player.items.append(axe)
                        npc.items.append(egg)
                        self.desc = "YOU STAND IN A CLEARING,\nWITH VIVID LIGHT FILTERING IN FROM THE TREES ABOVE.\nA MAN STANDS NEARBY."
                        user_input = player.user_input()
                    elif npc == lumberjack and axe in player.items:
                        print(npc.name + ": OH, YOU HAVE AN AXE.\nSAY, WOULD BE SO KIND AS TO CHOP DOWN THIS TREE? (Y/N)")
                        user_input = player.user_input()
                        if user_input == "Y":
                            print(npc.name + ": DAMMIT, ONE CHOP DIDN'T CUT IT DOWN.\nHEY, IT DID KNOCK SOMETHING SHINY OUT OF THE TREE THOUGH.")
                            user_input = player.user_input()
                            print(npc.name + ": SHIT! IS THAT THE TIME? I GOTTA GO!\nIF YOU WANT A JOB, TALK TO MY IDENTICAL BROTHER DAVE.")
                            self.items.append(dirty_gem)
                            self.npcs.remove(npc)
                            self.desc = "A MASSIVE TREE LOOMS OVER YOU.\nA LUMBERJACK IS RELAXING UNDERNEATH."
                            self.npcs.append(dave)
                            user_input = player.user_input()
                    elif npc == dave and stick in player.items:
                        print(npc.name + ": YOU BROUGHT THE STICK! HERE, TAKE THIS COIN. DON'T LOSE IT GAMBLING!")
                        player.items.remove(stick)
                        npc.items.remove(coin)
                        npc.items.append(stick)  
                        player.items.append(coin)
                        user_input = player.user_input()
                    elif npc == dave and coin not in player.items and stick not in self.items:
                        print(npc.name + ": IF YOU WANT WORK, GO GET ME A STICK.\nI'M A COLLECTER, AND I DON'T WANT TO GET UP.")
                        self.items.append(stick)
                        npc.items.append(coin)
                        user_input = player.user_input()
                    elif npc == hermit and coin in player.items:
                        print(npc.name + ": YOU CAN TAKE MY DICE FOR A COIN. (Y/N)")
                        user_input = player.user_input()
                        if user_input == "Y":
                            player.items.remove(coin)
                            npc.items.remove(dice)
                            npc.items.append(coin)  
                            player.items.append(dice)
                            print(npc.name + ": I CAN FINALLY MOVE OUT OF THIS SHACK! BYE!")
                            self.npcs.remove(npc)
                            user_input = player.user_input()
                    elif npc == potion_brewer and girthy_staff in player.items and deez_nutz in player.items and potion not in player.items:
                        print(npc.name + ": PERFECT, THOSE ARE JUST WHAT IS NEED. FOR MY POTION, I MEAN.\nCAN I HAVE THEM? (Y/N)")
                        user_input = player.user_input()
                        if user_input == "Y":
                            player.items.remove(girthy_staff)
                            player.items.remove(deez_nutz)
                            npc.items.append(girthy_staff)  
                            npc.items.append(deez_nutz)
                            print(npc.name + ": TO SHOW MY GRATITUDE, TAKE THIS POTION.\nIT WILL RESTORE ANY OBJECT SUBMERGED IN IT TO ITS FORMER GLORY.\nSEE ME IF YOU WANT TO USE IT.")
                            npc.items.remove(potion)
                            player.items.append(potion)
                            user_input = player.user_input()
                    elif npc == potion_brewer and potion in player.items:
                        if dirty_gem in player.items:
                            print(npc.name + ": DO YOU WANT TO USE THE POTION ON THAT DISGUSTING GEM? (Y/N)")
                            user_input = player.user_input()
                            if user_input == "Y":
                                print(npc.name + ": OKAY, POUR THE POTION IN THE CAULDRON AND DROP THE SHIT COVERED GEM IN.")
                                player.items.remove(potion)
                                player.items.remove(dirty_gem)
                                self.desc = "THERE'S A HUGE BUBBLING CAULDRON SPEWING NOXIOUS VAPOR.\nA POTION BREWER STANDS NEXT TO IT."
                                user_input = player.user_input()
                                print(npc.name + ": NOW, TAKE THE GEM OUT OF THE POTION.")
                                player.items.append(gem)
                                user_input = player.user_input()
                        else:
                            print(npc.name + ": COME BACK IF YOU HAVE ANYTHING TO USE THE POTION ON.")
                            user_input = player.user_input()
                    else:
                        print(npc.name + ": " + npc.dialog)
                        user_input = player.user_input()

            if len(self.npcs) > 0:
                for npc in self.npcs:
                    if len(npc.wager) > 0 and dice in player.items and player.wager in player.items:
                            for wager in npc.wager:
                                if wager in npc.items:
                                    game.dice_game(player,npc)
                                else:
                                    no_wager()
                               
                    else:
                        no_wager()
                        
        print("(L)OOK | (T)ALK | (ENTER) TO RETURN")
        user_input = player.user_input()

        if user_input == "L":
            look_npc(self)
        elif user_input == "T":
            talk_npc(self,player)
        else:
            print("GOING BACK TO MOVEMENT MENU")



class Character():
  def __init__(self,name,pos_x,pos_y,items,dialog,wager):
    self.name = name
    self.pos_x = pos_x
    self.pos_y = pos_y
    self.items = items
    self.dialog = dialog
    self.wager = wager

  def status(self):
    print(self.name)
    print(self.desc)
    print(str(self.name) + " POS X: " + str(self.pos_x))
    print(str(self.name) + " POS Y: " + str(self.pos_y))

    for item in self.items:
      print("ITEMS: ")
      print(item.name)

  def roll_die(self,die):
    roll = random.randint(1,die)
    print(self.name + " ROLLS: " + str(roll))
    user_input =player.user_input()
    return roll


class Item():
  def __init__(self,name,desc):
    self.name = name
    self.desc = desc

  def status(self):
    print(self.name)
    print(self.desc)


###   INSTANCE ITEM name,desc

###   ITEMS
dirty_gem = Item("BIRD SHIT COVERED GEM","A RARE GEM, ENCRUSTED WITH BIRD SHIT.")
gem = Item("SHINY GEM","A RARE, SHINY GEM.")
deez_nutz = Item("DEEZ NUTZ","HAH, GOT EEM!")
girthy_staff = Item("GIRTHY STAFF", "AKA THE CHODE WAND.")
dice = Item("DICE", "TRY YOUR LUCK.")
axe = Item("AXE","THE AXE GLINTS IN THE LIGHT, UNLESS YOUR'RE SOMEWHERE DARK.")
note = Item("NOTE","THE NOTE READS:\nGIVE THIS UGLY PIECE OF SHIT MY SPECIAL ITEM.\nTHANKS,\nDICK FETCH")
egg = Item("EGG","THIS WAS THE IMPORTANT ITEM? AN EGG?")
dull_axe = Item("DULL AXE","NOT GREAT FOR CHOPPING DOWN TREES, PROBABLY SHOULD HAVE BEEN SHARPENED.\nITS OWNER ISN'T THE SHARPEST AXE IN THE SHED.")
stick = Item("STICK","WEIRD THING TO COLLECT.")
coin = Item("GOLD COIN","IT WOULD BE COOL TO HAVE MORE OF THESE.")
potion = Item("POTION","MAKES AN ITEM SUBMERGED IN IT LIKE BRAND NEW.")

#name,pos_x,pos_y,max_hp,items,dialog,wager

goblin = Character("OBLIN THE GOBLIN",0,0,[deez_nutz],"GOBLIN ON DEEZ NUTZ!",[deez_nutz])
wizard = Character("WIZARD",0,0,[girthy_staff],"YOUR MOM KNOWS ALL ABOUT THIS STAFF.",[girthy_staff])
dick_fetch = Character("DICK FETCH",0,0,[axe,note],"I'M DICK FETCH! I SURE LIKE STANDING HERE!",[note])
witch = Character("WITCH",0,0,[egg],"LEAVE ME ALONE.",[])
lumberjack = Character("LUMBERJACK",0,0,[dull_axe],"I CAN'T CHOP DOWN THIS TREE, AND THAT DICK WON'T LET ME USE HIS AXE.",[])
dave = Character("DAVE",0,0,[coin],"DON'T BOTHER ME IF IT'S NOT IMPORTANT, I'M RELAXING.",[])
hermit = Character("HERMIT",0,0,[dice],"HEY KID! YOU WANT SOME DICE? I'LL GIVE YOU MINE FOR A COIN.",[])
potion_brewer = Character("POTION BREWER",0,0,[potion],"I NEED THINGS. FOR...A POTION. YEAH, A POTION.\n CAN YOU GET ME A THICK, PHALLIC ROD AND SOMETHING TESTICULAR?",[])

###   INSTANCE GAME
game = Game()

###    INSTANCE PLAYER
player = Player()

###   ROOMS        name,desc,pos_x,pos_y,npcs,items
outcropping = Room("OUTCROPPING", "AS YOU APPROACH AN OUTCROPPING OF ROCKS, YOU SMELL A DAMP STENCH\n AND SEE A GOBLIN SQUATTING IN THE SHADOWS.",0,1,[goblin],[])
wizard_tent = Room("WIZARD'S TENT","A WIZARD STANDS UNDER THE SHADE OF A SMALL TENT.",0,0,[wizard],[])
bright_clearing = Room("BRIGHT CLEARING","YOU STAND IN A CLEARING,\nWITH VIVID LIGHT FILTERING IN FROM THE TREES ABOVE.\nA MAN WITH AN AXE STANDS NEARBY.",0,-1,[dick_fetch],[])
stump = Room("STUMP","A WITCH SITS ATOP A LONE STUMP, MOTIONLESS, WAITING.",-1,-1,[witch],[])
tree = Room("GREAT TREE","A MASSIVE TREE LOOMS OVER YOU.\nA LUMBERJACK TRIES TO CHOP IT DOWN TO NO AVAIL.",1,-1,[lumberjack],[])
hermit_hut = Room("HERMIT HUT","YOU SEE AN OLD MAN PEERING OUT OF A HOVEL.",-1,0,[hermit],[])
cauldron = Room("CAULDRON","THERE'S A HUGE EMPTY CAULDRON.\nA POTION BREWER STANDS NEXT TO IT.",1,1,[potion_brewer],[])

rooms =  [outcropping,wizard_tent,bright_clearing,stump,tree,hermit_hut,cauldron]

###   RUN GAME MAIN LOOP
game.main_loop(player)
