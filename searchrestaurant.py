# coding=utf-8
import sqlite3
from erreur import erreur
from directory import directory
from jsoncontent import jsoncontent
import math
import re
import sqlite3
import urllib, json

connection = sqlite3.connect("mesburgers1.db")
connection.create_function('sqrt', 1, math.sqrt)
connection.create_function('cos', 1, math.cos)
connection.create_function('pow', 2, math.pow)

# cursor
global crsr
crsr = connection.cursor()

class searchrestaurantpage(jsoncontent):
  def __init__(self,path,title,params):
    try:
      listparams=("userid","lat","lon")
      for p in listparams:
          exec("try:\n {val}=params['{val}'][0]\nexcept:\n  {val}=None".format(val=p))
      self.set_path(path)
      self.set_json({"dujson":"resultat"})
      self.content_from_file("mysearchrestauranthtml.html")
      self.title=title
      self.params=title
      durees={}
      start = '%s,%s' % (lon,lat)
      sql_command = """SELECT * from bks GROUP BY bks.id HAVING SQRT( POW(69.1 * (lat - {startlat}), 2) + POW(69.1 * ({startlng} - lon) * COS(lat / 57.3), 2)) < 100 ORDER BY SQRT( POW(69.1 * (lat - {startlat}), 2) + POW(69.1 * ({startlng} - lon) * COS(lat / 57.3), 2)) desc;"""
      crsr.execute(sql_command.format(startlat=lat,startlng=lon))
      connection.commit()
      res=crsr.fetchall()
      print("resultat",res)
      for r in res:
          myid=self.searchattribute(r,"bks","id")
          mylat=self.searchattribute(r,"bks","lat")
          mylon=self.searchattribute(r,"bks","lon")
          stop = '%s,%s' % (mylon,mylat)
          #url = 'http://router.project-osrm.org/viaroute?loc=' + start + '&loc=' + stop
          url = 'http://router.project-osrm.org/route/v1/driving/'+start+';'+stop+'?overview=false'
          print(url)
          response = urllib.urlopen(url)
          data = json.loads(response.read())
          print("==DATA route==")

          duree=data["routes"][0]["duration"]
          print(data,duree)
          durees[str(myid)]=duree
          print(durees)
      minvalue=min(durees)
      print(minvalue)
      crsr.execute("update users set restaurant_id = ? where user_number = ?",(minvalue,userid))
      connection.commit()
      self.set_json({"restaurant_livraison_id":minvalue,"restauranttrouve":"1"})
    except Exception as e:
      print(e)
      self.__class__ = erreur
      self.set_erreur(str(e))
      self.set_title("/searchrestaurant")
      self.set_json({"erreur":str(e),"restaurant_livraison_id":None,"restauranttrouve":"0"})


