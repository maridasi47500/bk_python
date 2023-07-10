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
      print("REDEEM FUNC",params)
      self.set_path(path)
      self.content_from_file("mysavetoredeemhtml.html")
      self.title=title
      self.params=title
      try:
        burgerid=params["burgerid"][0]
      except:
        burgerid=None
      try:
        userid=params["userid"][0]
      except:
        userid=None
      self.mysql("insert into myoffers (user_id, burger_id) values (?,?)", (userid,burgerid))
    except Exception as e:
      self.__class__ = erreur
      print(traceback.format_exc())
      self.set_erreur(str(traceback.format_exc()))
      self.set_title("Erreur route \"/savetoredeem\": "+str(e))

