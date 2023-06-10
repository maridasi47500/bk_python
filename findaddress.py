# coding=utf-8
import sqlite3
from directory import directory
import urllib, json

global url


connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()

class findaddresspage(directory):
  def __init__(self,path,params):
    try:
      address=params["address"][0]
    else:
      address=""
    url = "https://nominatim.openstreetmap.org/?addressdetails=1&format=json&limit=1&q="+address.replace(" ","+")
    response = urllib.urlopen(url)
    data = json.loads(response.read())[0]
    print(data)
    lat=data['lat']
    lon=data['lon']

    self.set_path(path)
    self.title=title
    self.params=title
    try:
      userid=params["userid"][0]
    else:
      userid=None
