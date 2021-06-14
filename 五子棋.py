import pygame,sys#导入模块
pygame.init()#游戏初始化
pygame.mixer.init()
pygame.font.init()#汉字初始化
screen = pygame.display.set_mode((650,450))#创建游戏窗口
pygame.display.set_caption("五子棋")#设置游戏窗口的标题
pos=[]#记录棋盘上每一个点的坐标
x=10#记录点的x坐标
y=10#记录点的y坐标
p=[]#记录点的地图位置
n=0#判断棋子的颜色
color=[]#记录棋子的颜色
map1=[]#判断哪些项有点
i=0#判断胜负查看每一个点的循环变量
for a in range(16):#表示棋盘的行的点
    for a in range(16):#表示棋盘列的点
        pos.append((x,y))#将点的位置用元祖的方式记录到列表
        map1.append(0)#添加元素0代表点，1代表白棋，2代表黑棋
        x+=30#记录下一个点
    x=10#记录下一行的第一个
    y+=30#记录下一行
pygame.mixer.music.load("5a41_37f5_ac53_b2f6f7c0ea87d23a393503caa67a2c5f.mp3")
while True:#游戏循环
    if pygame.mixer.music.get_busy()==False:
        pygame.mixer.music.play()
    x=10#重设x坐标
    y=10#重设y坐标
    screen.fill((139,69,19))#设置为棋盘的颜色
    for event in pygame.event.get():#遍历所有按键
        if event.type == pygame.QUIT:#如果按下关闭键
            pygame.quit()#关闭窗口
            sys.exit()#关闭程序
        if event.type==pygame.MOUSEBUTTONDOWN:#判断是否点击鼠标
            for b in range(len(pos)):#遍历所有的点的位置
                #设置一个虚拟的圆，判断是否鼠标点击每个圆中
                if pos[b][0]-15<pygame.mouse.get_pos()[0] and pos[b][0]+15>pygame.mouse.get_pos()[0]:
                    if pos[b][1]-15<pygame.mouse.get_pos()[1] and pos[b][1]+15>pygame.mouse.get_pos()[1]:
                        if n==0:
                            n+=1
                            p.append(b)#添加点的项
                        if b!=p[-1]:
                            n+=1
                            p.append(b)#添加点的项
                        if n%2==0:#判断奇偶数
                            color.append((255,255,255))#将棋子颜色添加到列表
                            map1[b]=1
                        else:
                            color.append((0,0,0))
                            map1[b]=2
                        break
    for a in range(14):#表示棋盘行的点
        for a in range(15):#表示棋盘列的点
            pygame.draw.rect(screen,(0,0,0),(x,y,30,30),1)#绘制矩形
            x+=30#绘制下一个圆
        x=10#绘制下一行的第一个的圆
        y+=30#绘制下一行的圆
    pygame.draw.circle(screen,(255,0,0),(pygame.mouse.get_pos()[0]+5,pygame.mouse.get_pos()[1]+5),15,1)
    i+=1
    #绘制一个跟随鼠标的圆
    for c in range(len(p)):#判断有多少个点，将这些点都绘制出来
        pygame.draw.circle(screen,color[c],pos[p[c]],15,0)#绘制圆形
    screen.blit(pygame.font.SysFont("simhei",25).render("棋子数量：   "+str(n),0,(255,255,0)),(466,10))
    if i==250:#看循环是否结束
        i=0#重新检测
    #判断横
    if map1[i]==1 and map1[i+1]==1 and map1[i+2]==1 and map1[i+3]==1 and map1[i+4]==1:
        print("白棋赢")
        break
    if map1[i]==2 and map1[i+1]==2 and map1[i+2]==2 and map1[i+3]==2 and map1[i+4]==2:
        print("黑棋赢")
        break
    #判断竖
    if map1[i]==1 and map1[i+16]==1 and map1[i+32]==1 and map1[i+48]==1 and map1[i+64]==1:
        print("白棋赢")
        break
    if map1[i]==2 and map1[i+16]==2 and map1[i+32]==2 and map1[i+48]==2 and map1[i+64]==2:
        print("黑棋赢")
        break
    #判断反斜
    if map1[i]==1 and map1[i+16+1]==1 and map1[i+32+2]==1 and map1[i+48+3]==1 and map1[i+64+4]==1:
        print("白棋赢")
        break
    if map1[i]==2 and map1[i+16+1]==2 and map1[i+32+2]==2 and map1[i+48+3]==2 and map1[i+64+4]==2:
        print("黑棋赢")
        break
    #判断斜
    if map1[i]==1 and map1[i+16-1]==1 and map1[i+32-2]==1 and map1[i+48-3]==1 and map1[i+64-4]==1:
        print("白棋赢")
        break
    if map1[i]==2 and map1[i+16-1]==2 and map1[i+32-2]==2 and map1[i+48-3]==2 and map1[i+64-4]==2:
        print("黑棋赢")
        break
    #显示棋子数量，因为一共256个交叉点，所以空三格
    pygame.display.flip()#刷新游戏
 
