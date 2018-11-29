from tkinter import *

class Nota1(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)



        self.geometry("560x440+700+100")
        self.title('Cadastro')
        self["bg"]= "IndianRed3"
        self.font= ('14')

        self.lb=Label(self,text='Vendedor',bg='IndianRed3')
        self.lb2=Label(self,text='Cliente',bg='IndianRed3')
        self.lb3=Label(self,text='CPF cliente',bg='IndianRed3')
        self.lb4=Label(self,text='Valor do carro',bg='IndianRed3')
        self.lb5=Label(self,text='Valor vendido',bg='IndianRed3')
        self.lb6=Label(self,text='Data da venda',bg='IndianRed3')

        self.v=Entry(self)
        self.c=Entry(self)
        self.cpf=Entry(self)
        self.vc=Entry(self)
        self.vv=Entry(self)
        self.venda=Entry(self)



        self.lb.place(x=100,y=20)
        self.lb2.place(x=100,y=60)
        self.lb3.place(x=100,y=100)
        self.lb4.place(x=100,y=140)
        self.lb5.place(x=100,y=180)
        self.lb6.place(x=100,y=220)


        self.v.place(x=190,y=20)
        self.c.place(x=190,y=60)
        self.cpf.place(x=190,y=100)
        self.vc.place(x=190,y=140)
        self.vv.place(x=190,y=180)
        self.venda.place(x=190,y=220)

        self.bt=Button(self,text='Imprimir Nota',command=self.bt_imprimit)

        self.bt.place(x=190,y=300)

    def bt_imprimit(self):
        Nota1.imprimir(self)


    def imprimir(self):
        super().__init__()



        self.geometry("560x440+700+100")
        self.title('Cadastro')
        self["bg"]= "IndianRed3"
        self.grab_set()
        self.font= ('14')
        self.titulo = Label(self, text= 'NOTA FISCAL', font=('Arial', '20', 'bold'), bg='IndianRed3')
        self.titulo.pack(pady=10)

        self.lb=Label(self,text=self.v.get(),bg='IndianRed3')
        self.lb2=Label(self,text=self.c.get(),bg='IndianRed3')
        self.lb3=Label(self,text=self.cpf.get(),bg='IndianRed3')
        self.lb4=Label(self,text=self.vc.get(),bg='IndianRed3')
        self.lb5=Label(self,text=self.vv.get(),bg='IndianRed3')
        self.lb6=Label(self,text=self.venda.get(),bg='IndianRed3')

        self.vendendor=Label(self,text="Vendedor: ",bg='IndianRed3')
        self.comprador=Label(self,text="Comprador: ",bg='IndianRed3')
        self.cpf=Label(self,text="CPF: ",bg='IndianRed3')
        self.vc=Label(self,text="Valor do carro: ",bg='IndianRed3')
        self.vv=Label(self,text="Valor vendido: ",bg='IndianRed3')
        self.data=Label(self,text="Data de venda: ",bg='IndianRed3')

        self.vendendor.place(x=50,y=50)
        self.comprador.place(x=50,y=90)
        self.cpf.place(x=50,y=130)
        self.vc.place(x=50,y=170)
        self.vv.place(x=50,y=210)
        self.data.place(x=50,y=250)

        self.lb.place(x=150,y=50)
        self.lb2.place(x=150,y=90)
        self.lb3.place(x=150,y=130)
        self.lb4.place(x=150,y=170)
        self.lb5.place(x=150,y=210)
        self.lb6.place(x=150,y=250)

