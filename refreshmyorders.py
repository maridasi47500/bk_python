global refreshmyorders
from directory import directory
class refreshmyorderspage(directory):
    def __init__(self,title):
        self.title=title
        try:

            sql_command = "select  orders.user_id as userid, burgers.name as itemname, orders.id as orderno, burgers.image as burgerimage, burgers.prix as burgerprice, (o.qty*burgers.prix) as price, o.qty as qte, orders.dateorder as dateorder from orders left join orderitems o on o.order_id = orders.id left join burgers on o.burger_id = burgers.burger_number where orders.user_id = %s"
            message_else="Commencez une nouvelle commande maintenant !"
            tablename="orders"
            mystr="okokokokok"
            mystr="<div id=\"mydiv\">"+self.display_collection(sql_command, (str(session.current_user[0])), "_order", message_else, tablename,"orderid","_orderid.html")+"</div>"

            self.set_content(force_to_unicode(mystr))
            self.set_mimetype("html")
            self.set_layout(False)

        except Exception as e:

            print("erreur",e)
        print("okokokok")
