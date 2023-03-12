import codecs 
global home
import sqlite3
connection = sqlite3.connect("desburgers.db")
# cursor
global crsr
crsr = connection.cursor()
import os
path1=os.getcwd()
global card        
def card(title,description,button):
    try:
        f=open(path1+"/mesprsrages/card.html", 'rb')
        s=f.read().decode('utf-8')

        html=s % (title,description,button)
        return html
    except Exception as e:
        print("erreur card",e)
        return ""
global mycard        
def mycard(title,description,content):
    try:
        f=open(path1+"/mespages/card.html",'rb')
        s=f.read().decode('utf-8')
        html = s % n(title,description,content)
        return html
    except Exception as e:
        print("erreur card",e)
        return ""

from directory import directory 
class pagehome(directory):
    def __init__(self,title):
        self.title=title
        self.header=""
        self.footer=""
        self.js=""
        self.mimetype=200
        self.json=None
        self.redirect=None
        self.content=""
        self.css=""
        self.set_path("./home")
        self.set_title("Burger King")
        print('hi')
        self.set_header_with_path("header.html")
        self.set_footer_with_path("footer.html")
        
        j=open(self.get_filename_path("index.html"),'rb')
        text=j.read().decode('utf-8')
        print("my text",text)
        #print(result.group(1))
        crsr.execute("SELECT * FROM burgers")
        mycontent="<ul>"
        # store all the fetched data in the ans variable
        print("burgersok")
        ans = crsr.fetchall()
        print("burgers")

        print(mycontent)
        print("cards1")
        crsr.execute("SELECT * FROM cards")
        print("cards")
        mycontent=""
        # store all the fetched data in the ans variable
        ans = crsr.fetchall()
        print("allcards")
        print("cads")
        for x in ans:
            mycontent+= card(x[1],x[2],x[3])
        #print(mycontent)
        montitreici="Burger Queen"
        #print(text.decode('utf-8'))    
        print("le texte")
        text = text % ("",montitreici)
        
        self.set_path("./")
        self.set_content(text)
        print("le texte ok")    
        self.current_user=None
        #text=(text)
        print("hom function ok")
