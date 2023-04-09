from directory import directory
class changeitempage(directory):
    def __init__(self,path,title,params):
        self.set_layout(False)
        self.path=path
        self.title=title
        
        try:
            myid=params["myid"][0]
        except:
            myid=""
        
        try:
            otherburgerid=params["burger"][0]
            if otherburgerid=="undefined":
                raise Exception("sorry burger id must be defined")

        except:
            otherburgerid=None
        burgerid=otherburgerid or params["id"][0]
        burgercatid=params["catid"][0]
        sqlvalues=(burgercatid,)
        try:
            taille=params["taille"][0]
            if taille=="mataille":
                raise Exception("sorry type mustnt be big small or medium")

        except:
            taille=""
        mytype="where burgercat_id = %s"
        try:
            type=params["type"][0]
            if type=="undefined":
                raise Exception("sorry type mustnt be unedefined")
            mytype=" where mytype = 'jr%ss'"
            sqlvalues=(type,)
        except:
            type=None
            
        sql_command = "select * from burgers where burger_number = %s" % (burgerid)
        tablename="burgers"
        message_else=""
        articlesel= self.display_collection(sql_command, (), "_articlesel", message_else, tablename).replace("mataille",taille)
        #
        
        sql_command = ("select * from burgers "+mytype) % sqlvalues
        tablename="burgers"
        message_else=""
        collectionstr= self.display_collection(sql_command, (), "_checkboxburger", message_else, tablename).replace("mataille",taille)
        form=self.get_file("changeitem.html").read() % (articlesel,collectionstr)
        self.set_content(form.format(myid=myid))
