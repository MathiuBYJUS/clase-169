from tkinter import*
root=Tk()
root.geometry("400x400")
root.config(bg="lightblue")

class clase:
    def __init__(self):
        print("Hola!")
        
    def a(self):
        label_1=Label(root,text="haz creado una etiqueta usando las clases")
        label_1.place(relx=0.5,rely=0.3,anchor=CENTER)
        button_2=Button(root,text="Dame click para ver un mensaje",command=self.c)
        button_2.place(relx=0.5, rely=0.5)
        
    def c(self):
        messshowinfo("showinfo", "You clicked the button created using class")
        
v=clase()
button_1=Button(root,text="Dame click para crear una etiqueta y un boton",command=v.a)
button_1.place(relx=0.5,rely=0.1,anchor=CENTER,)


root.mainloop()
