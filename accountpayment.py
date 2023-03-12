# -*- coding: utf-8 -*-
global accountpayment
import directory
from directory import directory
class pageaccountpayment(directory):
    def __init__(self,title,user):
        self.title=title
        j=open(self.get_filename_path("accountpayment.html"), "rb")
        self.set_path("./css")
        self.set_css("")
        self.add_css("accountpaiement.css")
        text=j.read().decode('utf-8')
        #sql,templatename,errormessage,tablename
        mysql="select * from creditcards where orders.user_id = %s" % (user)
        str=self.display_collection(mysql,(),"_modedepaiement","Aucun mode de paiement n'a été ajouté","creditcards")
        text=text.replace("ici le mode de paiement",str)
        self.set_content(text)
        self.set_path("./mespages")
        k=codecs.open(self.get_filename_path("headersignin.html"))
        headertext=k.read()
        self.set_header(headertext)


