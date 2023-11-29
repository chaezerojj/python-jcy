# terminal >> pip install pygame
'''
게임창 띄우기
'''
import pygame # 파이게임 모듈 임포트

pygame.init(); # 파이게임 초기화
screen = pygame.display.set_mode((600,800)) # 가로 600 세로 800 지정
'''
게임 fps 설정
- 초당 프레임을 의미
* 프레임에 따라서 게임에서 캐릭터가 움직이는 속도가 다름
'''
clock = pygame.time.Clock();

while True:
    '''
    루프 내에서 게임 이벤트 설정, 화면 설정, 사용자 행위 등을 정의 하면 됨.
    '''
    screen.fill((0,0,0));
    event = pygame.event.poll(); # 이벤트 처리
    if event.type == pygame.QUIT:
        break;

    # 화면 그리기
    pygame.display.update(); # 모든 화면 그리기 업데이트
    clock.tick(30); # 30 fps
    '''
    30 FPS(초당 프레임 수)를 위한 딜레이 추가
    딜레이 시간이 아닌 목표로 하는 FPS 값
    '''
pygame.quit();