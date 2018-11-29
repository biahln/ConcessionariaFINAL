from tkinter import *
from view import Patio

class Login(Tk):
    def __init__(self):
        super().__init__()


        self["bg"] = "IndianRed3"
        self.geometry("560x440+100+100")
        self.title("Concessionaria BIBIS ")


        self.bt = Button(self, width=40, height=5, text="ENTRAR", command=self.btn_view, bg='aquamarine2')
        self.vendedor=Entry(bg='IndianRed3')
        self.lb=Label(self,text="vendedor: ",bg='IndianRed3')




        self.bt.place(x=125, y=280)
        self.vendedor.place(x=210, y=100)
        self.lb.place(x=130, y=100)






    def btn_view(self):
        if self.vendedor.get()=="bia1234":
            Patio(self)
        else:
            self.aviso = Label(self, text='Digite o código do vendedor para prosseguir a compra',bg='IndianRed3',font=('Arial','10','bold'))
            self.aviso.place(x=115, y=170)