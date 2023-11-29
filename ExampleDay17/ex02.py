import pygame

pygame.init();
screen = pygame.display.set_mode((600,800));
clock = pygame.time.Clock();

character_img = pygame.image.load('8db0ebf7cc80b1420dd141d77adbe420130c3207.png');
character_img = pygame.transform.scale(character_img, (100,100));
# 이미지를 조작하고 화면에서 이미지를 이동하는 걸 보여줌
character = character_img.get_rect();
character.left = 300 - character_img.get_width() // 2;
character.top = 800 - character_img.get_height()

# 이미지 크기 구해오기
# character_size = character.get_rect().size;
# character_width = character_size[0]; # 캐릭터 가로 크기
# character_height = character_size[1]; # 캐릭터 세로 크기

character_x_pos = screen

while True:
    screen.fill((0,0,0));

    event = pygame.event.poll();
    if event.type == pygame.QUIT:
        break;

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            # 방향키 왼쪽으로 이동
            character.left = character.left - 50;
        elif event.key == pygame.K_RIGHT:
            # 방향키 오른쪽으로 이동
            character.left = character.left + 50;
        elif event.key == pygame.K_UP:
            # 방향키 위쪽으로 이동
            character.top = character.top - 50;
        elif event.key == pygame.K_DOWN:
            # 방향키 아래로 이동
            character.top = character.top + 50;

    screen.blit(character_img, character);
    pygame.display.update();
    clock.tick(30);
pygame.quit();