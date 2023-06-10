# coding=utf-8
import sqlite3
from directory import directory
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()

class mynewaddresspage(directory):
  def __init__(self,path,params):
    self.set_path(path)
    self.title=title
    self.params=title
    try:
      userid=params["userid"][0]
    else:
      userid=None
