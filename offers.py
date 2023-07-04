# coding=utf-8
import sqlite3
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
from erreur import erreur

class offerspage(directory):
  def __init__(self,path,title,params):
    try:
      self.set_path(path)
      self.content_from_file("myoffershtml.html")
      self.title=title
      self.params=title

      try:
        userid=params["userid"][0]
        self.set_header_with_path_and_address("headersignedin.html",userid)
      except:
        userid=None
        self.set_header_with_path("mynav.html")
      self.set_footer_with_path("footer.html")
    except Exception as e:
      self.__class__ = erreur
      self.set_erreur(str(e))
      self.set_title("/rewards/offers")

