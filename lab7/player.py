import pygame


pygame.init()

AlemPath=r"C:\Users\abdim\Desktop\PP2\musics\ALEM_-_Kuiim_78724411.mp3"
BrunoPath=r"C:\Users\abdim\Desktop\PP2\musics\Bruno_Mars_-_Grenade_48078109.mp3"
MotPath=r"C:\Users\abdim\Desktop\PP2\musics\MoT_-_Avgust_-_jeto_ty_74130517.mp3"

screen=pygame.display.set_mode((400, 400))
pygame.display.set_caption("MP3 PLAYER")

clock=pygame.time.Clock()
image=pygame.image.load(r"C:\Users\abdim\Desktop\PP2\unnamed.jpg")
image = pygame.transform.scale(image, (400, 400))

musicList = [AlemPath, BrunoPath, MotPath]
pygame.mixer.music.load(musicList[0]) 

pygame.mixer.music.play(-1)

Play=False
running=True

musicNames = ["Kuim", "Grenade", "August"]

font = pygame.font.SysFont(None, 36)

index=0
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             running=False
             
    
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                Play=not Play
                
                if Play:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause() 
                    
            elif event.key==pygame.K_RIGHT:
                index+=1
                if index==len(musicList):
                    index=0
                pygame.mixer.music.load(musicList[index])   
                pygame.mixer.music.play() 
                
            elif event.key==pygame.K_LEFT:
                index-=1
                if index==-1:
                    index=len(musicList)-1
                pygame.mixer.music.load(musicList[index])   
                pygame.mixer.music.play()  
    screen.blit(image,(0,0))
    pygame.draw.rect(screen, (0, 0, 0), (20, 20, 200, 40))
    text_surface = font.render(musicNames[index], True, (255, 255, 255))
    screen.blit(text_surface, (20, 20))
                
    pygame.display.flip()   
    clock.tick(60)