import pygame
import sys,random,time
from pygame.locals import *
#日常调包
pygame.init()
DISPLAY = pygame.display.set_mode((1024*768))
pygame.display.set_caption('python-snake wants to FUCK the C# ones(remake by bluboy)')
#球球了C#这种东西真不直观我只想玩python哼哼哼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
#python复健练习 用python捋遍思路非常暴力的写出来真的比C#爽多了 而且简洁的过分
ScreenSpeed = pygame.time.Clock()
Font = pygame.font.SysFont("simhei.ttf", 80)
#用的黑体
Black = pygame.Color(0, 0, 0)
White = pygame.Color(255, 255, 255)
Red = pygame.Color(255, 0, 0)
Grey = pygame.Color(150, 150, 150)
#颜色
Snake_Head = [100,100]
Snake_Body = [[80,100],[60,100],[40,100]]
direction = RIGHT

Food_Position = [300,300]
Food_Flag = 1
#这里打算1表示没吃掉 0吃掉了

for event in pygame.event.get():
    if event.type == QUIT:
        # 接收到退出事件后，退出程序
        pygame.quit()
        sys.exit()

    # 判断键盘事件，用 方向键 或 wsad 来表示上下左右
    elif event.type == KEYDOWN:
        if (event.key == K_UP or event.key == K_w) and direction != DOWN:
            direction = UP
        if (event.key == K_DOWN or event.key == K_s) and direction != UP:
            direction = DOWN
        if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
            direction = LEFT
        if (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
            direction = RIGHT

# 根据键盘的输入，改变蛇的头部，进行转弯操作
if direction == LEFT:
    Snake_Head[0] -= 20
if direction == RIGHT:
    Snake_Head[0] += 20
if direction == UP:
    Snake_Head[1] -= 20
if direction == DOWN:
    Snake_Head[1] += 20

# 将蛇的头部当前的位置加入到蛇身的列表中
Snake_Body.insert(0, list(Snake_Head))
 
if Snake_Head[0]==Food_Position[0] and Snake_Head[1]==Food_Position[1]:
    Food_Flag = 0
else:
    Snake_Body.pop()

if Food_Flag == 0:
    # 随机生成x, y
    x = random.randrange(1,32)
    y = random.randrange(1,24)
    Food_Position = [int(x*20),int(y*20)]
    Food_Flag = 1

def drawSnake(Snake_Body):
    for i in Snake_Body:
        pygame.draw.rect(Display, White, Rect(i[0], i[1], 20, 20))

 def drawFood(Food_Position):
    pygame.draw.rect(Display Red, Rect(Food_Position[0], Food_Position[1], 20, 20))

def drawScore(score):
    # 设置分数的显示颜色
    score_Surf = Font.render('%s' %(score), True, GREY)
    # 设置分数的位置
    score_Rect = score_Surf.get_rect()
    score_Rect.midtop = (320, 240)
    # 绑定以上设置到句柄
    DISPLAY.blit(score_Surf, score_Rect)

DISPLAY.fill(BLACK)# 画出贪吃蛇
drawSnake(Snake_Body)
# 画出食物的位置
drawFood(Food_Position)
# 打印出玩家的分数
drawScore(len(Snake_Body) - 3)
# 刷新Pygame的显示层，贪吃蛇与食物的每一次移动，都会进行刷新显示层的操作来显示。
pygame.display.flip()
# 控制游戏速度
FPSCLOCK.tick(7)

# 游戏结束并退出
def GameOver():
    # 设置GameOver的显示颜色
    GameOver_Surf = Font.render('Game Over!', True, GREY)
    # 设置GameOver的位置
    GameOver_Rect = GameOver_Surf.get_rect()
    GameOver_Rect.midtop = (320, 10)
    # 绑定以上设置到句柄
    DISPLAY.blit(GameOver_Surf, GameOver_Rect)

    pygame.display.flip()
    # 等待3秒
    time.sleep(3)
    # 退出游戏
    pygame.quit()
    # 退出程序
    sys.exit()

'''游戏结束的判断'''
# 贪吃蛇触碰到边界
if snake_Head[0]<0 or snake_Head[0]>620:
    GameOver()
if snake_Head[1]<0 or snake_Head[1]>460:
    GameOver()
# 贪吃蛇触碰到自己
for i in snake_Body[1:]:
    if snake_Head[0]==i[0] and snake_Head[1]==i[1]:
        GameOver()
