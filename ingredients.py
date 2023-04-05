from directory import directory
class ingredientpage(directory):
    def __init__(self,path,title,params):
        self.path=path
        self.title=title
        try:
            id=params["id"][0]
        except:
            id=""
        try:
            catid=params["catid"][0]
        except:
            catid=""
        try:
            myid=params["myid"][0]
            print("myid")
        except:
            myid=""
        try:
            taille=params["taille"][0]
            if taille == "undefined":
                raise Exception("taille ne peut pas etre undefined".decode("utf-8"))
            print("myid")
        except:
            taille=""
        sql_command = ("select * from burgers where burger_number = %s") % (id,)
        tablename="burgers"
        message_else=""
        collectionstr= self.display_collection(sql_command, (), "_articlesel", message_else, tablename).decode('utf-8').replace("mataille",taille)

        try:
            cheese=params["cheese"][0]
        except:
            cheese=""
        try:
            bacon=params["bacon"][0]
        except:
            bacon=""            
        try:
            onion=params["onion"][0]
        except:
            onion=""   
        try:
            pickle=params["pickle"][0]
        except:
            pickle=""  
        try:
            tomato=params["tomato"][0]
        except:
            tomato=""   
        try:
            lettuce=params["lettuce"][0]
        except:
            lettuce=""   
        try:
            stacker=params["stacker"][0]
        except:
            stacker=""
        try:
            ketchup=params["ketchup"][0]
        except:
            ketchup=""
        try:
            mayo=params["mayo"][0]
        except:
            ketchup=""
        try:
            mustard=params["mustard"][0]
        except:
            mustard=""
        try:
            bbq=params["bbq"][0]
        except:
            bbq=""
        code=self.get_file("ingredients.html").read().format(cheese=cheese,myid=myid)
        self.set_content(collectionstr+code)
        self.set_layout(False)