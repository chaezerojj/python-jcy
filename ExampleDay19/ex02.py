'''
엔트리(Entry)
- 텍스트를 입력하거나 보여주고자 할 때 사용하는 컴포넌트
- 주로 한 줄로 구성된 문자열을 처리할 때 사용

텍스트(Text)
- 여러 줄의 문자열을 처리하려면 Text 컴포넌트 사용

리스트박스(ListBox)
- 정해진 순서가 있는 여러개 데이터를 표시하는 컴포넌트

버튼(Button)
- 클릭 시 어떠한 특정 함수를 실행하고자 할 때 사용

tkinter 모듈은 컴포넌트를 배치하는데 사용할 수 있는
pack(), place(), grid() 등의 함수를 제공
'''

from tkinter import *

root = Tk();

listbox = Listbox(root);
label = Label(root, text='제목');
entry = Entry(root)
text = Text(root)
b1 = Button(root, text="생성")
b2 = Button(root, text="수정")
b3 = Button(root, text="삭제")

for i in ["사과", "포도", "바나나", "체리", "귤", "딸기", "오렌지"]:
    listbox.insert(END, i);
listbox.grid(row=0, column=0, columnspan=3, sticky='ew');
label.grid(row=1, column=0);
entry.grid(row=1, column=1, columnspan=2, sticky='ew')
text.grid(row=2, column=0, columnspan=3)
b1.grid(row=3, column=0, sticky='ew'); # -> 버튼 좌우로 확장
b2.grid(row=3, column=1, sticky='ew');
b3.grid(row=3, column=2, sticky='ew')
root.mainloop()
