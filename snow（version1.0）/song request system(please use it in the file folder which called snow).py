import pygame as pg #pygame=python+game import导入

import random

from pygame.locals import * #导入常量

pg.init()#初始化

#设定雪花坐标列表

x=[]

y=[]

a=[]

b=[]

x1=[]

y1=[]

a1=[]

b1=[]

print ("1.只因你太美")

print ("2.雨花石")

print ("3.百战成诗")

print ("4.何以歌")

print ("5.赛马")

print ("6.我和我的祖国")

print ("7.Banana Banana")

print ("8.The Time of Our Life")

print ("9.UN' ESTATE ITALIANA")

print ("10.奥利给")

song=input("请输入歌名")

name=input("请输入弹幕内容")

if(song=="百战成诗"):

     timg = pg.image.load("BZCS.png")#加载背景

     h=timg.get_height()

     w=timg.get_width()

     pg.mixer.music.load("BZCS.mp3")#设定音乐

     pg.mixer.music.play(-1,0.0)

if(song=="只因你太美"):

     timg = pg.image.load("timg.jpg")#加载背景

     h=timg.get_height()

     w=timg.get_width()

     pg.mixer.music.load("SWIN.mp3")#设定音乐

     pg.mixer.music.play(-1,0.0)

if(song=="何以歌"):

     timg = pg.image.load("hyg.jpg")#加载背景

     h=timg.get_height()

     w=timg.get_width()

     pg.mixer.music.load("hyg.mp3")#设定音乐

     pg.mixer.music.play(-1,0.0)

elif(song=="雨花石"):

     timg = pg.image.load("YHT.jpg")#加载背景

     h=timg.get_height()

     w=timg.get_width()
     
     pg.mixer.music.load("YHS.mp3")#设定音乐

     pg.mixer.music.play(-1,0.0)

elif(song=="奥利给"):

     timg = pg.image.load("ALG.jpg")#加载背景

     h=timg.get_height()

     w=timg.get_width()

     pg.mixer.music.load("ALG.mp3")#设定音乐

     pg.mixer.music.play(-1,0.0)

elif(song=="赛马"):

     timg = pg.image.load("SM.jpg")#加载背景

     h=timg.get_height()

     w=timg.get_width()

     pg.mixer.music.load("SM.mp3")#设定音乐

     pg.mixer.music.play(-1,0.0)

elif(song=="我和我的祖国"):

     timg = pg.image.load("WHWDZG.jpeg")#加载背景

     h=timg.get_height()

     w=timg.get_width()
     
     pg.mixer.music.load("WHWDZG.mp3")#设定音乐

     pg.mixer.music.play(-1,0.0)

elif(song=="Banana"):

     timg = pg.image.load("Banana.jpg")#加载背景

     h=timg.get_height()

     w=timg.get_width()
     
     pg.mixer.music.load("Banana.mp3")#设定音乐

     pg.mixer.music.play(-1,0.0)

elif(song=="The Time of Our Life"):

     timg = pg.image.load("The Time of Our Life.jpg")#加载背景

     h=timg.get_height()

     w=timg.get_width()
     
     pg.mixer.music.load("The Time of Our Life.mp3")#设定音乐

     pg.mixer.music.play(-1,0.0)

elif(song=="UN' ESTATE ITALIANA"):

     timg = pg.image.load("UN' ESTATE ITALIANA.jpg")#加载背景

     h=timg.get_height()

     w=timg.get_width()
     
     pg.mixer.music.load("UN' ESTATE ITALIANA.mp3")#设定音乐

     pg.mixer.music.play(-1,0.0)

print ("请点击窗口")

screen = pg.display.set_mode((w,h))#设置窗口

pg.display.set_caption(song)#设置标题
     
r=[]

g=[]

bl=[]

for i in range(50):

     r.append(random.randint(0,255))

     g.append(random.randint(0,255))

     bl.append(random.randint(0,255))

