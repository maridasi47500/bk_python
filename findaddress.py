# coding=utf-8
import sqlite3
from directory import directory
from jsoncontent import jsoncontent
import urllib, json

global url


connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()

class findaddresspage(jsoncontent):
  def __init__(self,path,title,params):
    self.set_path(path)
    try:
      address=params["address"][0]
    except:
      address=""
    self.title=title
    self.content_from_file("myhtml.html")
    self.content=self.content.decode('utf-8')
    print(self.mimetype,"mimeype")
    print("content",self.content)
    try:
      print("essayer d'avoir la lat :")
      url = "https://nominatim.openstreetmap.org/?addressdetails=1&format=json&limit=1&q="+address.replace(" ","+")
      response = urllib.urlopen(url)
      data = json.loads(response.read())[0]
      print(data)
      lat=data['lat']
      lon=data['lon']
      self.set_json({"lat": lat, "lon": lon})
    except Exception as e:
      self.set_json({"quelquesoit le json envoyé":"résultat"})
      print("râté", e)

    self.title=title
    self.params=title
    try:
      userid=params["userid"][0]
    except:
      userid=None
