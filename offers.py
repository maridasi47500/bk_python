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
      except:
        userid=None
    except Exception as e:
      self.__class__ = erreur
      self.set_erreur(str(e))
      self.set_title("/rewards/offers")

