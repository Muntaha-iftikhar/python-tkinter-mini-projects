from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

root = Tk()
root.title("Google Translator")
root.geometry("1100x500")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    l1.configure(text=c)
    l2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()  # Retrieve and clean text
        c2 = combo1.get()
        c3 = combo2.get()
        if text_:
            words = textblob.TextBlob(text_)
            lan = words.detect_language()
            lan_code = None
            for i, j in language.items():
                if j == c3:
                    lan_code = i
                    break
            if lan_code:
                words = words.translate(from_lang=lan, to=lan_code)
                text2.delete(1.0, END)
                text2.insert(END, words)
            else:
                messagebox.showerror("Error", "Selected language is not available.")
    except Exception as e:
        messagebox.showerror("Translation Error", "Please try again.")

# icon
img_icon = PhotoImage(file="google.png")
root.iconphoto(False, img_icon)

arrow_img = PhotoImage(file="google.png")
img_lbl = Label(root, image=arrow_img, width=150)
img_lbl.place(x=460, y=50)

language = googletrans.LANGUAGES
languageV = list(language.values())

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

l1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
l1.place(x=10, y=50)

f1 = Frame(root, bg="black", bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

Scroll1 = Scrollbar(f1)
Scroll1.pack(side=RIGHT, fill=Y)
Scroll1.config(command=text1.yview)
text1.config(yscrollcommand=Scroll1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

l2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
l2.place(x=620, y=50)

f2 = Frame(root, bg="black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

Scroll2 = Scrollbar(f2)
Scroll2.pack(side=RIGHT, fill=Y)
Scroll2.config(command=text2.yview)
text2.config(yscrollcommand=Scroll2.set)

translate = Button(root, text="Translate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.configure(bg="white")
root.mainloop()
