# -*- coding: utf-8 -*-

from directory import directory
import math
import re
import sqlite3
import urllib, json

global url

from redirect import redirectaction
connection = sqlite3.connect("mesburgers1.db")
connection.create_function('sqrt', 1, math.sqrt)
connection.create_function('cos', 1, math.cos)
connection.create_function('pow', 2, math.pow)
global crsr
crsr = connection.cursor()
import os
path1=os.getcwd()
class listlocationpage(directory):
    def __init__(self,params):
        print("listthislocation")
        self.path="./store-locator"
        self.current_order=[]
        self.layout=False
        self.header=""
        self.footer=""
        try:
          param=params["mylist"][0]
          print(param)
          address=params["address"][0]
          userid=params["userid"][0]
        except:
          print("erreeeeur params")
        #voulez vous me partager lon/lat?
        #favorite recents or nearby?
        #à proximité , favoris puis recents
        collectionstr="" 
        if param == "nearby":
          try:
            url = "https://nominatim.openstreetmap.org/?addressdetails=1&format=json&limit=1&q="+address.replace(" ","+")
            response = urllib.urlopen(url)
            data = json.loads(response.read())[0]
            print(data)
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
            print("resultats longuur",len(res))
            tablename="bks"
            message_else=""
            collectionstr= self.display_collection(sql_command.format(startlat=lat,startlng=lon,userid=userid), (), "nearby", message_else, tablename,False,False,("myfavs",))
          except Exception as e:
            print("print error:",e)
            collectionstr=""
        elif param == "favorite":
          sql_command = "select * from bks left join favs on favs.bk_id = bks.id group by bks.id having bk.user_id in (?)"
          tablename="bks"
          message_else=""
          collectionstr= self.display_collection(sql_command, (), "favorite", message_else, tablename)
        try:
          g=self.get_file_with_path("list.html").read()
          self.set_content((g % collectionstr).replace("(userid)",str(userid)))
        except Exception as e:
          print(e,"eERREUR")
