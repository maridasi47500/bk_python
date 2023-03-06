global refreshmyorders
import directory
def refreshmyorders(query_components):
    Program=directory("")
    sql_command = "select  orders.user_id as userid, burgers.name as itemname, orders.id as orderno, burgers.image as burgerimage, burgers.prix as burgerprice, (o.qty*burgers.prix) as price, o.qty as qte, orders.dateorder as dateorder from orders left join orderitems o on o.order_id = orders.id left join burgers on o.burger_id = burgers.burger_number where orders.user_id = %s"
    message_else="Commencez une nouvelle commande maintenant !"
    tablename="orders"
    mystr="okokokokok"
    mystr="<div id=\"mydiv\">"+display_collection(sql_command, (str(session.current_user[0])), "_order", message_else, tablename,"orderid","_orderid.html")+"</div>"
    try:
        Program.set_content(force_to_unicode(mystr))
        Program.set_mimetype("html")
        Program.set_layout(False)
        return Program
    except Exception as e:

        print("erreur",e)
    print("okokokok")