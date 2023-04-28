# -*- coding: utf-8 -*-
from directory import directory
global menu
import re
import os
from displaythisburger import pagedisplaythisburger
import sqlite3
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
class menupage(directory):
    def __init__(self,title,params):
        self.title=title
        self.set_path("./menu")
        j=open(self.get_filename_path("menu.html"),'rb')
        text=j.read()
        result = re.search("<nav class=\"mytabs\"><ul>(.*)</ul></nav>",text)
        #print(result.group(1))
        #crsr.execute("SELECT * FROM cats")
        mycontent=""
        # store all the fetched data in the ans variable
        print("burgersok")
        ans = crsr.fetchall()
        print("burgers")
        try:
          print(params["userid"][0])
          #si l'uilisateur n'a pas de BK restaurant et est onnecté
          #rediriger vers page de lieu
          #self.set_header_with_path("mynavsignedin.html")
        except:
          #self.set_header_with_path("mynav.html")
          print("user non connecté========!!!'''--'''!!!")
        for myburger in ans:
            #print("burger",myburger[1],mycontent)
            mycontent+= "<li class=\"mycat\"><a href=\"/menu/"+repr(myburger[0] if myburger[0] > 1 else '')+"\">"+(myburger[1]).encode('utf-8')+"</a></li>"
        if result is not None and len(result.group(1)) > 0:
            text=text.replace(result.group(1),mycontent)
        for myburger in ans:
            mesburgers=""
            print("burger?!%*#")
            crsr.execute("SELECT * FROM burgers where burgercat_id = '"+repr(myburger[0])+"'")
            res=re.search("<div class=\"myitems\"><ul>(.*?)</ul></div>",text)
            ans1 = crsr.fetchall()
            for burger in ans1:
                #print("burger",burger[1])
                print("erreur ici")
                b=pagedisplaythisburger(burger,myburger[1],myburger[0]).get_content()
                print("myerreur")
                j=open(os.getcwd()+"/listburger/_modelburger.html","rb")
                s= j.read().decode('utf-8') % (str(burger[0]),(burger[1].encode('utf-8')))
                mesburgers+= s
                print("erreur")
            if mesburgers == "":
                mesburgers = "mes items ici"
            if res is not None and len(res.group(1)) > 0:
                text=text.replace(res.group(1),mesburgers)
            print("burgervalue")
            #print(myburger[1])
            self.set_path("./menu")
            try:
                userid=(params["userid"][0],)
                preorder=crsr.execute("SELECT * FROM preorders where user_id = ?",(userid,))
                if len(preorder) > 0:
                    self.add_css("menu.css")
                    text+=self.get_file("./addmessage.html").read() 
            except:
                print("pas de produit ajouté".decode("utf-8"))
            self.set_content(text)
            page=str(myburger[0] if myburger[0] > 1 else 'index')
