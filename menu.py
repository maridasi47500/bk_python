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
    def __init__(self,title):
        self.title=title
        self.set_path("./menu")
        j=open(self.get_filename_path("menu.html"),'rb')
        text=j.read()
        result = re.search("<nav class=\"mytabs\"><ul>(.*)</ul></nav>",text)
        #print(result.group(1))
        crsr.execute("SELECT * FROM cats")
        mycontent=""
        # store all the fetched data in the ans variable
        print("burgersok")
        ans = crsr.fetchall()
        print("burgers")
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
            self.set_content(text)
            page=str(myburger[0] if myburger[0] > 1 else 'index')

