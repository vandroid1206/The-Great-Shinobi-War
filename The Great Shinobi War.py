import time
import random

#Character Class
class Characters :
    def __init__(self , name , hp , atk , spatk , defe , spdef , speed , chakra , iq) -> None:
        self.hp = hp
        self.atk = atk
        self.spatk = spatk
        self.defe = defe
        self.spdef = spdef
        self.speed = speed
        self.chakra = chakra
        self.iq = iq
        self.name = name
    
    #Moves that damage the opponent
    def damaging_move(self , name , power , accuracy , type , chakra , target):
        self.dmg = 0
        misses = random.randint(range(100))
        if misses <= accuracy :
            if type == "atk" :
                self.dmg = (self.atk * power) / target.defe
                print(self.dmg)
                target.hp -= self.dmg
                self.chakra -= chakra
                print(target.hp)
            elif type == "spatk" :
                self.dmg = (self.spatk * power) / target.spdef
                print(self.dmg)
                target.hp -= self.dmg
                self.chakra -= chakra
                print(target.hp)
        else :
            print(target.name , "Dodged" , name)

#Creating characters using the Characters class
chars = {"Uchiha Madara" : [["Uchiha Madara" , 1250 , 240 , 260 , 175 , 150 , 190 , 1900 , 150] , ["Taijutsu/Weapon" , "Fire Style Majestic Destroyer Flame" , "Summoning Jutsu : Kurama" , "Shattered Heaven" , "Izanagi" , "Beast Bomb" , "Infinite Sukiyomi"] , ["Sussanoo" , "Sussanoo cloaked Kurama" , "Sage of six Paths"]] , "Hashirama Senju" : [["Hashirama Senju" , 1500 , 250 , 245 , 190 , 200 , 190 , 2500 , 140] , ["Taijutsu/Weapon","Wood Golem Jutsu" ,"Rashomon Gates" , "Wood Dragon Jutsu","Deep Forest Emergence Jutsu","Shin Susenju : True Several Thousand Hands Cannon" , "Earth Style : Swamp of the Underworld"] , ["Sage Mode" , "Chakra Healing"]] , "Uzumaki Naruto" : [["Uzumaki Naruto" , 950 , 185 , 195 , 165 , 175 , 180 , 3000 , 145] , ["Taijutsu/Weapon" , "Wind Style RasenShuriken" , "Lava Release RasenShuriken" , "Frog Kata Style" , "Planetary Rasengan" , "Super Tailed Beast RasenShuriken" , "Six Paths : Ultra Tailed Beast RasenShurikens"] , ["KCM Mode" , "Sage Mode" , "Baryon Mode" , "Ashura Mode"]] , "Hatake Kakashi" : [["Hatake Kakashi" , 900 , 180 , 200 , 155 , 170 , 200 , 1400 , 175 ] , ["Taijutsu/Weapon","Raikiri" , "Shiden" , "Chidori" , "Earth Release : Earth Style Wall" , "Kamui" , "Lightning Style : Raiden" , "Kamui Shuriken" , "Kamui Raikiri"] , ["DMS Kakashi"]] , "Might Guy" : [["Might Guy" , 1050 , 230 , 140 , 175 , 190 , 175 , 1850 , 135 ] , ["Master of Taijutsu" , "Sekizō : Evening Elephant" , "Strong Fist" , "Hidden Lotus" , "Yagai : Night Guy" , "Hirudora : Daytime Tiger" , "Asa kujaku : Morning Peacock"] , ["7th Gate of Wonder" , "8th Gate of Death"]] , "Tobirama Senju" : [["Tobirama Senju" , 1800 , 310 , 335 , 245 , 275 , 400 , 2500 , 200] , ["Blade of the Thunder Spirit" , "Edo Tensei" , "Flying Raijin" , "Water Style : Severing Waves" , "Gojo Kibaku Fuda" , "Water Style : Water Wall"] , ["Uchiha Hatred"]] , "Uchiha Itachi" : [["Uchiha Itachi" , 975 , 165 , 280 , 190 , 210 , 180 , 1450 , 175] , ["Taijutsu/Weapon" , "Amaterasu" , "Tsukuyomi" , "Izanami" , "Fire Style : Phoenix Sage Flower Nail Crimson" , "Water Style : Water Dragon Bullets" , "Demonic Illusion : Mirage Crow"] , ["Master if Genjutsu" , "Susanoo"]]}

#Data of all the moves
moves = {"Fire Style Majestic Destroyer Flame" : [[90 , 80 , "spatk" , 250] , "damaging_move"] , "Shattered Heaven" : [[135 , 90 , "atk" , 400] , "damaging_move"] , "Wood Dragon Jutsu" : [[95 , 80 , "spatk" , 225] , "damaging_move"] , "Deep Forest Emergence Jutsu" : [[120 , 95 , "atk" , 340] , "damaging_move"]}


result = False

#Showing the list of characters
for i in enumerate(chars.keys()):
    print(i)

#Choosing p1
P1 = Characters(*chars[list(chars)[int(input("Player 1 choose a character with the index number "))]][0])
while P1 not in [i[0] for i in enumerate(chars.keys())] :
    print("Please choose a valid index number")
    P1 = Characters(*chars[list(chars)[int(input("Player 1 choose a character with the index number "))]][0])

for i in enumerate(chars.keys()):
    print(i)

#Choosing p2
P2 = Characters(*chars[list(chars)[int(input("Player 1 choose a character with the index number "))]][0])
while P2 not in [i[0] for i in enumerate(chars.keys())] :
    print("Please choose a valid index number")
    P2 = Characters(*chars[list(chars)[int(input("Player 1 choose a character with the index number "))]][0])

#Sorting the above chosen characters according to their speed
fighters = sorted([(chars[list(chars)[P1]][0].name , chars[list(chars)[P1]][0].speed) , (chars[list(chars)[P2]][0].name , chars[list(chars)[P2]][0].speed)] , reverse=False)
print(fighters)

#Main gameplay
while result == False :
    #Character Select P1
    for i in enumerate(chars[list(chars)[P1]][1]) :
        print(i)
    p1 = int(input())
    while p1 not in [i[0] for i in enumerate(chars[list(chars)[P1]][1])] :
        p1 = int(input())
    
    #Character Select P2
    for i in enumerate(chars[list(chars)[P2]][1]) :
        print(i)
    p2 = int(input())
    while p2 not in [i[0] for i in enumerate(chars[list(chars)[P2]][1])] :
        p2 = int(input())
    
    #Implementing the attacks/moves

    for i in fighters : 
        chars[list(chars)[P1]][0].damaging_move(chars[list(chars)[P1]][1][p1] , *moves[chars[list(chars)[P1]][1][p1][0]] , chars[list(chars)[P2]][0])
