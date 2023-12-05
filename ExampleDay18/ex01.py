# # pip install PyQt5
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# class App(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI();
#
#     def initUI(self):
#         # 창의 제목을 설정
#         self.setWindowTitle("My App");
#         # 너비와 높이 조정
#         self.resize(600, 800);
#         # 화면에 요소가 보여짐
#         self.show();
#
# if __name__ == '__main__':
#     # QApplication 클래스는 GUI 응용프로그램의 제어흐름과 기본 설정 관리
#     app = QApplication(sys.argv)
#     ex = App();
#     sys.exit(app.exec_());


from tkinter import *

def onClick():
    btn1.config(text="One")
def onClick2():
    btn2.config(text="Two")

root = Tk();
root.title("제목지정");
root.geometry("600x800") # 창의 너비, 창의 높이
# 최대 가능범위를 둘다 False로 두면 작동 불가
root.resizable(width=False, height=False)

btn1 = Button(root, text="첫번째", width=25, height=5, command=onClick)
btn2 = Button(root, text="두번째", width=25, height=5, command=onClick2)
btn1.pack(side=LEFT, padx=10);
btn2.pack(side=LEFT, padx=10);

root.mainloop()
