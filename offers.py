# coding=utf-8
import sqlite3
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
from erreur import erreur
import traceback

class offerspage(directory):
  def __init__(self,path,title,params):
    try:
      self.set_path(path)

      self.title=title
      self.params=title

      try:
        userid=params["userid"][0]
        self.set_header_with_path_and_address("headersignedin.html",userid)
        sql="select *, (select count(offers.id) from offers where offers.burger_id = burgers.burger_number ) as countoffers, (select count(offers.id) from offers where offers.bk_id = (select restaurant_id from users where user_number = ?)) as countrestaus from burgers where countoffers > 0 and countrestaus > 0 "
        myparams=("countoffers","countrestaus",)
        myarg=(userid,)
      except:
        userid=None
        self.set_header_with_path("mynav.html")
        sql="select *, (select count(offers.id) from offers where offers.burger_id = burgers.burger_number) as countoffers from burgers where countoffers > 0"
        myarg=()
        myparams=("countoffers",)
      self.set_footer_with_path("footer.html")
      tablename="burgers"
      message_else="Aucune offre n'est disponible."

      collectionstr= self.display_collection(sql, myarg, "_offre", message_else, tablename,False,False,myparams)
      self.content_from_file_yield("myoffershtml.html",collectionstr)
    except Exception as e:
      self.__class__ = erreur
      self.set_erreur(str(e))
      self.set_title("/rewards/offers")
      self.set_erreur(str(traceback.format_exc()))
      self.set_title("Erreur route home: "+str(e))

