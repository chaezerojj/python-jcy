import pygame
import sys
import random

pygame.init();
SCREEN_WIDTH = 750;
SCREEN_HEIGHT = 750;
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT));
clock = pygame.time.Clock();
background_image = pygame.image.load('BG.png');

character_image = pygame.image.load('8db0ebf7cc80b1420dd141d77adbe420130c3207.png')
character_image = pygame.transform.scale(character_image, (60,60));
character = character_image.get_rect(centerx=SCREEN_WIDTH // 2, bottom=SCREEN_HEIGHT);
running = True;
rock_image = pygame.image.load('rock.png');
rock_image = pygame.transform.scale(rock_image, (40,40));
rocks = [];
for i in range(10):
    rock = rock_image.get_rect(left=random.uniform(10, SCREEN_WIDTH - rock_image.get_width()), top=-20);
    dy = random.uniform(200,500);
    rocks.append((rock, dy));

while True:
    screen.blit(background_image, (0,0));

    event = pygame.event.poll();
    if event.type == pygame.QUIT:
        running = False;
    pressed = pygame.key.get_pressed();
    if pressed[pygame.K_LEFT]:
        character.left -= 15;
    elif pressed[pygame.K_RIGHT]:
        character.left += 15;

    # 캐릭터가 화면 왼쪽으로 벗어나는 것을 방지
    if character.left < 0:
        character.left = 0;
    # 캐릭터가 화면 오른쪽으로 벗어나는 것을 방지
    if character.right > SCREEN_WIDTH:
        character.right = SCREEN_WIDTH;

    for rock, dy in rocks:
        rock.top += 20;
        if rock.top > SCREEN_HEIGHT:
            rocks.remove((rock, dy));
            rock = rock_image.get_rect(left=random.uniform(10, SCREEN_WIDTH - rock_image.get_width()), top=20)
            dy = random.uniform(200, 500);
            rocks.append((rock, dy))
        if character.colliderect(rock):
            print("충돌!");
            running = False;
            pygame.quit();

    for rock, dy in rocks:
        screen.blit(rock_image, rock);

    # 화면에 캐릭터 그림
    screen.blit(character_image, character)
    pygame.display.update();
    clock.tick(30);
pygame.quit();
