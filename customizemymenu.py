from directory import directory
global customizemymenu
global splitparams
def splitparams(x):
    return x.split("=")
import sqlite3
connection = sqlite3.connect("mesburgers1.db")
# cursor
global crsr
crsr = connection.cursor()

class customizemymenupage(directory):
    def __init__(self,title,query_components):
        try:
            self.set_path("./showburger/custom")
            self.title=title
            print("customize my burger (=)")
            self.set_layout(False)
            self.set_mimetype("html")
            print("hllo")
            unefois=False
            erreurmsg="il n'a en a plus"
            code=""
            burgerid=query_components["burgerid"][0]
            print("burger jr ici=>")

            dataparams={"9":"burgerid=&burger=","7":"burger=burgerjr&jrsides=jrsides&jrdrinks=jrdrinks&jrtreats=toy&burgerid=","1":"burger1=sandwich&burger2=sandwich&drink1=small&drink2=small&side1=small&side2=small","2":"burger=burger","4":"burger=sideonly","5":"burger=drinkonly","6":"burger=sweet","8":"burgerid=&burger=&drink=&side="}
            burgercatid=None

            try:
                burgersize=query_components["burger"][1]
                burgercatid=crsr.execute("select * from burgercats where url like ?",(query_components["burger"][0],)).fetchall()[0][0]
            except:
                burgersize=None
                #burgercatid=None
            try:
                drinksize=query_components["drink"][-1]
            except:
                drinksize=None
            try:
                sidesize=query_components["drink"][-1]
            except:
                sidesize=None
            try:
                burger1=query_components["burger1"][0]
                burger2=query_components["burger2"][0]
                drink1=query_components["drink1"][0]
                drink2=query_components["drink2"][0]
                side1=query_components["side1"][0]
                side2=query_components["side2"][0]
                burgercatid="1"
            except: 
                burger1=None
                burger2=None
                drink1=None
                drink2=None
                side1=None
                side2=None
            try:
                jrsides=query_components["jrsides"][0]
                jrdrinks=query_components["jrdrinks"][0]
                jrtreats=query_components["jrtreats"][0]
                jrburgersize=query_components["burger"][-1]
                burgercatid="7"
            except:
                jrsides=None
                jrdrinks=None
                jrtreats=None
                #burgercatid=None            
            sql="select * from burgers where burger_number = ?"
            crsr.execute(sql,(burgerid,))
            burger=crsr.fetchall()[0]
            burgercatid=burger[7]
            print("burger jr yes========>",burgercatid,burger)
            if str(burgercatid) == "7":
                print("burger jr yeah========>")
                tablename="burgers" 
                erreurmsg=""
                sql="select * from burgers where burger_number = %s"
                values=(query_components["burgerid"][-1])
                param1="burger"
                code+=self.display_collection(sql,values,"/_"+param1,erreurmsg,tablename)

                tablename="burgers"
                sql="select * from burgers where mytype = '%s' limit 1"
                values=(query_components["jrsides"][0])
                param1="jrsides"
                code+=self.display_collection(sql,values,"/_"+param1,erreurmsg,tablename)
                #replace size with value
                tablename="burgers"
                sql="select * from burgers where mytype = '%s' limit 1"
                values=(query_components["jrdrinks"][0])
                param1="jrdrinks"
                code+=self.display_collection(sql,values,"/_"+param1,erreurmsg,tablename)
                #replace size with value
                tablename="burgers"
                sql="select * from burgers where burger_number = %s limit 1"
                values=(query_components["jrtreats"][0])
                param1="jrtreats.html"
                print(self.get_file("/_"+param1).read())
                code+=self.get_file("/_"+param1).read()
                #replace size with value
                unefois=True
            elif str(burgercatid) == "4":
                print("ok ")
                erreurmsg=""
                tablename="burgers"
                value="sideonly"
                sql="select * from burgers where burger_number = %s"
                values=(query_components["burgerid"][0])
                mataille=query_components["burger"][-1]
                if mataille =="value":
                    mataille=""
                code+=self.display_collection(sql,values,"/_"+value,erreurmsg,tablename).replace("mataille",mataille)
            elif str(burgercatid) in ["1"]:
                for param1 in ["burger1","burger2"]:
                    tablename="burgers"
                    sql="select * from burgers where burger_number = %s"
                    values=(burgerid)
                    code+=self.display_collection(sql,values,"/_"+param1,erreurmsg,tablename).replace("mataille",burger1)
                for param1 in ["side1","side2"]:
                    tablename="burgers"
                    sql="select * from burgers where burgercat_id = %s limit 1"
                    values=("4")
                    code+=self.display_collection(sql,values,"/_"+param1,erreurmsg,tablename).replace("mataille",side1)
                for param1 in ["drink1","drink2"]:
                    tablename="burgers"
                    sql="select * from burgers where burgercat_id = %s limit 1"
                    values=("5")
                    code+=self.display_collection(sql,values,"/_"+param1,erreurmsg,tablename).replace("mataille",drink1)
            elif str(burgercatid) in ["2","3"]:
                tablename="burgers"
                param1="burger"
                sql="select * from burgers where burger_number = %s"
                values=(burgerid)
                code+=self.display_collection(sql,values,"/_"+param1,erreurmsg,tablename)
                try:
                    drinksize=query_components["drink"][0]
                    sidesize=query_components["side"][0]
                    tablename="burgers"
                    value="drink"
                    values=("5",)
                    
                    try:
                        drinkid=query_components["drinkid"][0]
                        myid="and burger_number = %s "
                        values=values+(drinkid,)
                    except:
                        myid=""
                    sql="select * from burgers where burgercat_id = %s "+myid+"limit 1"
                    
                    code+=self.display_collection(sql,values,"/_"+value,erreurmsg,tablename).replace("mataille",drinksize)
                    tablename="burgers"
                    value="side"
                    values=("4",)
                    try:
                        sideid=query_components["sideid"][0]
                        myid="and burger_number = %s "
                        values=values+(sideid,)
                    except:
                        myid=""
                    sql="select * from burgers where burgercat_id = %s "+myid+"limit 1"

                    code+=self.display_collection(sql,values,"/_"+value,erreurmsg,tablename).replace("mataille",sidesize)
                except Exception as e:
                    print("no side no rink",e)
                    drinksize=False
                    sidesize=False
                
            elif str(burgercatid) in ["6"]:
                tablename="burgers"
                value="sweet"
                sql="select * from burgers where burger_number = %s"
                values=(burgerid)
                code+=self.display_collection(sql,values,"/_"+value,erreurmsg,tablename)
            elif str(burgercatid) in ["5"]:
                tablename="burgers"
                sql="select * from burgers where burger_number = %s limit 1"
                values=(burgerid,)
                param1="drinkonly"
                burgersize=query_components["burger"][-1]
                if burgersize=="value":
                    burgersize=""
                code+=self.display_collection(sql,values,"/_"+param1,erreurmsg,tablename).replace("mataille",burgersize)
                #replace size with value
            #elif str(burgercatid) in ["4"]:
            #    tablename="burgers"
            #    sql="select * from burgers where burgercat_id = %s limit 1"
            #    values=("4")
            #    code+=self.display_collection(sql,values,"/_"+param1,erreurmsg,tablename).replace("mataille",value)
                #replace size with value
            else:
                print("toutes les cles cond #1")
                erreurmsg=""
                tablename="burgers"
                value="sideonly"
                sql="select * from burgers where burger_number = %s"
                values=(query_components["burgerid"][0])
                mydic={'small':"small","medium":"medium","large":"large","value":""}
                code+=self.display_collection(sql,values,"/_"+value,erreurmsg,tablename).replace("mataille",mydic[query_components["burger"][-1]])


        except Exception as e:
            print("next params",e)
        self.set_content(self.force_to_unicode(code))
