import random
class Rectangle:
    def __init__(self,size,x1,y1):
        self.size =size
        self.x1 = x1
        self.y1 = y1
        self.x2 = x1+size
        self.y2 = y1+size
class Background:
    def __init__(self,size):
        self.size = size
        sizerec = random.randint(20,self.size-20)  #ขนาดสี่เหลี่ยม 
        xrec = random.randint(0,self.size-sizerec) #ตำแหน่งสี่เหลี่ยมแกน x
        yrec = random.randint(0,self.size-sizerec) #ตำแหน่งสี่เหลี่ยมแกน y
        self.rec = Rectangle(sizerec,xrec,yrec)
    def checkPoint(self):
        x,y = [int(a) for a in input("ทายตำแหน่ง x และ y :").split(" ")]
        print("พิกัดสี่เหลี่ยม X : [%d,%d] Y : [%d,%d]" %(self.rec.x1,self.rec.x2,self.rec.y1,self.rec.y2))
        if self.rec.x1 <= x <= self.rec.x2 and self.rec.y1 <= y <= self.rec.y2:  ##เช็คจุด
            print("ยินดีด้วย คุณคุณทายจุดถูก")
        else:
            print("เสียใจด้วย คุณคุณทายจุดผิด")

    def checkArea(self):
        guessarea = int(input("ทายขนาดของสี่เหลี่ยม :"))
        arearec = self.rec.size**2
        if guessarea == arearec :        ##เช็คขนาด
            print("ยินดีด้วย คุณคุณทายพื้นที่ถูก")
        else:
            print("เสียใจด้วย คุณคุณทายพื้นที่ผิด พื้นที่ขนาด %d"%arearec)

start = Background(random.randint(50,100))
print("ยินดีต้อนรับสู่เกมทายจุด")
print("้เกมขนาด %d * %d"%(start.size,start.size))
start.checkPoint()
start.checkArea()