# coding=utf-8
import sqlite3
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
import traceback
global crsr
crsr = connection.cursor()
from erreur import erreur

class rewardspage(directory):
  def __init__(self,path,title,params):
    try:
      self.set_path(path)
      self.content_from_file("myrewardshtml.html")
      self.title=title
      self.params=title


      try:
        userid=params["userid"][0]
        self.set_header_with_path_and_address("headersignedin.html",userid)
        sql="select *, (select count(offers.id) from offers where offers.burger_id = burgers.id ) as countoffers, (select count(offers.id) from offers where offers.bk_id = (select restaurant_id from users where user_number = ?)) as countrestaus from burgers where countoffers > 0 and countrestaus > 0 "
      except Exception as e:
        userid=None
        self.content_from_file("rewardsoffline.html")
        print(traceback.format_exc())
        self.set_header_with_path("mynav.html")
        sql="select *, (select count(offers.id) from offers where offers.burger_id = burgers.id) as countoffers from burgers where countoffers > 0"
      self.set_footer_with_path("footer.html")
    except Exception as e:
      self.__class__ = erreur
      self.set_erreur(str(e))
      self.set_title("/rewards/list")
      print(traceback.format_exc())
      self.set_erreur(str(traceback.format_exc()))
      self.set_title("Erreur route home: "+str(e))

