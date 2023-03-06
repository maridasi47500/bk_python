import directory
global myaccountinfo
def myaccountinfo(params = None):
    try:
        Program=directory("")
        print("account info: current user")
        print(session.current_user)
        Program.set_path("./mespages")
        j=codecs.open(Program.get_filename_path("accountinfo.html"))
        text=j.read()
        Program.set_css("")
        Program.set_path("./css")
        Program.add_css("account.css")
        Program.add_css("signin.css")
        Program.set_path("./js")
        Program.add_js("saveinfo.js")
        Program.edit_title("Account Details")
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
        Program.set_content(text)
        Program.set_path("./accountinfo")
        set_my_header("headersignin")
        set_my_footer("footer")
        return render_figure("index.html")

    except Exception as e:
        print("erreur my account info page",e)

