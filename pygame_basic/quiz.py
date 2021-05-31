import pygame
import random
###################################################################
#기본 초기화 (반드시 해야하는 것들)
pygame.init() 

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임 이름") # 게임 이름

#FPS
clock = pygame.time.Clock()
###################################################################

#1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#배경화면 불러오기
background = pygame.image.load("C:/Users/지호/Desktop/python workspace/pygame_basic/background.png")
#캐릭터 불러오기
chracter = pygame.image.load("C:/Users/지호/Desktop/python workspace/pygame_basic/chracter.png")
chracter_size = chracter.get_rect().size #이미지의 크기를 구해옴
chracter_width = chracter_size[0] #캐릭터 가로 크기
chracter_height = chracter_size[1] #캐릭터 세로 크기 
chracter_x_pos = (screen_width/2) - (chracter_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
chracter_y_pos = screen_height - chracter_height #화면 세로의 제일 아래에 위치
#적 불러오기
enemy = pygame.image.load("C:/Users/지호/Desktop/python workspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터 가로 크기
enemy_height = enemy_size[1] #캐릭터 세로 크기 
enemy_x_pos = random.randrange(0,screen_width-chracter_width) #랜덤
enemy_y_pos = 0 #화면 세로의 제일 위에 위치

#이동할 좌표
to_x = 0

#이동 속도
chracter_speed = 0.6
enemy_speed = 5


running = True 
while running:
    dt = clock.tick(30) #게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= chracter_speed
            elif event.key == pygame.K_RIGHT:
                to_x += chracter_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    #가로 경계값 처리
    if chracter_x_pos < 0:
        chracter_x_pos = 0
    elif chracter_x_pos > screen_width - chracter_width:
        chracter_x_pos = screen_width - chracter_width
         
    #3. 게임 캐릭터 위치 정의
    chracter_x_pos += to_x * dt
    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randrange(0,screen_width-chracter_width)
    #4. 충돌 처리
    #충돌 처리를 위한 rect정보 받아오기
    chracter_rect = chracter.get_rect()
    chracter_rect.left = chracter_x_pos
    chracter_rect.top = chracter_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 확인
    if chracter_rect.colliderect(enemy_rect):
        print("충돌했습니다.")
        running = False

    #5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(chracter,(chracter_x_pos,chracter_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
   

    pygame.display.update() #게임화면을 다시 그리기!




#pygame 종료
pygame.quit()