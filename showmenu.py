# -*- coding: utf-8 -*-
global showmenu
from directory import directory
import sqlite3
global connection
connection = sqlite3.connect("mesburgers1.db")
global crsr
crsr = connection.cursor()
class showmenupage(directory):
    def __init__(self,title,query_components):
        self.set_path("./menu")
        try:
            print("menu : ",query_components)
            catname=query_components.get("param2")
            print("catname : ",catname)
            crsr.execute("select * from burgercats where url = ?",(catname,))
            connection.commit()
            xx=crsr.fetchall()
            print(xx)
            if len(xx) > 0:
                catid=xx[0][0]
            elif len(xx) == 0:
                catid=None
        except:
            catid=None
            print("cat id is none")
        self.title=""
        self.css=""
        self.js=""
        print("show menu",query_components)
        self.set_title("Burger Menu")
        self.set_layout("ok")
        print("burger king")
        
        print('hi')
        self.set_header_with_path("header.html")
        
        sql_command = "select * from burgercats"
        message_else=""
        tablename="burgercats"
        

        contentpage=self.force_to_unicode(self.get_file("menu.html").read())
        mytabs=self.display_collection(sql_command, (), "_burgercat", message_else, tablename)
        #=======
        if query_components.get("param1") is not None:
            x=query_components.get("param1")[0]
        else:
            x=""
        print("")
        print("my tab name:",x)
        if (x == "fullmenu") or (catid is None):
            sql_command = "select * from burgercats"
            message_else="Il n'y a aucune catégorie"
            tablename="burgercats"
            myitems=self.display_collection(sql_command, (), "_myburgercat", message_else, tablename)
            contentpage=contentpage.replace("my items here",myitems)
        elif x == "recents" and query_components.get("userid") is not None:
            sql_command = "select * from burgers left join user_recents u on u.burger_id = burgers.id group by burgers.id having u.user_id = %s"
            message_else="commencez une commande pour voir les items ici<a href=\"/store-locator\">commencez à commander</a>"
            tablename="burgers"
            myarguments=(str(query_components.get("userid")[0]))
            myitems=self.display_collection(sql_command, myarguments, "_burger", message_else, tablename)
            contentpage=contentpage.replace("my items here",myitems)
        elif x == "recents":
            myitems="<h2>Sign In to Save Recents</h2><h3>Sign up or sign in to save your recents.</h3><a href=\"/signin\">Sign in</a>"
            contentpage=contentpage.replace("my items here",myitems)
        elif x == "favorites" and query_components.get("userid") is not None:
            sql_command = "select * from burgers left join user_favs u on u.burger_id = burgers.id group by burgers.id having u.user_id = %s"
            message_else="Favorisez un article de votre panier ou des articles récents pour l'enregistrer en tant que favori."
            tablename="burgers"
            myarguments=(str(query_components.get("userid")[0]))
            myitems=self.display_collection(sql_command, myarguments, "_burger", message_else, tablename)
            contentpage=contentpage.replace("my items here",myitems)
        elif x == "favorites":
            myitems="<h2>Sign In to Save Favorites</h2><h3>Sign up or sign in to save your favorites.</h3><a href=\"/signin\">Sign in</a>"
            contentpage=contentpage.replace("my items here",myitems)

        elif catid is not None:
            sql_command = "select burgers.* from burgers where burgercat_id = ?"
            message_else="Il n'y a aucun item < a href=\"/menu\">Retour au menu</a>"
            tablename="burgers"
            myitems=self.display_collection_sql(sql_command, (str(catid),), "_burger", message_else, tablename)
            contentpage=contentpage.replace("my items here",myitems)

        #=======

        contentpage=contentpage.replace("my tabs here",mytabs)
        try:
            self.set_content(self.force_to_unicode(contentpage))
            self.set_mimetype("html")
            self.set_footer("")
            self.add_css("mymenu.css")

        except Exception as e:

            print("erreur",e)
        self.set_path("./menu/")
  
