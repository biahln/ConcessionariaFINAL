from tkinter import *
from nota import Nota1

class Tela_venda4(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("560x440+700+100")
        self.title("Hb20")
        self["bg"]= "IndianRed3"
        self.font = ('14')

        self.lb = Label(self, text='Marca: Hyundai\nValor: 50.000\nContém:\n-Ar Condicionado\n-Vidro Elétrico\n',
                        font=self.font, bg='IndianRed3', fg='black')
        self.titulo = Label(self, text='INFORMAÇÕES', font=('Arial', '20', 'bold'), bg='IndianRed3')
        self.titulo.pack(pady=10)
        self.lb.pack()
        self.bt = Button(self, text='Comprar', width=40, height=5, bg='IndianRed3',command=self.bt_venda)

        self.bt.pack(side=BOTTOM, pady=10)

    def bt_venda(self):
        Nota1(self)