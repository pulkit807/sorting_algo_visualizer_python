import pygame
import random 
pygame.font.init() 
screen = pygame.display.set_mode((900, 650)) 
pygame.display.set_caption("SORTING VISUALISER") 
run = True
width = 900

length = 600

array =[0]*151

arr_clr =[(0, 204, 102)]*151

clr_ind = 0

clr =[(0, 204, 102), (255, 0, 0),  

(0, 0, 153), (255, 102, 0)] 

fnt = pygame.font.SysFont("comicsans", 30) 

fnt1 = pygame.font.SysFont("comicsans", 20) 


def generate_arr(): 

    for i in range(1, 151): 

        arr_clr[i]= clr[0] 

        array[i]= random.randrange(1, 100) 
generate_arr()  

def refill(): 

    screen.fill((255, 255, 255)) 

    draw() 

    pygame.display.update() 

    pygame.time.delay(20) 

def mergesort(array, l, r): 

    mid =(l + r)//2

    if l<r: 

        mergesort(array, l, mid) 

        mergesort(array, mid + 1, r) 

        merge(array, l, mid, mid + 1, r) 


def merge(array, x1, y1, x2, y2): 

    i = x1 

    j = x2 

    temp =[] 

    pygame.event.pump()  

    while i<= y1 and j<= y2: 

        arr_clr[i]= clr[1] 

        arr_clr[j]= clr[1] 

        refill() 

        arr_clr[i]= clr[0] 

        arr_clr[j]= clr[0] 

        if array[i]<array[j]: 

                temp.append(array[i]) 

                i+= 1

        else: 

                temp.append(array[j]) 

                j+= 1

    while i<= y1: 

        arr_clr[i]= clr[1] 

        refill() 

        arr_clr[i]= clr[0] 

        temp.append(array[i]) 

        i+= 1

    while j<= y2: 

        arr_clr[j]= clr[1] 

        refill() 

        arr_clr[j]= clr[0] 

        temp.append(array[j]) 

        j+= 1

    j = 0    

    for i in range(x1, y2 + 1):  

        pygame.event.pump()  

        array[i]= temp[j] 

        j+= 1

        arr_clr[i]= clr[2] 

        refill() 

        if y2-x1 == len(array)-2: 

            arr_clr[i]= clr[3] 

        else:  

            arr_clr[i]= clr[0] 

def draw(): 
    txt = fnt.render("PRESS 'ENTER' TO PERFORM SORTING.", 1, (0, 0, 0)) 

    screen.blit(txt, (20, 20)) 

    txt1 = fnt.render("PRESS 'R' FOR NEW ARRAY.", 1, (0, 0, 0)) 

    screen.blit(txt1, (20, 40)) 

    txt2 = fnt1.render("ALGORITHM USED: MERGE SORT", 1, (0, 0, 0)) 

    screen.blit(txt2, (600, 60)) 

    element_width =(width-150)//150

    boundry_arr = 900 / 150

    boundry_grp = 550 / 100

    pygame.draw.line(screen, (0, 0, 0),  (0, 95), (900, 95), 6) 

    for i in range(1, 100): 

        pygame.draw.line(screen,  

                        (224, 224, 224),  

                        (0, boundry_grp * i + 100),  

                        (900, boundry_grp * i + 100), 1) 

    for i in range(1, 151): 

        pygame.draw.line(screen, arr_clr[i],

            (boundry_arr * i-3, 100),

            (boundry_arr * i-3, array[i]*boundry_grp + 100),

            element_width) 

while run: 

    screen.fill((255, 255, 255)) 

    for event in pygame.event.get(): 

        if event.type == pygame.QUIT: 

            run = False

        if event.type == pygame.KEYDOWN: 

            if event.key == pygame.K_r: 

                generate_arr()  

            if event.key == pygame.K_RETURN: 

                mergesort(array, 1, len(array)-1)      
    draw() 
    pygame.display.update() 

pygame.quit() 