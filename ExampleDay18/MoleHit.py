import time
import pygame
import sys
import random

# 초기화
pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height));
# 창 이름 설정
pygame.display.set_caption("두더지 잡기 게임");
background = (255,255,255);
# 두더지 이미지 로드
mole_img = pygame.image.load("do.jpg")
mole_img = pygame.transform.scale(mole_img, (100,100));

score = 0;
font = pygame.font.Font(None, 36)
mole_rect = mole_img.get_rect();
mole_rect.center = (width // 2, height // 2);

clock = pygame.time.Clock();
start_time = pygame.time.get_ticks();
game_time = 60000; # 1분(밀리초 단위)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();

        # 마우스 클릭 이벤트
        # 만약 마우스가 클릭되었다.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mole_rect.collidepoint(event.pos):
                score = score + 1;
                mole_rect.x = random.randint(0, width - mole_rect.width);
                mole_rect.y = random.randint(0, height - mole_rect.height);

    screen.fill(background);
    screen.blit(mole_img, mole_rect);

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, (0,0,0));
    screen.blit(score_text, (10,10));
    current_time = pygame.time.get_ticks()
    sec = current_time / 1000.0;
    int_sec = int(sec);
    time_text = font.render(f"Time: {int_sec}", True, (0,0,0))
    screen.blit(time_text, (screen.get_width() - time_text.get_width(), 0));
    if current_time - start_time >= game_time:
        pygame.quit();
        sys.exit();
    # 화면 업데이트
    pygame.display.flip()
    # 초당 프레임 수 설정
    clock.tick(20);