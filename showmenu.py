global showmenu
from directory import directory
class showmenupage(directory):
    def __init__(self,title,query_components):
        self.title=""
        print("show menu",query_components)
        self.set_title("Burger King")
        self.set_layout("ok")
        print("burger king")
        
        print('hi')
        self.set_header_with_path("header.html")
        self.set_footer_with_path("footer.html")
        sql_command = "select * from burgercats"
        message_else=""
        tablename="burgercats"
        

        contentpage=force_to_unicode(get_file("menu.html").read())
        mytabs=display_collection(sql_command, (), "_burgercat", message_else, tablename)
        #=======
        if query_components.get("mytab") is not None:
            x=query_components.get("mytab")[0]
        else:
            x=""
        print("")
        print("my tab name:",x)
        if x == "fullmenu":
            sql_command = "select * from burgercats"
            message_else="Il n'y a aucune catégorie"
            tablename="burgercats"
            myitems=display_collection(sql_command, (), "_myburgercat", message_else, tablename)
            contentpage=contentpage.replace("my items here",myitems)
        elif x == "recents" and query_components.get("userid") is not None:
            sql_command = "select * from burgers left join user_recents u on u.burger_id = burgers.id group by burgers.id having u.user_id = %s"
            message_else="commencez une commande pour voir les items ici<a href=\"/store-locator\">commencez à commander</a>"
            tablename="burgers"
            myarguments=(str(query_components.get("userid")[0]))
            myitems=display_collection(sql_command, myarguments, "_burger", message_else, tablename)
            contentpage=contentpage.replace("my items here",myitems)
        elif x == "recents":
            myitems="<h2>Sign In to Save Recents</h2><h3>Sign up or sign in to save your recents.</h3><a href=\"/signin\">Sign in</a>"
            contentpage=contentpage.replace("my items here",myitems)
        elif x == "favorites" and query_components.get("userid") is not None:
            sql_command = "select * from burgers left join user_favs u on u.burger_id = burgers.id group by burgers.id having u.user_id = %s"
            message_else="Favorisez un article de votre panier ou des articles récents pour l'enregistrer en tant que favori."
            tablename="burgers"
            myarguments=(str(query_components.get("userid")[0]))
            myitems=display_collection(sql_command, myarguments, "_burger", message_else, tablename)
            contentpage=contentpage.replace("my items here",myitems)
        elif x == "favorites":
            myitems="<h2>Sign In to Save Favorites</h2><h3>Sign up or sign in to save your favorites.</h3><a href=\"/signin\">Sign in</a>"
            contentpage=contentpage.replace("my items here",myitems)

        elif query_components.get("catid") is not None:
            sql_command = "select * from burgers where burgercat_id = %s"
            message_else="Il n'y a aucun item < a href=\"/menu\">Retour au menu</a>"
            tablename="burgers"
            myitems=display_collection(sql_command, (str(query_components.get("catid")[0])), "_burger", message_else, tablename)
            contentpage=contentpage.replace("my items here",myitems)

        #=======

        contentpage=contentpage.replace("my tabs here",mytabs)
        try:
            self.set_content(force_to_unicode(contentpage))
            self.set_mimetype("html")
            self.set_footer("")
            self.add_css("mymenu.css")

        except Exception as e:

            print("erreur",e)
  
