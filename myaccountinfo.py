from directory import directory
global myaccountinfo
class myaccountinfopage(directory):
    def __init__(self):
        print("account info: current user")
        print(session.current_user)
        self.set_path("./mespages")
        j=open(self.get_filename_path("accountinfo.html"),'rb')
        text=j.read()
        self.set_css("")
        self.set_path("./css")
        self.add_css("account.css")
        self.add_css("signin.css")
        self.set_path("./js")
        self.add_js("saveinfo.js")
        self.edit_title("Account Details")
        try:
            if session.current_user is not None:
                for a in range(len(session.current_user)):
                    try:
                        if session.current_user[a] is not None:
                            idstring="id=\""+force_to_unicode(table_users[a][1])+"\""
                            print(idstring)
                            idvaluestring=(idstring+" value=\""+str(session.current_user[a])+"\" ")
                            if force_to_unicode(table_users[a][1]) == u'offres':
                                text=text.replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                            text=force_to_unicode(text).replace(idstring,idvaluestring)

                            if force_to_unicode(table_users[a][1]) == u'dateofbirth':
                                date=session.current_user[a].split(" ")[0]
                                print("date : "+date)
                                idstring="id=\""+"yy"+"\""
                                idvaluestring=(idstring+" value=\""+date.split("-")[0]+"\" ").replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                                text=force_to_unicode(text).replace(idstring,idvaluestring)
                                idstring="id=\""+"mm"+"\""
                                idvaluestring=(idstring+" value=\""+date.split("-")[1]+"\" ").replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                                text=force_to_unicode(text).replace(idstring,idvaluestring)
                                idstring="id=\""+"dd"+"\""
                                idvaluestring=(idstring+" value=\""+date.split("-")[2]+"\" ").replace("value=\"1\"","value=\"1\" checked=\"checked\"")
                                text=force_to_unicode(text).replace(idstring,idvaluestring)

                    except Exception as e:
                        print("mon texte erreur",e)
        except:
            print("erreur afficher le formulaire")
        self.set_content(text)
        self.set_path("./accountinfo")
        self.set_my_header("headersignin")
        self.set_my_footer("footer")

