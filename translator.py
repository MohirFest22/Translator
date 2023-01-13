from tkinter import *
from googletrans import Translator
#from tkinter import messagebox
import webbrowser
window = Tk()
window.geometry("1600x900")
window.title("Translator")

main_menu = Menu()
window.config(menu=main_menu)

def programmer():
	programmer = Toplevel(window)
	programmer.geometry("900x600")
	programmer.title("About Programmer")
	programmer_l = Label(programmer,text="About  Pogrammer",font="Stencil 20")
	programmer_l.pack()
	programmer_about = Label(programmer,text="My name is Sunnatjon, my surname is Arslonov.\n I'm 16 years old. I know HTML-70%, CSS-30%, BOOTSTRAP-20%, PYTHON-50%. \nI mostly write codes in Python. I want to become a FullStack developer \nin the future",font="Franklin 15 bold")
	programmer_about.pack(padx="50",pady="70")
	programmer_page = Label(programmer,text="👇🏻 My page on social networks 👇🏻",font="Franklin 18 bold")
	programmer_page.pack()

	def tg_link():
		url = "https://t.me/sunnatjonpy"
		webbrowser.open_new(url)
	def ins_link():
		url = "https://www.instagram.com/sunnatjon.py/"
		webbrowser.open_new(url)
	def fc_link():
		url = "https://www.facebook.com/profile.php?id=100088538125935"
		webbrowser.open_new(url)
	tg= Button(programmer,text="Telegram",command=tg_link).place(x="200",y="370",width="100",height="50")
	ins= Button(programmer,text="Instagram",command=ins_link).place(x="400",y="370",width="100",height="50")
	fc = Button(programmer,text="Facebook",command=fc_link).place(x="600",y="370",width="100",height="50")

def tg_linkk():
		url = "https://t.me/mohirdev22"
		webbrowser.open_new(url)

def about():
	about = Toplevel(window)
	about.geometry("900x400")
	about.title("About the Program")
	about_l = Label(about,text="About  the  Program",font="Stencil 20")
	about_l.pack()
	program_about = Label(about,text="The program is written using the Python programming language,\n and this program is a Desktop program. This program is compiled using\n Python's <Tkinter>, <Googletrans> modules.\n The code of the program is more than 250, in which various functions are located ",font="Franklin 15 bold")
	program_about.pack(padx="50",pady='110')

def prog_func():
	func = Toplevel(window)
	func.geometry("900x400")
	func.title("Function the Program")
	func_l = Label(func,text="Function  the  Program",font="Stencil 20")
	func_l.pack()
	func_about = Label(func,text="The main function of the program is to translate the text. \nYou can select the language from which to translate by pressing\n the <From which language> button and select the language to be translated \nby pressing the <To which language> button,\n then enter text. You can get information by choosing one of the menus.",font="Franklin 15 bold")
	func_about.pack(padx="50",pady="100")

def use():
	using = Toplevel(window)
	using.geometry("1200x500")
	using.title("Use the Program")
	using_l = Label(using,text="Using  the  Program",font="Stencil 20")
	using_l.pack()
	using_1_button = Label(using,text="1.FROM WHiCH LANGUAGE  button    --- ",font="Arial 14 bold")
	using_1_button_t = Label(using,text="With this button, you choose from which language you want to translate",font="Franklin 13 ")
	using_2_button = Label(using,text="2.TO WHICH LANGUAGE button    --- ",font="Arial 14 bold")
	using_2_button_t = Label(using,text="With this button you can choose which language to translate to",font="Franklin 13")
	using_input = Label(using,text="3.INPUT    --- ",font="Arial 14 bold")
	using_input_t = Label(using,text="You enter the text to be translated through the input section",font="Franklin 13")
	using_trans_button = Label(using,text="4.TRANSLATE button    --- ",font="Arial 14 bold")
	using_trans_button_t = Label(using,text="With this button you can click to translate the text",font="Franklin 13")
	using_consol = Label(using,text="5.CONSOL    --- ",font="Arial 14 bold")
	using_consol_t = Label(using,text="This section is a text translation window",font="Franklin 13 ")
	using_1_button.place(x="30",y="100")
	using_1_button_t.place(x="430",y="105")
	using_2_button.place(x="30",y="140")
	using_2_button_t.place(x="390",y="145")
	using_input.place(x="30",y="180")
	using_input_t.place(x="180",y="185")
	using_trans_button.place(x="30",y="220")
	using_trans_button_t.place(x="290",y="225")
	using_consol.place(x="30",y="260")
	using_consol_t.place(x="205",y="265")







prog_menu = Menu(main_menu, tearoff=0)
about_menu = Menu(main_menu, tearoff=0)
help_menu = Menu(main_menu, tearoff=0)

prog_menu.add_command(label="Programmer",command=programmer)
prog_menu.add_command(label="Connect", command=tg_linkk)

about_menu.add_command(label="About program",command=about)
about_menu.add_command(label="Program fuction",command=prog_func)

help_menu.add_command(label="For questions",command=tg_linkk)
help_menu.add_command(label="Using program",command=use)

main_menu.add_cascade(label="Program",menu=prog_menu)
main_menu.add_cascade(label="About",menu=about_menu)
main_menu.add_cascade(label="Help",menu=help_menu)