while True:

     screen.blit(timg,(0,0))#贴背景

     font = pg.font.Font("simsun.ttc",30)#加载字体

     if(song!="YHS" and song!="SM"):
          
          for i in range(50):
               
               jntm = font.render(name,True,(r[i],g[i],bl[i]))#制作雪花

               #添加雪花的坐标

               x.append(random.randint(0,w))

               y.append(random.randint(0,h))
          
               screen.blit(jntm,(x[i],y[i]))#贴雪花

               x[i] = x[i]+1#让x坐标增加

               y[i] = y[i]+1#让y坐标增加

               if(y[i]>h):#如果雪花y坐标超过底边

                    y[i]=-50#让雪花回到顶部

               if(x[i]>w):#如果雪花x坐标超过底边

                    x[i]=-50#让雪花回到顶部
                    
          for i in range(50):
          
               jntm1 = font.render(name,True,(r[i],g[i],bl[i]))#制作雪花
          
               #添加雪花的坐标

               a.append(random.randint(0,w))

               b.append(random.randint(0,h))
          
               screen.blit(jntm1,(a[i],b[i]))#贴雪花

               a[i] = a[i]-1#让x坐标增加

               b[i] = b[i]+1#让y坐标增加

               if(b[i]>h):#如果雪花y坐标超过底边

                    b[i]=-50#让雪花回到顶部

               if(a[i]<-100):#如果雪花x坐标超过底边

                    a[i]=675#让雪花回到顶部

          for i in range(50):
          
               jntm3 = font.render(name,True,(r[i],g[i],bl[i]))#制作雪花   

               #添加雪花的坐标

               a1.append(random.randint(-2000,-50))
          
               b1.append(random.randint(0,h))
          
               screen.blit(jntm3,(a1[i],b1[i]))#贴雪花

               a1[i] = a1[i]+1#让x坐标增加

               if(a1[i]>w):#如果雪花x坐标超过底边

                    a1[i]=-50#让雪花回到顶部

          for i in range(50):
          
               jntm2 = font.render(name,True,(r[i],g[i],bl[i]))#制作雪花   

               #添加雪花的坐标

               x1.append(random.randint(0,w))
          
               y1.append(random.randint(-200,-50))
          
               screen.blit(jntm2,(x1[i],y1[i]))#贴雪花

               y1[i] = y1[i]+1#让x坐标增加

               if(y1[i]>h):#如果雪花x坐标超过底边

                    y1[i]=-50#让雪花回到顶部

     if(song=="YHS"):
          
          for i in range(50):
               
               jntm2 = font.render(name,True,(r[i],g[i],bl[i]))#制作雪花   

               #添加雪花的坐标

               x1.append(random.randint(0,w))
          
               y1.append(random.randint(-200,-50))
          
               screen.blit(jntm2,(x1[i],y1[i]))#贴雪花

               y1[i] = y1[i]+1#让x坐标增加

               if(y1[i]>h):#如果雪花x坐标超过底边

                    y1[i]=-50#让雪花回到顶部

     if(song=="SM"):

          for i in range(50):
          
               jntm3 = font.render(name,True,(r[i],g[i],bl[i]))#制作雪花   

               #添加雪花的坐标

               a1.append(random.randint(-2000,-50))
          
               b1.append(random.randint(0,h))
          
               screen.blit(jntm3,(a1[i],b1[i]))#贴雪花

               a1[i] = a1[i]+1#让x坐标增加

               if(a1[i]>w):#如果雪花x坐标超过底边

                    a1[i]=-50#让雪花回到顶部

     for event in pg.event.get():#获取pg中的事件列表
          
          if(event.type == QUIT):
               
               pg.display.quit()#窗口退出
               
               exit()#程序退出
               
          if event.type==KEYDOWN:
               
               if event.key==K_SPACE:

                    x=[]

                    y=[]

                    a=[]

                    b=[]

                    x1=[]

                    y1=[]

                    a1=[]

                    b1=[]

                    print ("1.只因你太美")

                    print ("2.雨花石")

                    print ("3.百战成诗")

                    print ("4.何以歌")

                    print ("5.赛马")

                    print ("6.我和我的祖国")

                    print ("7.Banana Banana")

                    print ("8.The Time of Our Life")

                    print ("9.UN' ESTATE ITALIANA")

                    print ("10.奥利给")

                    song=input("请输入歌名")

                    name=input("请输入弹幕内容")

                    print ("请点击窗口")
                    
                    if(song=="只因你太美"):

                         timg = pg.image.load("timg.jpg")#加载背景

                         h=timg.get_height()

                         w=timg.get_width()

                         pg.mixer.music.load("SWIN.mp3")#设定音乐

                         pg.mixer.music.play(-1,0.0)

                    elif(song=="雨花石"):

                         timg = pg.image.load("YHT.jpg")#加载背景

                         h=timg.get_height()

                         w=timg.get_width()
                         
                         pg.mixer.music.load("YHS.mp3")#设定音乐

                         pg.mixer.music.play(-1,0.0)

                    elif(song=="奥利给"):

                         timg = pg.image.load("ALG.jpg")#加载背景

                         h=timg.get_height()

                         w=timg.get_width()

                         pg.mixer.music.load("ALG.mp3")#设定音乐

                         pg.mixer.music.play(-1,0.0)

                    elif(song=="赛马"):

                         timg = pg.image.load("SM.jpg")#加载背景

                         h=timg.get_height()

                         w=timg.get_width()
                         
                         pg.mixer.music.load("SM.mp3")#设定音乐

                         pg.mixer.music.play(-1,0.0)

                    elif(song=="我和我的祖国"):

                         timg = pg.image.load("WHWDZG.jpeg")#加载背景

                         h=timg.get_height()

                         w=timg.get_width()
     
                         pg.mixer.music.load("WHWDZG.mp3")#设定音乐

                         pg.mixer.music.play(-1,0.0)

                    elif(song=="Banana"):

                         timg = pg.image.load("Banana.jpg")#加载背景

                         h=timg.get_height()

                         w=timg.get_width()
     
                         pg.mixer.music.load("Banana.mp3")#设定音乐

                         pg.mixer.music.play(-1,0.0)

                    elif(song=="The Time of Our Life"):

                         timg = pg.image.load("The Time of Our Life.jpg")#加载背景

                         h=timg.get_height()

                         w=timg.get_width()
     
                         pg.mixer.music.load("The Time of Our Life.mp3")#设定音乐
               
                         pg.mixer.music.play(-1,0.0)

                    elif(song=="UN' ESTATE ITALIANA"):

                         timg = pg.image.load("UN' ESTATE ITALIANA.jpg")#加载背景

                         h=timg.get_height()

                         w=timg.get_width()
     
                         pg.mixer.music.load("UN' ESTATE ITALIANA.mp3")#设定音乐

                         pg.mixer.music.play(-1,0.0)

                    if(song=="百战成诗"):

                         timg = pg.image.load("BZCS.png")#加载背景

                         h=timg.get_height()

                         w=timg.get_width()

                         pg.mixer.music.load("BZCS.mp3")#设定音乐

                         pg.mixer.music.play(-1,0.0)

                    screen = pg.display.set_mode((w,h))#设置窗口

                    pg.display.set_caption(song)#设置标题
                         
                    r=[]

                    g=[]

                    bl=[]
                    
                    for i in range(50):

                         r.append(random.randint(0,255))

                         g.append(random.randint(0,255))

                         bl.append(random.randint(0,255))
   
     pg.display.update()#刷新窗口
     
