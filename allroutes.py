class routes(object):
  mots={  "/favlocation":{"partiedemesmots":"favlocation"},      r"\/rewards\/offers\/[0-9]+(\/)?":{"partiedemesmots":"showoffer"},      "/rewards/list":{"partiedemesmots":"rewards"},      "/rewards/offers":{"partiedemesmots":"offers"},      "/searchrestaurant":{"partiedemesmots":"searchrestaurant"},  "/findaddress":{"partiedemesmots":"findaddress"},  "/offerslocation":{"partiedemesmots":"offerslocation"},"/orderlocation":{"partiedemesmots":"orderlocation"},"/infolocation":{"partiedemesmots":"infolocation"},"/bkaction":{"partiedemesmots":"id"},"/listlocation":{"partiedemesmots":"listlocation"},  "^/redeem(/.*)?$":{"partiedemesmots":"royalprk"},  "\/redeem[\/]+":{"partiedemesmots":"royalprk"},  r"^/store-locator/service-mode$":{"partiedemesmots":"Emplacements"},r"^/store-locator/address$":{"partiedemesmots":"Entrez votre adresse"},r"^/store-locator$":{"partiedemesmots":"Emplacements"},"/account/info":{"partiedemesmots":"Account"},"/confirm-jwt":{"partiedemesmots":""},"/updateitem/changeitem":{"partiedemesmots":"burger"},"/updateitem/customize":{"partiedemesmots":"bacon"},"/customizemenu":{"partiedemesmots":"burger"},   r"/menu(/)([0-9]+)(/)?": {"partiedemesmots":"Personnaliser votre commande"}, r"/menu(/)([a-z]+)(/)?": {"partiedemesmots":"Hamburgers grillés à la flamme"}, r"/menu(/)?([a-z]+)?(/)?": {"partiedemesmots":"Hamburgers grillés à la flamme"},"/menu(/)?":{"partiedemesmots":"Hamburgers grillés à la flamme"},"^\/$":{"partiedemesmots":"Get rewarded like Royalty"},"/signin":{"partiedemesmots":"sign-in-form\""},"/signup":{"partiedemesmots":"J'accepte ce qui suit : Politique de confidentialité Conditions d'utilisation des récompenses Conditions d'utilisation"}}
  def __init__(self):
    self.routes=[
    ]
  def get_routes(self):
    return self.routes



  myroutes = {"/customizemenu":customizemymenu,
  r"\/rewards\/offers\/[0-9]+(\/)?":showofferfunc,
  "/rewards/list":rewardsfunc,
  "/rewards/offers":offersfunc,
  "/searchrestaurant":searchrestaurantfunc,
  "/findaddress":findaddressfunc,
      "/infolocation":infolocation,
  
  r"^/store-locator/address$":addressfunc,
  r"^/store-locator/service-mode$":servicemode,
  r"^/store-locator$":servicemode,
  
  "/listlocation":listlocation,
  "/updateitem/customize":ingredients,
  "/updateitem/changeitem":changeitem,
  
  r"/menu(/)([0-9]+)(/)?": showburger,
  r"/menu(/)([a-z]+)(/)?": showmenu,
  r"/menu(/)?([a-z]+)?(/)?": showmenu,
  "/orders/refresh":refreshmyorders,
  "/account/orders":myorders,
  "^/redeem(/.*)?$":code,
  "\/redeem[\/]+":code,
  "/account/payment":accountpayment,
  "/account/payment/add-card":addcard,
  "/account/payment/add-gift-card":addgiftcard,
  "/signinuser": signinuser,
  r"^\/$":homefunc,
  "/signin":signin,
              "/signup": signup,
              #"/rewards/offers": offersfunc,
              #"/rewards/list": rewardsfunc,
  '/account/info': myaccountinfo,
  '/confirm-otp': confirmotp,
  "/confirm-jwt": confirmjwt,
  "/setcookie": setcookie,
  
  '/confirm-jwt': confirmjwt
  }
  global menu
  # POST routes
  route_post={
  r"\/rewards\/offers\/[0-9]+(\/)?":savetoredeemfunc,
  
      "/orderlocation":orderlocation,
      "/offerslocation":offerslocation,
      "/favlocation":favlocation,
      "/bkaction":bkaction,
      "/addburger":addburger,
      "/savegiftcard": savegiftcard,
      "/savepayment": savepayment,
      "/signup": signup_user,
      "/signin": signmein,
      "/saveinfo": savemyinfo,
      "/aftersignup": aftersignup,
      "/confirm-otp": confirmotp,
      "/checkemail": checkemail,
      "/checkuser.json": checkuser,
      "/validatecode": validatecode
  }
