# coding=utf-8
import sqlite3
from directory import directory
from jsoncontent import jsoncontent
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()

class searchrestaurantpage(jsoncontent):
  def __init__(self,path,title,params):
    self.set_path(path)
    self.set_json({"dujson":"resultat"})
    self.content_from_file("mysearchrestauranthtml.html")
    self.title=title
    self.params=title
    try:
      userid=params["userid"][0]
    except:
      userid=None
    lat=data['lat']
    lon=data['lon']
    sql_command = """SELECT *, (case when (select count(favbks.id) from favbks where favbks.bk_id = bks.id and favbks.user_id = {userid}) > 0 then 1 else 0 end) as myfavs from bks GROUP BY bks.id HAVING SQRT( POW(69.1 * (lat - {startlat}), 2) + POW(69.1 * ({startlng} - lon) * COS(lat / 57.3), 2)) < 100 ;"""
    sql_command2 = """SELECT id,address, sqrt( pow((69.1 * (lat - {startlat})), 2) + pow((69.1 * ({startlng} - lon) * cos(lat / 57.3)), 2)) AS distance FROM bks GROUP BY bks.id ORDER BY distance;"""
    crsr.execute(sql_command2.format(startlat=lat,startlng=lon))
    connection.commit()
    res=crsr.fetchall()
    print("resultat",res)
    sql_command2 = """SELECT * from bks"""
    crsr.execute(sql_command2)
    connection.commit()
    res=crsr.fetchall()

