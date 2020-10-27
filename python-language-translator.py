from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES


root = Tk()
root.geometry('1200x480')
root.resizable(0,0)
root.title("Project--  Rahman Language Translator")
root.config(bg = 'blue')

#heading
Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()
Label(root,text ="Developed By Rahman", font = 'arial 20 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')



#INPUT AND OUTPUT TEXT WIDGET
Label(root,text ="Enter Text", font = 'arial 18 bold', bg ='white smoke').place(x=250,y=60)
Input_text = Text(root,font = 'arial 13',bg='black',fg='white', height = 11, wrap = WORD, padx=5, pady=5, width = 60,insertbackground='white')
Input_text.place(x=30,y = 100)
# Input_text.configure( insertbackground='white')

Label(root,text ="Output", font = 'arial 18 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(root,font = 'arial 13',bg='black',fg='white', height = 11, wrap = WORD, padx=5, pady= 5, width =60,insertbackground='white')
Output_text.place(x = 600 , y = 100)
# Output_text.configure( insertbackground='white')

##################
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root,font = 'arial 13', values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('english')

dest_lang = ttk.Combobox(root,font = 'arial 13', values= language, width =22)
dest_lang.place(x=890,y=60)
dest_lang.set('hindi')
########################################  Define function #######

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
   


##########  Translate Button ########
trans_btn = Button(root, text = 'Translate',bg='#f55c33',font = 'arial 18 bold',pady = 5,command = Translate )
trans_btn.place(x = 540, y = 330)

# trans_btn.bind('<Return>',Translate)

root.mainloop()

