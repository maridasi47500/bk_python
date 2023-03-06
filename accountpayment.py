global accountpayment
import directory
def accountpayment(params = None):
    try:
        Program=directory("")
        print("account payment: current user")
        print(session.current_user)
        Program.set_path("./mespages")
        j=codecs.open(Program.get_filename_path("accountpayment.html"))
        Program.set_path("./css")
        Program.set_css("")
        Program.add_css("accountpaiement.css")
        text=force_to_unicode(j.read())
        #sql,templatename,errormessage,tablename
        mysql="select * from creditcards where orders.user_id = %s" % (session.current_user[0])
        str=display_collection(mysql,(),"_modedepaiement","Aucun mode de paiement n'a été ajouté","creditcards")
        text=text.replace("ici le mode de paiement",str)
        Program.set_content(text)
        Program.set_path("./mespages")
        k=codecs.open(Program.get_filename_path("headersignin.html"))
        headertext=k.read()
        Program.set_header(headertext)

        return render_figure("my page.html")
    except Exception as e:
        print("account payment erreur",e)
