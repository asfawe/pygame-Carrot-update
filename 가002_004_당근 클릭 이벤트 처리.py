import pygame as pg
import random

def 당근초기화():
    global 랜덤당근, 랜덤당근좌표
    랜덤당근 = [당근] * 4 + [상한당근] * 5 # 랜덤당근은 4개의 당근 5개의 상한당근이 있는 리스트입니다.
    랜덤당근좌표 = [(170 + x * 260, 190 + y * 220)for x in range(3) for y in range(3)] # 리스트 컴프리헨션을 이용하여 x,y위치값들이 있는 당근좌표의 리스트를 만듭니다.
    random.shuffle(랜덤당근) # 랜덤 라이브러리의 shuffle함수를 이용해 랜덤당근 내 요소드을 섞어줍니다.

pg.init()

화면가로길이, 화면세로길이 = (980, 940)
화면 = pg.display.set_mode([화면가로길이, 화면세로길이])
pg.display.set_caption('상한 당근을 싱싱한 당근으로! By 인피니티 스톤')

#글꼴설정
글꼴 = pg.font.SysFont('malgungothic', 35)


#이미지 초기화
배경이미지 = pg.image.load('img/당근_배경.png')
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))
화면.blit(배경이미지, (0, 0))

#시간바
시간바 = pg.image.load('img/시간바.png')
시간바 = pg.transform.scale(시간바, (400, 100))
화면.blit(시간바, (520, 20))

#당근
당근 = pg.image.load('img/당근.png')
당근 = pg.transform.scale(당근, (130, 220))
# 화면.blit(당근, (200, 200))

#상한당근
상한당근 = pg.image.load('img/상한당근.png')
상한당근 = pg.transform.scale(상한당근, (130, 220))
# 화면.blit(상한당근, (300, 300))

pg.display.update()

당근초기화()

경과시간 = 0
당근생성시간 = 0
당근인덱스 = 0

시계 = pg.time.Clock()
현재챕터 = 1
최종챕터 = 10

while True:
    화면.blit(배경이미지, (0, 0))
    화면.blit(시간바, (520, 20))

    흐른시간 = 시계.tick(60) / 1000
    경과시간 += 흐른시간

    if 경과시간 <= 60:
        시간문자열 = f'{round(경과시간, 1)} 초'
    else:
        시간문자열 = f'{int(경과시간 // 60)}분 {int(경과시간 % 60)}초'

    시간 = 글꼴.render(시간문자열, True, (0, 0, 0))
    화면.blit(시간, (700, 50))

    챕터글자 = 글꼴.render(f'챕터 : {현재챕터} / {최종챕터}', True, (255, 255, 255))
    화면.blit(챕터글자, (80, 20))

    당근글자 = 글꼴.render(f'남은 상한당근 갯수 : {len(랜덤당근) - 랜덤당근.count(당근)}개', True, (255, 255, 255))
    화면.blit(당근글자, (80, 90))

    당근생성시간 += 흐른시간
    if 당근생성시간 >= 1: # 흐른시간을 당근생성시간에 추가해 만약 생성시간이 1초가 지났으면 
        당근생성시간 = 0 # 생성시간을 0으로 초기화하고
        당근인덱스 = random.randrange(len(랜덤당근)) # random.randrange(len(랜덤당근)) 를 이용해 랜덤당근의 인덱스를 랜덤으로 정합니다.

    현재당근 = 화면.blit(랜덤당근[당근인덱스], 랜덤당근좌표[당근인덱스])

    pg.display.update()

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            pg.display.quit()

        elif 이벤트.type == pg.MOUSEBUTTONDOWN:
            클릭_위치 = pg.mouse.get_pos()
            if 당근인덱스 != -1 and 현재당근.collidepoint(클릭_위치): # 현재당근.collidepoint(클릭_위치) = 현재 당근을 내가 클릭했다.
                if 랜덤당근[당근인덱스] == 상한당근:
                    랜덤당근[당근인덱스] = 당근

                    if len(랜덤당근) - 랜덤당근.count(당근) == 0: # 상한당근에 갯수가 0 이라면
                        현재챕터 += 1
                        당근초기화()
