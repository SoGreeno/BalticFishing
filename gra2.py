import pygame
import time
from colorama import init, Fore #, Back, Style

# resetuj kolory w terminalu
init(autoreset=True)

pygame.init()

window_width = 100
window_height = 100
okno = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption("Baltic Fishing")

ocean = pygame.image.load("ocean.png")
player = pygame.image.load("lodz.png")
ryba = pygame.image.load("ryba.png")
port = pygame.image.load("port.png")

splash = pygame.image.load("splash.png")

okno.blit(splash, (0, 0))
pygame.display.flip()
time.sleep(1.5)

# pozycja startu gracza
player_x = 25
player_y = 25

# ustawianie portu, oceanu i ikony ryb (której o dziwo nie ma)
ocean_koordynaty = [(0, 0), (50, 0), (0, 50), (50, 50)]
for koordocean in ocean_koordynaty:
    okno.blit(ocean, koordocean)
    
ryba_koordynaty = [(0,0)]
for koordryba in ryba_koordynaty:
    okno.blit(ryba, koordryba)
    
port_koordynaty = [(35,0)]
for koordoport in port_koordynaty:
    okno.blit(port, koordoport)

# zmienne
player_speed = 5
max_player_speed = 13
przyPorcie = False
zdobyteRyby = 0

def ulepszSzybkosc():
    global player_speed
    global zdobyteRyby
    if player_speed < max_player_speed:
    	player_speed += 2
#    	zdobyteRyby -= 2
    	print(Fore.GREEN + "Ulepszono łódź: " + str(player_speed))
    else:
    	print(Fore.RED + "Osiągnięto maksymalną prędkość. Ulepszenie jest niemożliwe")

def Status():
	print(Fore.YELLOW + "STATUS")
	print("")
	print("Szybkość: " + str(player_speed))
	print("Ryby: " + str(zdobyteRyby))
	
clock = pygame.time.Clock()

# kontrolki
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Wychodzenie z gry...")
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y -= player_speed
            elif event.key == pygame.K_DOWN:
                player_y += player_speed
            elif event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed
            elif event.key == pygame.K_l:
            	print("Wychodzenie z gry...")
            	quit()
            elif event.key == pygame.K_u and przyPorcie:
            	ulepszSzybkosc()
            elif event.key == pygame.K_s:
            	Status()

    player_rect = player.get_rect(topleft=(player_x, player_y))

    okno.fill((0, 0, 0))
    
    for koordocean in ocean_koordynaty:
        okno.blit(ocean, koordocean)
        
    for koordryba in ryba_koordynaty:
        okno.blit(ocean, koordryba)
    	
    for koordoport in port_koordynaty:
    	okno.blit(port, koordoport)
    	
    if player_rect.colliderect(pygame.Rect(port_koordynaty[0], port.get_size())):
    	przyPorcie = True
    else:
    	przyPorcie = False
    	
    okno.blit(player, player_rect)

    pygame.display.flip()

    clock.tick(60)
