import directory
global customizemymenu
global pagedisplaythisburger
class pagedisplaythisburger(directory)
    def __init__(self,title):
        self.title=title
    def __init__(self,title,burger,catid,catname):
        self.title=title
        text="<a href=\"/menu/"+repr(catid)+"\">retour au menu "+catname+"</a>"
        text+=mycard(burger[1],str(burger[4])+"€","min "+str(burger[5])+" cal")
        self.content=text

