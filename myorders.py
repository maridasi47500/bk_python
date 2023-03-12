from directory import directory
global myorders
class myorderspage(directory):
    def __init__(self,title):
        sql_command = "select orders.user_id as userid, burgers.name as itemname, orders.id as orderno, burgers.image as burgerimage, burgers.prix as burgerprice, (o.qty*burgers.prix) as price, o.qty as qte, orders.dateorder as dateorder from orders left join orderitems o on o.order_id = orders.id left join burgers on o.burger_id = burgers.burger_number where orders.user_id = %s"
        message_else="Commencez une nouvelle commande maintenant !"
        tablename="orders"

        mystr="<div id=\"mydiv\">"+self.display_collection(sql_command, (str(session.current_user[0])), "_order", message_else, tablename,"orderid","_orderid")+"</div>"
        try:
            self.add_js("orders.js")
            self.add_css("orders.css")
            self.set_path("./mespages")
            k=get_file("orders.html")
            text=force_to_unicode(k.read())
            text=text.replace("les commandes apparaissent ici",mystr)

            self.set_content(text)

        except Exception as e:

            print("erreur",e)
        print("okokokok")
