from directory import directory
import re
import sqlite3
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
import os
path1=os.getcwd()
class showburgerpage(directory):
    
    def __init__(self,title):
        self.title=title
    def __init__(self,path,title,query_components):
        self.set_path(path)
        self.css=""
        self.js=""
        print("show menu",query_components)
        dataparams={"1":"burger1=sandwich&burger2=sandwich&drink1=small&drink2=small&side1=small&side2=small","2":"burger=burger&burger=value","3":"burger=burger&burger=value","4":"burger=side&burger=value","5":"burger=drink&burger=value","6":"burger=sweet&burger=value","7":"burger=burgerjr&burger=value&jrsides=jrsides&jrdrinks=jrdrinks&jrtreats=toy&burgerid="}
        self.set_title("Burger King")
        self.set_layout("ok")
        print("burger king")
        self.add_css("burger.css")
        self.add_js("burger.js")

        

        print('hi')
        self.set_path(path)
        self.set_header_with_path("headersignin.html")
        self.set_header(self.get_header().replace("\"/\"","\"/menu\""))
        self.set_footer_with_path("footer.html")
        burgerid=re.findall("\d+",str(query_components.get("param0")))[0]
        sql_command = "select * from burgers where burger_number = %s" % (burgerid)
        crsr.execute(sql_command)
        connection.commit()
        res=crsr.fetchall()
        message_else=""
        tablename="burgers"
        matable=self.infotable(tablename)

        contentpage=self.force_to_unicode(self.get_file("burger.html").read())
        contentpage=contentpage.replace("<!-- myparams -->",dataparams[str(res[0][7])]+"&burgerid="+str(res[0][0]))
        sql_command = "select * from nutinfos where burger_id = %s" % (burgerid)
        tablename="nutinfos"
        message_else="Aucune information n'est disponible."
	self.set_path("./showburger/custom")
        collectionstr= self.display_collection(sql_command, (), "_infonutrition", message_else, tablename)

        contentpage=contentpage.replace("info nutritionnelle ici",collectionstr)
        sql_command = "select * from burgers where burgercat_id in (%s,%s) and burger_number = %s" % ("2","3",burgerid)
        tablename="burgers"
        message_else=""
        collectionstr= self.display_collection(sql_command, (), "_combosize", message_else, tablename)
        contentpage=contentpage.replace("<!-- size combo here -->",collectionstr)

        sql_command = "select * from burgers where burgercat_id in (%s,%s) and burger_number = %s" % ("4","5",burgerid)
        collectionstr= self.display_collection(sql_command, (), "_valuesize", message_else, tablename)
        contentpage=contentpage.replace("<!-- size item here -->",collectionstr)
        sql_command = "select burgers.* from burgers where burger_number = %s and burgers.burgercat_id = %s" % (burgerid,1)
        collectionstr= self.display_collection(sql_command, (), "_customizeburger", message_else, tablename)
        contentpage=contentpage.replace("<!-- personnaliser votre burger -->",collectionstr)
	self.set_path("./showburger")

        
        if len(res) > 0:
            for resu in res:
                paspremier = False
                contentpage=self.force_to_unicode(contentpage)
                for x in range(len(resu)):
                    print(x)
                    print(resu[x])
                    z=resu[x]
                    strrep=self.force_to_unicode("(%s)" % (matable[x][1]))
                    print(strrep)
                    if type(z) == int or type(z) == float:
                        z=str(z)
                    if z is not None:
                        contentpage=contentpage.replace(strrep, self.force_to_unicode(z))
        loggedin=True
        if loggedin:
            g=self.get_file("./customize.html").read()
            contentpage=contentpage.replace("<!-- personnaliser ma commande-->",g)
            
        self.set_content(contentpage)    
