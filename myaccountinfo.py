from directory import directory
import sqlite3
global crsr
connection = sqlite3.connect("mesburgers1.db")

crsr = connection.cursor()

myusers=crsr.execute("PRAGMA table_info([users])")
table_users = myusers.fetchall()
global myaccountinfo
class myaccountinfopage(directory):
    def __init__(self,title,params):
        try:
            myusers=crsr.execute("select * from users where user_number = ?",((params["userid"][0]),))
            current_user = myusers.fetchall()[0]
            print("current user :::: ",current_user)
        except Exception as e:
            current_user=None
            print("erreur",e)
        print("account info: current user")
        self.set_path("./accountinfo")
        print("ici")
        self.set_header_with_path("headersignin.html")
        print("la")
        #self.set_footer_with_path("footer.html")
        print(" et la")
        self.set_mimetype("html")
        #print(current_user)

        j=self.get_file("accountinfo.html").read()
        text=j
        self.set_css("")
        self.add_css("account.css")
        self.add_css("signin.css")
        self.add_js("saveinfo.js")
        self.set_title(title)
        self.edit_title("Account Details")
        try:
            if current_user is not None:
                for a in range(len(current_user)):
                    try:
                        if current_user[a] is not None:
                            idstring="id=\""+self.force_to_unicode(table_users[a][1])+"\""
                            print(idstring)
                            idvaluestring=(idstring+" value=\""+str(current_user[a])+"\" ")
                            if self.force_to_unicode(table_users[a][1]) == u'offres':
                                text=text.replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                            text=self.force_to_unicode(text).replace(idstring,idvaluestring)

                            if self.force_to_unicode(table_users[a][1]) == u'dateofbirth':
                                date=current_user[a].split(" ")[0]
                                print("date : "+date)
                                idstring="id=\""+"yy"+"\""
                                idvaluestring=(idstring+" value=\""+date.split("-")[0]+"\" ").replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                                text=self.force_to_unicode(text).replace(idstring,idvaluestring)
                                idstring="id=\""+"mm"+"\""
                                idvaluestring=(idstring+" value=\""+date.split("-")[1]+"\" ").replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                                text=self.force_to_unicode(text).replace(idstring,idvaluestring)
                                idstring="id=\""+"dd"+"\""
                                idvaluestring=(idstring+" value=\""+date.split("-")[2]+"\" ").replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                                text=self.force_to_unicode(text).replace(idstring,idvaluestring)

                    except Exception as e:
                        print("mon texte erreur",e)
                        pass
        except:
            print("erreur afficher le formulaire")
        print("longueur du texte",len(text))
        self.set_content(self.force_to_unicode(text.encode('utf-8')))

