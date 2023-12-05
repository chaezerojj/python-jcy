from tkinter import *

class Login(object):
    def register(self):
        pass;

    def __init__(self, root):
        self.frLogin = Frame(root, padx=20, pady=20);
        self.frLogin.grid(row=0, column=0);

        Label(self.frLogin, text='UserName').grid(row=0, column=0)
        self.usEntry = Entry(self.frLogin);
        self.usEntry.grid(row=0, column=1)

        Label(self.frLogin, text='Password').grid(row=1, column=0)
        self.pwEntry = Entry(self.frLogin, show="*");
        self.pwEntry.grid(row=1, column=1, padx=20, pady=20)

        Label(self.frLogin, text="Password check").grid(row=2, column=0)
        self.pwEntry_reg = Entry(self.frLogin, show="*")
        self.pwEntry_reg.grid(row=2, column=1, padx=20, pady=20)

        Button(self.frLogin, borderwidth=10, text="회원가입", width=10, pady=4).grid(row=3, column=1, padx=10, pady=19)

        self.frReg = Frame(root, padx=20, pady=20)
        self.frReg.grid(row=0, column=0, padx=20, pady=20)

def main():
    root = Tk();
    demo = Login(root);
    root.geometry('300x350');
    root.title('Join Form')
    root.mainloop()

if __name__ == '__main__':
    main();