lang_src = ["Uzbek","Russian","English","Arabic","German","Turkish","Italian","Spanish","French","Kazakh","Kyrgyz","Hindi","Japan","Korean"]
lang_srcc_v = StringVar()
lang_srcc_v.set("From which language")

lang_dest_v= StringVar()
lang_dest_v.set("To which language")



languages = ["Uz","En","Ru"]
languages_v = StringVar()
languages_v.set("Language")
def language_func(noargument):
	if languages_v.get()=="Uz":
		window.title("Tarjimon")
		prog_name.config(text="Tarjimon")
		prog_menu.add_cascade(label="Dastur")
		lang_srcc_v.set("Qaysi tildan")
		lang_dest_v.set("Qaysi tilga")
		result_btn.config(text="TARJIMA")
	elif languages_v.get()=="En":
		window.title("Translator")
		prog_name.config(text="Translator")
		lang_srcc_v.set("From which language")
		lang_dest_v.set("To which language")
		result_btn.config(text="TRANSLATE")
	elif languages_v.get()=="Ru":
		window.title("Переводчик")
		prog_name.config(text="Переводчик")
		lang_srcc_v.set("с какого языка")
		lang_dest_v.set("какой язык")
		result_btn.config(text="ПЕРЕВОД")


languages_choise = OptionMenu(
    window,
    languages_v,
    *languages,
    command=language_func
)
languages_choise.pack(anchor="ne",padx="50",pady="20")


prog_name = Label(text="TRANSLATOR",fg="blue",width="40",height="3",font="Stencil 40")
prog_name.pack(side=TOP)

get_var = StringVar()






def srcc_choicee(choice):
    choice = lang_srcc_v.get()
    if choice == "Uzbek":
    	srcc_logo.config(text="uz")
    elif choice == "Russian":
    	srcc_logo.config(text="ru")
    elif choice == "English":
    	srcc_logo.config(text="en")  
    elif choice =="Arabic":
    	srcc_logo.config(text="ar")  	
    elif choice == "German":
    	srcc_logo.config(text="de")
    elif choice == "Spanish":
    	srcc_logo.config(text="es")
    elif choice == "Turkish":
    	srcc_logo.config(text="tr")
    elif choice == "Italian":
    	srcc_logo.config(text="it")
    elif choice == "French":
    	srcc_logo.config(text="fr")
    elif choice == "Kazakh":
    	srcc_logo.config(text="kk")
    elif choice == "Kyrgyz":
    	srcc_logo.config(text="ky")
    elif choice == "Hindi":
    	srcc_logo.config(text="hi")
    elif choice == "Japan":
    	srcc_logo.config(text="ja")
    elif choice == "Korean":
    	srcc_logo.config(text="ko")	



srcc = OptionMenu(
    window,
    lang_srcc_v,
    *lang_src,
    command=srcc_choicee
)
srcc.place(x="350",y="260",width="200",height="60")

def dest_choicee(choice):
    choice = lang_dest_v.get()
    if choice == "Uzbek":
    	en_logo.config(text="uz")
    elif choice == "Russian":
    	en_logo.config(text="ru")
    elif choice == "English":
    	en_logo.config(text="en")
    elif choice == "Arabic":
    	en_logo.config(text="ar") 
    elif choice == "German":
    	en_logo.config(text="de")
    elif choice == "Spanish":
    	en_logo.config(text="es")
    elif choice == "Turkish":
    	en_logo.config(text="tr")
    elif choice == "Italian":
    	en_logo.config(text="it")
    elif choice == "French":
    	en_logo.config(text="fr")
    elif choice == "Kazakh":
    	en_logo.config(text="kk")
    elif choice == "Kyrgyz":
    	en_logo.config(text="ky")
    elif choice == "Hindi":
    	en_logo.config(text="hi")
    elif choice == "Japan":
    	en_logo.config(text="ja")
    elif choice == "Korean":
    	en_logo.config(text="ko")	


destt = OptionMenu(
    window,
    lang_dest_v,
    *lang_src,
    command=dest_choicee
)

destt.place(x="950",y="260",width="200",height="60")
#translator = Translator()
#result_word = (translator.translate(get_var.get(), src="uz", dest="ru")).text

words = Entry(font="Berlin 20",textvariable=get_var)
words.place(x="50",y="400",width="1440",height="50")

en_logo = Label(text="",font="Haettenschweiler 20")
en_logo.place(x="25",y="610",width="20")
srcc_logo = Label(text="",font="Haettenschweiler 20")
srcc_logo.place(x="25",y="410",width="20")

def translate_get():
	translator = Translator()
	result_word = (translator.translate(get_var.get(), src=srcc_logo["text"], dest=en_logo["text"])).text
	result_consol_en.config(text=result_word)
	

result_consol_en = Label(bg="white",font="Berlin 15")
result_consol_en.place(x="50",y="600",width="1440",height="50")

#goto_label = Label(f"From {srcc_logo["text"]} to {en_logo["text"]}")
#goto_label.place(x='550', y="200",width="200",height="60")

result_btn = Button(text="TRANSLATE",bg="ivory",font="Algerian 20",command=translate_get)
result_btn.place(x="600",y="500",width="350",height="75")

window.mainloop()
#ru_logo = Label(text="RU",font="Haettenschweiler 20")
#ru_logo.place(x="25",y="560",width="20")
#result_consol_ru = Label(bg="white",font="Berlin 15")
#result_consol_ru.place(x="50",y="550",width="1440",height="50")