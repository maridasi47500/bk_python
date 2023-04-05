function makeid(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    var counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return result;
}
function clickmeal(evt){
        onmenuburger();
        var url, myburger,myid;
        myburger=evt.target;
        while ((typeof $(myburger).data("id") === "undefined")) {
            myburger=myburger.parentElement;
        }
            console.log($(myburger).data("customize"),$(myburger).data("select"))
        if ($(myburger).data("customize") || $(myburger).data("select")) {
            sometextmenuburger.innerHTML="";
                
            myid=makeid(5);
            $(myburger)[0].dataset.myid=myid;
            alert($(myburger).data("myid"))
            if ($(myburger).data("select")) {    
        $.ajax({url:"/updateitem/changeitem?id="+$(myburger).data("id")+"&catid="+$(myburger).data("catid")+"&taille="+String($(myburger).data("taille"))+"&type="+String($(myburger).data("type"))+"&myid="+String(myid),
        success:function(data){
                console.log(data);
            sometextmenuburger.innerHTML += data;
        }
        });
        }
            if ($(myburger).data("customize")) {    
        $.ajax({url:"/updateitem/customize?id="+$(myburger).data("id")+"&catid="+$(myburger).data("catid")+"&taille="+String($(myburger).data("taille"))+"&myid="+String(myid)+"&type="+String($(myburger).data("type")),
        success:function(data){
            console.log(data);
            sometextmenuburger.innerHTML += data;
        }
        });
        }
    }   
        
        
    };