# coding=utf-8
import sqlite3
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
from erreur import erreur
import traceback

class savetoredeempage(directory):
  def __init__(self,path,title,params):
    try:
      self.set_path(path)
      self.content_from_file("mysavetoredeemhtml.html")
      self.title=title
      self.params=title
      try:
        userid=params["userid"][0]
      except:
        userid=None
    except Exception as e:
      self.__class__ = erreur
      print(traceback.format_exc())
      self.set_erreur(str(traceback.format_exc()))
      self.set_title("Erreur route \"/savetoredeem\": "+str(e))

