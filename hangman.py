import pygame
import random

def loadimages(images):

    for i in range(7):
        image = pygame.image.load("hangman"+str(i)+".png")
        images.append(image)


def drawGameObject():

    x = 30
    y = 450
 
    for i in range(0,26):
        pixel = pygame.draw.rect(game_window,(0,0,0),[x,y,30,30])
        letter = font.render(chr(65+i),True,(255,255,255))
        game_window.blit(letter,(x+6,y))
        buttons.append(pixel)

        if i == 12:
            x = 30
            y += 50
        else:
            x += 60
        
    game_window.blit(images[hangman_status], (150,100))

    display_letters = ""

    for letter in word:
        
        if letter in guess_list:
                display_letters += letter + " "
        else:
            display_letters += "_ "

    w = font2.render(display_letters, True, (0,0,0))
    game_window.blit(w,(480,140))

    if hangman_status == 6:
        wonText = font3.render("You Lose",True,(0,0,0))
        game_window.blit(wonText,(410,270))
        text2 = font.render("Guessing word  = "+word, True, (0,0,0))
        game_window.blit(text2, (451,40))


def draw():

    game_window.fill((255,255,255))
    drawGameObject()
    pygame.display.update()
    clock.tick(FPS)

##########################################################################
pygame.init()                                   
WINDOW_HEIGHT = 600
WINDOW_WIDTH  = 800
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hangman game")
###########################################################################

## load images

images = []
loadimages(images)

# buttons 
buttons = []

# fonts 

font = pygame.font.Font("SourceSansPro-Regular.ttf",25)
font2 = pygame.font.Font("SourceSansPro-Regular.ttf",35)
font3 = pygame.font.Font("SourceSansPro-Regular.ttf",45)

# generate random words from list 
wordlist = []

with open ("wordslist.txt","r") as file:
    wordlist = file.readlines()

wordnum = random.randint(0,854)
word = str(wordlist[wordnum])
word = word[0:len(word)-1]

guessnum = random.randint(0,len(word))
guess_list = []
guess_list.append(word[guessnum])

hangman_status = 0
################# Game Loop ##################
FPS = 30
clock  = pygame.time.Clock()
print(clock)
gameEND = False

while not gameEND:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameEND = True

        if event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            if pos[0] >= 30 and pos[0] <= 60 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("A")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 90 and pos[0] <= 120 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("B")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 150 and pos[0] <= 180 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("C")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 210 and pos[0] <= 240 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("D")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 270 and pos[0] <= 300 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("E")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 330 and pos[0] <= 360 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("F")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 390 and pos[0] <= 420 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("G")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 450 and pos[0] <= 480 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("H")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 510 and pos[0] <= 540 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("I")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 570 and pos[0] <= 600 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("J")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 630 and pos[0] <= 660 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("K")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 690 and pos[0] <= 720 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("L")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 750 and pos[0] <= 780 and pos[1] >= 450 and pos[1] <= 470:
                guess_list.append("M")
                if guess_list[-1] not in word:
                    hangman_status += 1

            #### second row
            if pos[0] >= 30 and pos[0] <= 60 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("N")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 90 and pos[0] <= 120 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("O")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 150 and pos[0] <= 180 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("P")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 210 and pos[0] <= 240 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("Q")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 270 and pos[0] <= 300 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("R")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 330 and pos[0] <= 360 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("S")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 390 and pos[0] <= 420 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("T")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 450 and pos[0] <= 480 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("U")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 510 and pos[0] <= 540 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("V")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 570 and pos[0] <= 600 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("W")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 630 and pos[0] <= 660 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("X")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 690 and pos[0] <= 720 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("Y")
                if guess_list[-1] not in word:
                    hangman_status += 1

            if pos[0] >= 750 and pos[0] <= 780 and pos[1] >= 501 and pos[1] <= 530:
                guess_list.append("Z")
                if guess_list[-1] not in word:
                    hangman_status += 1
            print(pos[0])
            print(pos[1])
            print(buttons[0])

    draw()

    