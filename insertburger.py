global insertburger
import directory
def insertburger(query_components):
    if query_components.get("burgername"):
        Program=directory("bk")
        data_string = query_components["burgername"][0]
        sql_command = """INSERT INTO burgers (name) VALUES ('""" + data_string + """');"""
        print("ok ok")
        crsr.execute(sql_command)
        connection.commit()
        try:
            print("jom")
            crsr.execute("SELECT * FROM burgers")
            mycontent="<main><ul>"
            # store all the fetched data in the ans variable
            ans = crsr.fetchall()

            for myburger,name1,image1,description1,prix1 in ans:
                mycontent+= "<li>"+name1+"</li>"
            mycontent+="</ul></main>"
            #print(mycontent)
            #Program.path("./")
            print("ok")
            print("yeah")
            Program.set_content(mycontent)
            return render_figure("index.html")
        except Exception as e:
            print("erreur",e)
        print("okokokok")
        #connection.commit()
