import linecache
import pyautogui
import os
from PIL import Image 
import PIL 
from time import sleep
import sys
import shutil
current_dir=os.getcwd()
list = sum([len(files) for r, d, files in os.walk(current_dir)])
total_pokemon=int(list)-1
action=(input("State a function:- "))
if action=="Total Pokemon":
    print("The total amount of Pokemon you have is "+str(total_pokemon)+".")
    exit()
else:
    pass
if action=="Create a Pokemon":
    cpcreate=(int(input("Write down the CP of your Pokemon:- ")))
    hpcreate=(int(input("Write down the HP of your Pokemon:- ")))
    namecreate=(input("Write down the name of your Pokemon:- "))
    nicknamecreate=(input("Write down the nickname of your Pokemon:- "))
    new_attack_taughtcreate=(input("Does your Pokemon have 2 charged attacks?:- "))
    caught_locationcreate=(input("Did you catch this Pokemon in the wild or in field research or special research or in a raid?:- "))
    eventcreate=(input("Was this Pokemon caught during an event?:- "))
    datecreate=(input("When was this Pokemon caught?: "))
    ballcreate=(input("In which Pokeball was this Pokemon caught?: "))
    tradedcreate=(input("Was this Pokemon obtained from a trade?: "))
    shinycreate=(input("Is this Pokemon Shiny?: "))
    curentdirplusnamecreate=current_dir+"/"+namecreate
    var=open(os.getcwd()+"/"+"variables_.txt","a+")
    var.write(namecreate)
    var.close()
    var69=open(os.getcwd()+"/"+"variables_2.0.txt","a+")
    var69.write(datecreate)
    var69.close()
    if os.path.exists(curentdirplusnamecreate):
        pass
    else:
        os.mkdir(curentdirplusnamecreate)
    os.chdir(current_dir+"/"+namecreate)
    list = os.listdir(curentdirplusnamecreate)
    noExistPokemon = len(list)
    os.mkdir(curentdirplusnamecreate+"/"+namecreate+"-"+datecreate+"-"+str(noExistPokemon))
    os.chdir(curentdirplusnamecreate+"/"+namecreate+"-"+datecreate+"-"+str(noExistPokemon))
    nameanddatecreate=namecreate+"-"+datecreate+"-"+str(noExistPokemon)+".txt"
    createpokemon=open(nameanddatecreate,"a+")
    createpokemon.write("CP="+str(cpcreate))
    createpokemon.write("\n")
    createpokemon.write("HP="+str(hpcreate))
    createpokemon.write("\n")
    createpokemon.write("Name="+namecreate)
    createpokemon.write("\n")
    createpokemon.write("Nickname="+nicknamecreate)
    createpokemon.write("\n")
    createpokemon.write("New_Attack_Taught="+new_attack_taughtcreate)
    createpokemon.write("\n")
    createpokemon.write("Caught_Location="+caught_locationcreate)
    createpokemon.write("\n")
    createpokemon.write("Event="+eventcreate)
    createpokemon.write("\n")
    createpokemon.write("Date="+str(datecreate))
    createpokemon.write("\n")
    createpokemon.write("Caught_In="+ballcreate)
    createpokemon.write("\n")
    createpokemon.write("Traded="+tradedcreate)
    createpokemon.write("\n")
    createpokemon.write("Shiny="+shinycreate)
    createpokemon.write("\n")
    createpokemon.close()
    var69420=curentdirplusnamecreate+"/"+namecreate+"-"+datecreate+"-"+str(noExistPokemon)
    var69420dir=current_dir+"/directoryToSwitchTo.txt"
    var_69420=open(var69420dir, "a+")
    var_69420.write(var69420)
    var_69420.close()
    print("The Pokemon has been created.")
    dir_name=curentdirplusnamecreate+"/"+namecreate+"-"+datecreate+"-"+str(noExistPokemon)
    screenshots=input("Do you wanna take screenshots of the Pokemon you just created?: ")
    if screenshots=="Yes":
        print("Alright, switch to scrcpy or any other screen mirroring application quick.")
        sleep(5)
        from ivchecking import ivchecking
        ivchecking()
        dir_name=curentdirplusnamecreate+"/"+namecreate+"-"+datecreate+"-"+str(noExistPokemon)
        print("Done! The Pokemon has been created again but with more info.")
    else:
        print("Okay then.")
        pass
else:
    pass
def main():
    cp=linecache.getline(pkmn, 1)
    cp=cp[3:]
    print(cp)
    hp=linecache.getline(pkmn, 2)
    hp=hp[3:]
    print(hp)
    name=linecache.getline(pkmn, 3)
    name=name[5:]
    print(name)
    nickname=linecache.getline(pkmn, 4)
    nickname=nickname[9:]
    print(nickname)
    new_attack_taught=linecache.getline(pkmn, 5)
    new_attack_taught=new_attack_taught[18:]
    print(new_attack_taught)
    caught_location=linecache.getline(pkmn, 6)
    caught_location=caught_location[16:]
    print(caught_location)
    event=linecache.getline(pkmn, 7)
    event=event[6:]
    print(event)
    date=linecache.getline(pkmn, 8)
    date=date[5:]
    print(date)
    caught_in=linecache.getline(pkmn, 9)
    caught_in=caught_in[10:]
    print(caught_in)
    traded=linecache.getline(pkmn, 10)
    traded=traded[7:]
    print(traded)
if action=="Information":
    pkmnname=(input("Write down the name of the Pokemon you wanna know stuff about:- "))
    os.chdir(current_dir+"/"+pkmnname)
    pkmndate=(input("when was this Pokemon Caught?:- "))
    pkmn=pkmnname+"-"+pkmndate+".txt"
    main()
    exit()
else:
    pass