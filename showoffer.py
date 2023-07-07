# coding=utf-8
import sqlite3
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()
from erreur import erreur
import traceback

class showofferpage(directory):
  def __init__(self,path,title,params):
    try:
      self.set_path(path)
      burgerid=params["path"][0].split("/")
      if len(burgerid) > 0:
        burgerid=burgerid[(len(burgerid) - 1)]
      sql="select b.*, b.name,b.image,b.prix,b.mincal,b.maxcal,(select count(offers.id) as mycountoffer from offers where offers.burger_id = ? and offers.burger_id = b.burger_number) as nboffers from burgers b where nboffers > 0"
      myarg=(burgerid,)
      myparams=("nboffers")
      mytemplatenames=("",)
      self.set_footer_with_path("footer.html")
      tablename="burgers"
      message_else="Aucune offre n'est disponible."

      collectionstr= self.display_collection(sql, myarg, "_voiroffre", message_else, tablename,False,False,myparams,mytemplatenames)


      self.content_from_file_yield("myshowofferhtml.html",collectionstr)
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
      self.set_title("Erreur route \"/showoffer\": "+str(e))

