from directory import directory
from redirect import redirectaction
class offerslocationpage(redirectaction):
  def __init__(self,title,param):
    self.param=param
    self.path="/"
    try:
      id=param["id"][0]
    except:
      id=None
    try:
      userid=param["userid"][0]
    except:
      userid=None
    self.mysql("update users set restaurant_id = ? where user_number = ?", (id,userid))
    self.redirect="/orders"


