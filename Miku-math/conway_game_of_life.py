import pygame as pg
from pygame.locals import *
import random
import time

import streamlit as st

pg.init()

ScreenWidth = 1500
ScreenHeight = 900
screen = pg.display.set_mode((ScreenWidth, ScreenHeight))
pg.display.set_caption(f'Conway, game of life [generation: 0 ] : start')

FPS = 60

row = {}

NeihtborAliveState = []
NeihtborDeathState = []
class Cell():
    def __init__(self, x, y, widght ,height):
        self.state = False #bool(random.randrange(0,2))
        self.x = x
        self.y = y
        self.widght = widght
        self.height = height
        self.myself = pg.Rect(self.x, self.y, self.widght, self.height)

    def Create(self):   
        if self.state == True:
            pg.draw.rect(screen, "white", self.myself)
        elif self.state == False:
            pg.draw.rect(screen, "dark grey", self.myself)

    def OnClick(self):
        if self.myself.collidepoint(pg.mouse.get_pos()):
           self.state = not self.state
           self.Create()
           return True

    def CheckSur(self,villageName, Birthrow):    
        global NeihtborDeathState, NeihtborAliveState
        ListOfVillageName = list(row)
        neighbor = []
        aliveNeightbor = 0
        try:
           pos = Birthrow.index(self)
           #print(pos)
        except ValueError:
            print("ไม่พบ")

        for i, key in enumerate(row):
            if key == villageName:

                BornRow = i 
                #print(ListOfVillageName[BornRow])'
                #print(underVillage[pos])
                if key == "row_0":
                    underVillage = row[ListOfVillageName[i+1]]
                    if pos == 0:
                        neighbor = [
                            Birthrow[pos+1],
                            underVillage[pos],
                            underVillage[pos+1]
                            ]
                    elif pos == int(ScreenWidth/25)-1:
                        neighbor = [
                            Birthrow[pos-1],
                            underVillage[pos-1],
                            underVillage[pos],
                            ]
                    else:
                        neighbor = [
                            Birthrow[pos-1],
                            Birthrow[pos+1],
                            underVillage[pos-1],
                            underVillage[pos],
                            underVillage[pos+1]
                        ]
                elif key == f"row_{int(ScreenWidth/25)-1}":
                    upperVillage = row[ListOfVillageName[i-1]]
                    if pos == 0:
                        neighbor = [
                            Birthrow[pos+1],
                            upperVillage[pos],
                            upperVillage[pos+1]
                            ]
                    elif pos == int(ScreenWidth/25)-1:
                        neighbor = [
                            Birthrow[pos-1],
                            upperVillage[pos-1],
                            upperVillage[pos],
                            ]
                    else:
                        neighbor = [
                            Birthrow[pos-1],
                            Birthrow[pos+1],
                            upperVillage[pos-1],
                            upperVillage[pos],
                            upperVillage[pos+1]
                            ]  
                else:
                    upperVillage = row[ListOfVillageName[i-1]]
                    underVillage = row[ListOfVillageName[i+1]]                    
                    if pos == 0:
                        neighbor = [
                            Birthrow[pos+1],
                            upperVillage[pos],
                            upperVillage[pos+1],
                            underVillage[pos],
                            underVillage[pos+1]
                            ]
                    elif pos == int(ScreenWidth/25)-1:
                        neighbor = [
                            Birthrow[pos-1],
                            upperVillage[pos-1],
                            upperVillage[pos],
                            underVillage[pos],
                            underVillage[pos-1]                            
                            ]
                    else:
                        neighbor = [
                            Birthrow[pos-1],
                            Birthrow[pos+1],
                            upperVillage[pos-1],
                            upperVillage[pos],
                            upperVillage[pos+1],
                            underVillage[pos],
                            underVillage[pos-1],
                            underVillage[pos+1]                      
                            ]            
                break
        else:
            print("Key not found")
        for alive in neighbor:
            if alive.state == True:
                aliveNeightbor += 1

        if self.state == True:
            if aliveNeightbor < 2 or aliveNeightbor > 3:
               NeihtborDeathState += [self]
        elif self.state == False:
            if aliveNeightbor == 3:
                NeihtborAliveState += [self]
        #print(neighbor)

#สร้างตาราง cell

for loop in range(0,int(ScreenWidth/25)):
    comRow = []
    for i in range(0,int(ScreenWidth/25)):
        cell = Cell((25*i)+2,25*loop,21.5,21.5)
        cell.Create()
        comRow.append(cell)
        #print(i)

    row[f"row_{loop}"] = comRow
    
#เกมทำงาน
#print(row["row_1"][0])
generation = 0
run = True
start = False
clock = pg.time.Clock()
while run:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        #ตรวจการคลิก

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                start = not start
                print(start)
            if event.key == pg.K_d:
               for village in row.values():
                    #print(i)
                    generation = 0
                    for member in village:
                        member.state = False 
                        member.Create()

        if event.type == pg.MOUSEBUTTONDOWN and start == False:
            #ตรวจว่าคลิกตรงไหน
            found = False
            for village in row.values():
                #print(i)
                for member in village:
                    found = member.OnClick()
                    if found == True:
                      break
                if found == True:
                    break    
    if start == True:
        for villageName, village in row.items():
                    #print(i)
                    for member in village:
                        member.CheckSur(villageName, village)
                        member.Create() 

        for member in NeihtborAliveState:
            member.state = True
        for member in NeihtborDeathState:
            member.state = False       
        NeihtborAliveState.clear()
        NeihtborDeathState.clear()

    if start == True:
        pg.display.set_caption(f'Conway, game of life [ generation: {generation} ] status: start')
        generation += 1
    elif start == False:
        pg.display.set_caption(f'Conway, game of life [generation: {generation}] status: pause')
    pg.display.flip()
    time.sleep(0.01)
pg.quit