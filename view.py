from tkinter import *
from venda import Tela_venda
from venda2 import Tela_venda2
from venda3 import Tela_venda3
from venda4 import Tela_venda4

class Patio(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)

        self["bg"] = "IndianRed3"
        self.geometry("560x440+100+100")
        self.title("Concessionaria BIBIS ")



        self.bt = Button(self, width=40, height=5, text="UP TSI\n 2017/2018", command=self.btn_venda, bg='aquamarine2')
        self.bt2 = Button(self, width=40, height=5, text="Civic\n 2018/2019", command=self.btn_venda2, bg='aquamarine2')
        self.bt3 = Button(self, width=40, height=5, text="New Beetle\n 2010/2011",command=self.btn_venda3, bg='aquamarine2')
        self.bt4 = Button(self, width=40, height=5, text="Hb20\n 2016/2017",command=self.btn_venda4, bg='aquamarine2')


        self.bt.place(x=125, y=20)
        self.bt2.place(x=125, y=110)
        self.bt3.place(x=125, y=200)
        self.bt4.place(x=125, y=290)


    def btn_venda(self):
        Tela_venda(self)
    def btn_venda2(self):
        Tela_venda2(self)
    def btn_venda3(self):
        Tela_venda3(self)
    def btn_venda4(self):
        Tela_venda4(self)