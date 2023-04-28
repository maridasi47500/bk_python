# coding=utf-8
import codecs 
global home
import sqlite3
connection = sqlite3.connect("mesburgers1.db")
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
    def __init__(self,title,params):
        self.title=title
        self.header=""
        self.footer=""
        self.js=""
        self.html=""
        self.layout=None
        self.response=""
        self.mime="html"
        self.json=None
        self.redirect=None
        mycontent=""
        self.content=""
        self.css=""
        self.set_title("Burger King")
        self.set_path("./home")
        q=""
        print('hi')
        try:
          print(params["userid"][0])
          userid=params["userid"][0]
          self.set_header_with_path("mynavsignedin.html")
          #vous vous etes bien connecté ===> message fenetre ajouter un toast!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
          users=crsr.execute("select * from users where user_number = ?",(userid,)).fetchall()[0]
          if str(users[-1]) == "1":
            #self.add_css("toast.css")
            self.add_js("signedin.js")
            q+=self.get_file("signedin.html").read().decode("utf-8") % "vous vou es bien connecté-e.".decode('utf-8')
            mycontent+=q
            crsr.execute("update users set signedin = ? where user_number = ?",(0,users[0]))
            connection.commit()
          elif str(users[-1]) == "2":
            #self.add_css("toast.css")
            self.add_js("signedin.js")
            q+=self.get_file("signedin.html").read().decode("utf-8") % "vous vou es bien inscrit-e sur bk. Bienvenue.".decode('utf-8')
            mycontent+=q
            crsr.execute("update users set signedin = ? where user_number = ?",(0,users[0]))
            connection.commit()

        except Exception as e:
          print("quelle erreur?",e)
          self.set_header_with_path("mynav.html")
        self.set_footer_with_path("footer.html")
        j=open(self.get_filename_path("index.html"),'rb')
        text=j.read().decode('utf-8')
        #print("my text",text)
        #print(result.group(1))
        crsr.execute("SELECT * FROM burgers")
        mycontent+="<ul>"
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
        #for x in ans:
        #    mycontent+= card(x[1],x[2],x[3])
        #print(mycontent)
        montitreici="Burger Queen"
        #print(text.decode('utf-8'))    
        print("le texte")
        text = text % ("",montitreici)
        
        self.add_css("home.css")
        self.add_css("account.css")
        self.add_css("signin.css")


        try:
            user_id=params["userid"][0]
            sql="select * from preorders where user_id = ? and display = ?"
            o=crsr.execute(sql,(user_id,"0"))
            p=o.fetchall()
            print(p[0])
            paspremier=False
            burgerslist=""
            for burger in p:
              if paspremier:
                burgerslist+=", "
              paspremier=True
              print("order : ",burger)
              burgernom=crsr.execute("select * from burgers where burger_number = ?",(burger[1],)).fetchall()[0][1]
              print(burgernom)
              crsr.execute("update preorders set display = 1 where id = ?",(burger[0],))
              connection.commit()
              burgerslist+=burgernom
            q=self.get_file("burgerajoute.html").read().decode("utf-8")
            print(q[0:40])
            if len(p) == 1:
              q=q % self.force_to_unicode(("votre burger a été ajouté (%s)".decode('utf-8') % burgerslist).encode('utf-8'))
            else:
              q=q % self.force_to_unicode(("vos burgers ont été ajoutés (%s)".decode('utf-8') % burgerslist).encode('utf-8'))
            self.add_js("burgerajoute.js")
            print("ok BURGER AJOUTE¡$$")
        except Exception as e:
            print(e,"ok user non connecté ???? u're OFFLINE")
        self.set_content(text+q)
        print("le texte ok")    
        self.current_user=None
        #text=(text)
        print("hom function ok")
