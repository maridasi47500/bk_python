global savegiftcard
from directory import directory
class savegiftcardpage(directory):
    def __init__(self,title,query_components):
        print("save gift card",query_components["numero"])
        if query_components.get("numero"):
            numero=query_components.get("numero")[0]
            sql="select * from giftcards where numero = '%s'" % (numero)
            crsr.execute(sql)
            connection.commit()
            data=crsr.fetchall()
            if len(data) > 0:
                card=data[0]
                cardid=card[0]
                userid=session.current_user[0]
                sql="update giftcards set user_id = '%s' where id = %s" % (userid,cardid)
                crsr.execute(sql)
                connection.commit()
                self.set_json({"ok":"1"})
            else:
                card=None
                self.set_json({"ok":"0"})
            print("save giftcard")
            self.set_mimetype("json")
