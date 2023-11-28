'''
다음 TV 클래스가 있다.
TV 클래스를 상속받은 ColorTV 클래스를 작성하세요

출력결과)
64인치
Blue
'''

class TV:
    size = 0;
    def __init__(self, size):
        self.size = size;

    def getSize(self):
        print("{}인치".format(self.size))

class ColorTv(TV):
    def __init__(self, size, color):
        super().__init__(size);
        self.color = color;

    def info(self):
        print(self.color)

colortv = ColorTv(64, "Blue")
colortv.getSize()
colortv.info()