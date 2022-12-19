import pyautogui
import pytesseract
from pymem import *
from pymem.process import *
from PIL import ImageGrab
from PIL import Image, ImageOps
import cv2
import numpy as np
import time
import string
from stopwatch import Stopwatch
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


citizen_info = (20,1006) #Dwarf portrait on lower left of screen location with (x,y) coordinates, used to bring up Creatures/Citizens, otherwise brought up with hotkey 'U'.
magni_glass_list = [(478,196),(478,241),(478,286),(478,331),(478,376),(478,421),(478,466),(478,511),(478,556),(478,601),(478,646),(478,691),(478,736),(478,781),(478,826),(478,871),(478,916)] #This is the location of the magnifying glass associated with a dwarf in creatures/citizens table, used to open that particular dwarf's character dossier.
quill = (1467,117) #Location of the quill in the Dwarf dossier to open up the name changer. Use this to get the dwarf_name_coords and dwarf_title_coords
dwarf_name_coords = (1074,104,1398,140)
dwarf_title_coords = (1074,149,1398,185)
attributes = (1247,249,1539,344) # Coordinate box for Dwarf attributes
down_arrow = (1611,931)
alphabet = set(string.ascii_letters) # tuple of uppercase and lowercase letters in alphabet
population = 0

fortress_population = []
badlist = ['ovr metatetstty','Ualues sacrifice','Obst inate','Disdains hard vork','Ualues independence','Values decorun','High social avareness']
goodlist = ['Good intuition','Values sacrifice','Obstinate','Disdains hard work','Values independence','Values decorum','High social awareness']
stopwatch = Stopwatch()

def checkPop():
    global population
    if population == 0:
        mem = Pymem("Dwarf Fortress.exe")
        module = module_from_name(mem.process_handle,"Dwarf Fortress.exe").lpBaseOfDll
        population += mem.read_int(module + 0x1DA19CC)
    else:
        population = 0
        mem = Pymem("Dwarf Fortress.exe")
        module = module_from_name(mem.process_handle,"Dwarf Fortress.exe").lpBaseOfDll
        population += mem.read_int(module + 0x1DA19CC)

def checkAttr():
    dwarf_counter = 0
    time.sleep(1)
    if population == 0:
        print("You Need To Establish Population First")
    if population <= 17:
        fortress_population.clear()
        for dwarf_number in range(0,population):
            pyautogui.mouseDown(citizen_info)
            pyautogui.mouseUp()
            pyautogui.mouseDown(magni_glass_list[dwarf_number])
            pyautogui.mouseUp()
            pyautogui.mouseDown(quill)
            ImageGrab.grab(dwarf_name_coords).save('dwarf_name.png')
            ImageGrab.grab(dwarf_title_coords).save('dwarf_title.png')
            image = Image.open('dwarf_name.png')
            dwarf_name_string = pytesseract.image_to_string('dwarf_name.png')
            image = Image.open('dwarf_title.png')
            dwarf_title_string = pytesseract.image_to_string('dwarf_title.png')
            ImageGrab.grab(attributes).save('attributes.png')
            image = Image.open('attributes.png')
            attributes_string = pytesseract.image_to_string('attributes.png')
            attributes_list = []
            attributes_spell = []
            for letter in attributes_string:
                if letter in alphabet or letter == " " or letter == "-":
                    attributes_spell.append(letter)
                else:
                    if len(attributes_spell) > 1:
                        attributes_list.append(''.join(attributes_spell))
                        attributes_spell.clear()
            dwarf_name = dwarf_name_string.strip()
            dwarf_title = dwarf_title_string.strip()
            dorfciv = []
            dorfciv.append(dwarf_name)
            dorfciv.append(dwarf_title)
            for trait in attributes_list:
                if trait in badlist:
                    goodListReplace = badlist.index(trait)
                    attributes_list[attributes_list.index(trait)] = goodlist[goodListReplace]
            dorfciv.append(attributes_list)
            fortress_population.append(dorfciv)
        print(fortress_population)

    if population > 17:
        fortress_population.clear()
        for dwarf_number in range(0,17):
            pyautogui.mouseDown(citizen_info)
            pyautogui.mouseUp()
            pyautogui.mouseDown(magni_glass_list[dwarf_number])
            pyautogui.mouseUp()
            pyautogui.mouseDown(quill)
            ImageGrab.grab(dwarf_name_coords).save('dwarf_name.png')
            ImageGrab.grab(dwarf_title_coords).save('dwarf_title.png')
            image = Image.open('dwarf_name.png')
            dwarf_name_string = pytesseract.image_to_string('dwarf_name.png')
            image = Image.open('dwarf_title.png')
            dwarf_title_string = pytesseract.image_to_string('dwarf_title.png')
            ImageGrab.grab(attributes).save('attributes.png')
            image = Image.open('attributes.png')
            attributes_string = pytesseract.image_to_string('attributes.png')
            attributes_list = []
            attributes_spell = []
            for letter in attributes_string:
                if letter in alphabet or letter == " " or letter == "-":
                    attributes_spell.append(letter)
                else:
                    if len(attributes_spell) > 1:
                        attributes_list.append(''.join(attributes_spell))
                        attributes_spell.clear()
            dwarf_name = dwarf_name_string.strip()
            dwarf_title = dwarf_title_string.strip()
            dorfciv = []
            dorfciv.append(dwarf_name)
            dorfciv.append(dwarf_title)
            for trait in attributes_list:
                if trait in badlist:
                    goodListReplace = badlist.index(trait)
                    attributes_list[attributes_list.index(trait)] = goodlist[goodListReplace]
            dorfciv.append(attributes_list)
            fortress_population.append(dorfciv)
        for downClickz in range(1, population - 16):
            counter_mouseclick = 0
            pyautogui.mouseDown(citizen_info)
            pyautogui.mouseUp()
            while counter_mouseclick < downClickz:
                pyautogui.mouseDown(down_arrow)
                counter_mouseclick += 1
            pyautogui.mouseDown(magni_glass_list[-1])
            pyautogui.mouseUp()
            pyautogui.mouseDown(quill)
            ImageGrab.grab(dwarf_name_coords).save('dwarf_name.png')
            ImageGrab.grab(dwarf_title_coords).save('dwarf_title.png')
            image = Image.open('dwarf_name.png')
            dwarf_name_string = pytesseract.image_to_string('dwarf_name.png')
            image = Image.open('dwarf_title.png')
            dwarf_title_string = pytesseract.image_to_string('dwarf_title.png')
            ImageGrab.grab(attributes).save('attributes.png')
            image = Image.open('attributes.png')
            attributes_string = pytesseract.image_to_string('attributes.png')
            attributes_list = []
            attributes_spell = []
            for letter in attributes_string:
                if letter in alphabet or letter == " " or letter == "-":
                    attributes_spell.append(letter)
                else:
                    if len(attributes_spell) > 1:
                        attributes_list.append(''.join(attributes_spell))
                        attributes_spell.clear()
            dwarf_name = dwarf_name_string.strip()
            dwarf_title = dwarf_title_string.strip()
            dorfciv = []
            dorfciv.append(dwarf_name)
            dorfciv.append(dwarf_title)
            for trait in attributes_list:
                if trait in badlist:
                    goodListReplace = badlist.index(trait)
                    attributes_list[attributes_list.index(trait)] = goodlist[goodListReplace]
            dorfciv.append(attributes_list)
            fortress_population.append(dorfciv)        
                
                
            

                    

            
checkPop()
checkAttr()
            
            
            
            
