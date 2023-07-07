


  myroutes = [("/customizemenu",customizemymenu),(
  r"\/rewards\/offers\/[0-9]+(\/)?",showofferfunc),(
  "/rewards/list",rewardsfunc),(
  "/rewards/offers",offersfunc),(
  "/searchrestaurant",searchrestaurantfunc),(
  "/findaddress",findaddressfunc),(
      "/infolocation",infolocation),(
  
  r"^/store-locator/address$",addressfunc),(
  r"^/store-locator/service-mode$",servicemode),(
  r"^/store-locator$",servicemode),(
  
  "/listlocation",listlocation),(
  "/updateitem/customize",ingredients),(
  "/updateitem/changeitem",changeitem),(
  
  r"/menu(/)([0-9]+)(/)?", showburger),(
  r"/menu(/)([a-z]+)(/)?", showmenu),(
  r"/menu(/)?([a-z]+)?(/)?", showmenu),(
  "/orders/refresh",refreshmyorders),(
  "/account/orders",myorders),(
  "^/redeem(/.*)?$",code),(
  "\/redeem[\/]+",code),(
  "/account/payment",accountpayment),(
  "/account/payment/add-card",addcard),(
  "/account/payment/add-gift-card",addgiftcard),(
  "/signinuser", signinuser),(
  r"^\/$",homefunc),(
  "/signin",signin),(
              "/signup", signup),(
              #"/rewards/offers", offersfunc),(
              #"/rewards/list", rewardsfunc),(
  '/account/info', myaccountinfo),(
  '/confirm-otp', confirmotp),(
  "/confirm-jwt", confirmjwt),(
  "/setcookie", setcookie),(
  
  '/confirm-jwt', confirmjwt)
  ]
  route_post=[(
  r"\/rewards\/offers\/[0-9]+(\/)?",savetoredeemfunc),(
  
      "/orderlocation",orderlocation),(
      "/offerslocation",offerslocation),(
      "/favlocation",favlocation),(
      "/bkaction",bkaction),(
      "/addburger",addburger),(
      "/savegiftcard", savegiftcard),(
      "/savepayment", savepayment),(
      "/signup", signup_user),(
      "/signin", signmein),(
      "/saveinfo", savemyinfo),(
      "/aftersignup", aftersignup),(
      "/confirm-otp", confirmotp),(
      "/checkemail", checkemail),(
      "/checkuser.json", checkuser),(
      "/validatecode", validatecode
  ]
