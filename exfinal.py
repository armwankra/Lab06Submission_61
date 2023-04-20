import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')     
FONT = pg.font.Font(None, 32)

firstname = FONT.render('Firstname', True, (0,0,0))
firstnameRect = firstname.get_rect() # text size
firstnameRect.center = (100,60)

lastname = FONT.render('Lastname', True, (0,0,0))
lastnameRect = lastname.get_rect() # text size
lastnameRect.center = (100,160)

age = FONT.render('Age', True, (0,0,0))
ageRect = age.get_rect() # text size
ageRect.center = (70,260)

submit = FONT.render('Submit', True, (0,0,0))
submitRect = submit.get_rect() # text size
submitRect.center = (150,385)

firstname = FONT.render('Firstname', True, (0,0,0))
firstnameRect = firstname.get_rect() # text size
firstnameRect.center = (100,60)

# __________________

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


class InputAgeBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def checkNum(self):
        if not self.text.isnumeric():
            self.text = "Error"
        return self.text

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


input_boxFirst = InputBox(100, 100, 140, 32) # สร้าง InputBox1
input_boxLast = InputBox(100, 200, 140, 32) # สร้าง InputBox2
input_boxAge = InputAgeBox(100, 300, 140, 32) # สร้าง InputBox2
input_boxes = [input_boxFirst, input_boxLast,input_boxAge] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย


class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,r=0,g=0,b=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.R = r
        self.G = g
        self.B = b

    def draw(self,screen):
        pg.draw.rect(screen,(self.R,self.G,self.B),(self.x,self.y,self.w,self.h))

class Button(Rectangle):

    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mousePosX ,mousePosY = pg.mouse.get_pos()
        if mousePosX >= self.x and mousePosX <= self.x + self.w and mousePosY >= self.y and mousePosY <= self.y+self.h:
            return True
        else:
            return False
        pass
    def isClick(self):
        if pg.mouse.get_pressed()[0]:
            return True
        else:
            return False
btn = Button(100,360,100,50)
check = 0
while(1):
    screen.fill((255, 255, 255))
    screen.blit(firstname, firstnameRect)
    screen.blit(lastname, lastnameRect)
    screen.blit(age, ageRect)
    

    
    if check == 1:
        ans = FONT.render("Hello " +str(input_boxFirst.text)+" "+str(input_boxLast.text)+" !",True,(0,0,0))
        ansRect = ans.get_rect()
        ansRect.center = (550,150)
        screen.blit(ans, ansRect)

        ansAge = FONT.render("Your are " +input_boxAge.checkNum()+" year old",True,(0,0,0))
        ansAgeRect = ansAge.get_rect()
        ansAgeRect.center = (550,200)
        screen.blit(ansAge, ansAgeRect)

    if btn.isMouseOn():
        if btn.isClick():
            btn.R = 94
            btn.G = 0
            btn.B = 255
            check = 1
        else:
            btn.R = 160
            btn.G = 160
            btn.B = 160
    else:
        btn.R = 255
        btn.G = 0
        btn.B = 0

    btn.draw(screen)

    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    screen.blit(submit,submitRect)
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()

    
    pg.time.delay(1)
    pg.display.update()