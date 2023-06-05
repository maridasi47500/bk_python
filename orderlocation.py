from directory import directory
from redirect import redirectaction
class orderlocationpage(redirectaction):
  def __init__(self,title,param):
    self.param=param
    self.path="/"
    try:
      userid=param["userid"][0]
    except:
      userid=None
    self.mysql("update users set restaurant_id = ?", (userid))
    self.redirect="/orders"

