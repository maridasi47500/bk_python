import directory
global customizemymenu
def customizemymenu(query_components):
    try:
        Program=directory('burger king') 
        print("customize my burger (=)")
        Program.set_layout(False)
        Program.set_mimetype("html")
        print("hllo")
	unefois=False

        code=""
        burgerid=query_components["burgerid"][0]
	print("burger jr ici=>")
        Program.set_path("./mespages/custom")
        dataparams={"7":"burger=burgerjr&jrsides=jrsides&jrdrinks=jrdrinks&jrtreats=toy&burgerid=","1":"burger1=sandwich&burger2=sandwich&drink1=small&drink2=small&side1=small&side2=small","2":"burger=burger","4":"burger=sideonly","5":"burger=drinkonly","6":"burger=sweet","8":"burgerid=&burger=&drink=&side=","9":"burgerid=&burger="}
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
	    code+=display_collection(sql,values,"/custom/_"+param1,erreurmsg,tablename)
	    
	    tablename="burgers"
	    sql="select * from burgers where mytype = '%s' limit 1"
	    values=(query_components["jrsides"][0])
	    param1="jrsides"
	    code+=display_collection(sql,values,"custom/_"+param1,erreurmsg,tablename)
	    #replace size with value
	    tablename="burgers"
	    sql="select * from burgers where mytype = '%s' limit 1"
	    values=(query_components["jrdrinks"][0])
	    param1="jrdrinks"
	    code+=display_collection(sql,values,"custom/_"+param1,erreurmsg,tablename)
	    #replace size with value
	    tablename="burgers"
	    sql="select * from burgers where burger_number = %s limit 1"
	    values=(query_components["jrtreats"][0])
	    param1="jrtreats.html"
	    code+=get_file("custom/_"+param1).read()
	    #replace size with value
	    unefois=True
        if unefois == False:
            for myvalues in dataparams.values():
                if unefois==True:
	    	    break
                othervalues=map(splitparams,myvalues.split("&"))
                try:
	    	    if unefois == True:
	    	        break		
                    print(othervalues)
                    print(all(query_components.get(item[0])[0] == item[1] for item in othervalues))
                    #si toutes les cles sont la (sans les valeurs)
                    #si toutes les cles et vlauers egales
                    if all( len(query_components[item[0]][0]) > 0 for item in othervalues):
	    	        if unefois == True:
	    	            break		
                        #sitouteslesclessontpresentes
                        print(query_components)
                        print("si toutes les cles sont presentes")  
                        print("firstcond")
                        print(all(dic in ["burger","burgerid"] for dic in query_components.keys()))
                        print(all( item[0] in ["burger","jrsides","jrdrinks","jrtreats","burgerid"] for item in othervalues))

                        print("#2 cond",any(query_components[dic][-1] in ["small","medium","large","value"] for dic in query_components))

	    	    if all( item[0] in ["side","drink","burger","burgerid"] for item in othervalues):
                            print("ok ")
                            erreurmsg=""
                            tablename="burgers"
                            value="burger"
                            sql="select * from burgers where burger_number = %s"
                            values=(query_components["burgerid"][0])
                            code+=display_collection(sql,values,"/custom/_"+value,erreurmsg,tablename)
                            tablename="burgers"
                            sql="select * from burgers where burgercat_id = 4 limit 1"
                            values=()
                            value="sideavecdrink"
                            code+=display_collection(sql,values,"/custom/_"+value,erreurmsg,tablename).replace("mataille",query_components["side"][0])
                            tablename="burgers"
                            sql="select * from burgers where burgercat_id = 5 limit 1"
                            values=()
                            value="drinkavecside"
                            code+=display_collection(sql,values,"/custom/_"+value,erreurmsg,tablename).replace("mataille",query_components["drink"][0])
                            break
	    	    if all( dic in ["burger","burgerid"] for dic in query_components.keys()) & any(query_components[dic][-1] in ["small","medium","large","value"] for dic in query_components):
                            print("toutes les cles cond #1")
                            erreurmsg=""
                            tablename="burgers"
                            value="sideonly"
                            sql="select * from burgers where burger_number = %s"
                            values=(query_components["burgerid"][0])
                            mydic={'small':"small","medium":"medium","large":"large","value":""}
                            code+=display_collection(sql,values,"/custom/_"+value,erreurmsg,tablename).replace("mataille",mydic[query_components["burger"][-1]])
                            break
	    	    if unefois == True:
	    	        break		

                    if all( query_components[item[0]][0] == item[1] for item in othervalues):
                        try:

                            for param1, value in othervalues:
                                print("hello")
                                Program.set_path("./mespages/custom")
                                erreurmsg=""
                                if value in ["burger","sandwich"]:
                                    tablename="burgers"
                                    sql="select * from burgers where burger_number = %s"
                                    values=(burgerid)
                                    code+=display_collection(sql,values,"/custom/_"+param1,erreurmsg,tablename)
                                elif value in ["sweet","sideonly","drinkonly"]:
                                    tablename="burgers"
                                    sql="select * from burgers where burger_number = %s"
                                    values=(burgerid)
                                    code+=display_collection(sql,values,"/custom/_"+value,erreurmsg,tablename)
                                elif param1 in ["drink","drink1","drink2"]:
                                    tablename="burgers"
                                    sql="select * from burgers where burgercat_id = %s limit 1"
                                    values=("5")
                                    code+=display_collection(sql,values,"custom/_"+param1,erreurmsg,tablename).replace("mataille",value)
                                    #replace size with value
                                elif param1 in ["side1","side2","side"]:
                                    tablename="burgers"
                                    sql="select * from burgers where burgercat_id = %s limit 1"
                                    values=("4")
                                    code+=display_collection(sql,values,"custom/_"+param1,erreurmsg,tablename).replace("mataille",value)
                                    #replace size with value

                        except Exception as e:
                            print("erreur azertyu",e)
                except Exception as e:
                    print("next params",e)
        Program.set_content(force_to_unicode(code))
        return Program
    except Exception as e:
        print("my errooor (=)",e)