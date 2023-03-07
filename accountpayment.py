global accountpayment
import directory
from directory import directory
class pageaccountpayment(directory):
    self.__init__(self,title):
    self.title=title
    j=codecs.open(self.get_filename_path("accountpayment.html"))
    self.set_path("./css")
    self.set_css("")
    self.add_css("accountpaiement.css")
    text=force_to_unicode(j.read())
    #sql,templatename,errormessage,tablename
    mysql="select * from creditcards where orders.user_id = %s" % (session.current_user[0])
    str=display_collection(mysql,(),"_modedepaiement","Aucun mode de paiement n'a été ajouté","creditcards")
    text=text.replace("ici le mode de paiement",str)
    self.set_content(text)
    self.set_path("./mespages")
    k=codecs.open(self.get_filename_path("headersignin.html"))
    headertext=k.read()
    self.set_header(headertext)


