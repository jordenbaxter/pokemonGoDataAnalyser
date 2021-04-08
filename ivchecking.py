import pyautogui
import os
from time import sleep

path_parent=os.path.dirname(os.getcwd())
os.chdir(path_parent)
patth_parent=os.path.dirname(os.getcwd())
os.chdir(patth_parent)

thingy=os.getcwd()+"/"+"variables_.txt"
fileVar=open(thingy,"r")
namecreate=fileVar.readline()
fileVar.close()

thingything=os.getcwd()+"/"+"variables_2.0.txt"
fileyVar=open(thingything, "r")
datecreate=fileyVar.readline()
fileyVar.close()

thingythingything=os.getcwd()+"/directoryToSwitchTo.txt"
fileyFileVar=open(thingythingything, "r")
directory=fileyFileVar.readline()
fileyFileVar.close()
os.remove("variables_.txt")
os.remove("variables_2.0.txt")
os.remove("directoryToSwitchTo.txt")
os.chdir(directory)


def ivchecking():
    pyautogui.click(x=540, y=671)
    pyautogui.moveTo(x=1160, y=395)
    ss=pyautogui.screenshot(region=(520, 48, 325, 680))
    ss=ss.save(namecreate+"-"+datecreate+"-"+"-screenshot 1"+".png")
    pyautogui.click(x=797, y=685)
    sleep(0.2)
    pyautogui.click(x=772, y=561)
    sleep(0.2)
    pyautogui.click(x=772, y=562)
    sleep(0.2)
    pyautogui.click(x=772, y=562)
    sleep(0.19)
    pyautogui.click(x=772, y=562)
    sleep(0.3)
    ss1=pyautogui.screenshot(region=(520, 48, 325, 680))
    ss1=ss1.save(namecreate+"-"+datecreate+"-"+"-screenshot 2"+".png")
    pyautogui.click(x=541, y=667)
    sleep(0.2)
    pyautogui.moveTo(x=541, y=667)
    pyautogui.mouseDown(button="left")
    sleep(0.2)
    pyautogui.moveTo(x=536, y=469)
    sleep(0.1)
    pyautogui.mouseUp(button="left")
    sleep(0.3)
    ss2=pyautogui.screenshot(region=(520, 48, 325, 680))
    ss2=ss2.save(namecreate+"-"+datecreate+"-"+"-screenshot 3"+".png")
    pass