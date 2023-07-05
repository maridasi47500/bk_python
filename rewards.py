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
        sql="select * from burgers where mytype = 'rewards'"
        userid=params["userid"][0]
        self.set_header_with_path_and_address("headersignedin.html",userid)

      except Exception as e:
        userid=None
        self.content_from_file("rewardsoffline.html")
      self.set_footer_with_path("footer.html")
      tablename="burgers"
      message_else="Aucune récompense n'est disponible."
      myarg=()

      collectionstr= self.display_collection(sql, myarg, "_recompense", message_else, tablename)
      self.content_from_file_yield("myrewardshtml.html",collectionstr)

    except Exception as e:
      self.__class__ = erreur
      self.set_erreur(str(e))
      self.set_title("/rewards/list")
      print(traceback.format_exc())
      self.set_erreur(str(traceback.format_exc()))
      self.set_title("Erreur route home: "+str(e))

