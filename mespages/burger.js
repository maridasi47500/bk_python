function on() {
  document.getElementById("overlayburger").style.display = "block";
}
function toTitleCase(str) {
  return str.replace(
    /\w\S*/g,
    function(txt) {
      return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    }
  );
}
function off() {
  document.getElementById("overlayburger").style.display = "none";
}
function resetform(){
    var myform=$(".ingredients-form")[0];
    var mydivs=$("[value=\"No\"]");
    for (var i=0;i<mydivs.length;i++) {
        $(mydivs[i]).val("no")
    }
    myform.reset();
    $("#dispoptions").html("");
}
function displayart(myinput = null){
    if (myinput && !myinput.checked && myinput.previousSibling.type==="hidden"){
        myinput.previousSibling.value="No";
    }else if (myinput && !myinput.checked && myinput.previousSibling.previousSibling.type==="hidden"){
        myinput.previousSibling.previousSibling.value="No";
    }else if (myinput && myinput.checked && myinput.previousSibling.type==="hidden"){
        myinput.previousSibling.value="no";
    }else if (myinput && myinput.checked && myinput.previousSibling.previousSibling.type==="hidden"){
        myinput.previousSibling.previousSibling.value="no";
    } else if (myinput && myinput.children[0] && myinput.children[0].value==="no"){
        myinput.children[0].value="No";
    }
    var mydiv=$(".ingredients-form")[0];
    if (mydiv){
            var url=$(mydiv).serialize(),param,val,size,price;
            var lstopt=url.split("&");
                $(mydiv).data("options",url)
                var childr=$("#dispoptions")[0],dispoptions=false;
            
            var count=[];
            var mystr="";
            for (var y=0;y<lstopt.length;y++){
                param=lstopt[y].split("=")[0];
               val=lstopt[y].split("=")[1];
                console.log(param,val);
               if (val !=="no"){
               size=val.split("-")[0].replace("%20"," ");
               if (size =="on") {
                   size="Add";
               }
               mystr+="<p>";
               mystr+=size;
               try{
                   price=parseFloat(val.split('-')[1]);
                   if (NaN(price)) {
                       throw new Error("price is not a number")
                   }
               }
               catch(e) {
                   price="";
                   console.log(e);
               }
               
               
               if (!isNaN(parseFloat(val))){
                   count.push(val);
               }
               switch(param){
                   case "tomato":
                        mystr+=" tomate";
                        break;
                   case "lettuce":
                       console.log("hheese",val)
                       mystr+=" laitue";
                       break;
                   case "onions":
                       console.log("hheese",val)
                       mystr+=" oignons caramélisés";
                       break;
                   case "bacon":
                   case "cheese":
                   case "pickle":
                   case "ketchup":
                   case "mayo":
                   case "mustard":
                        mystr+=" "+param;
                        break;
                   case "stacker":
                        mystr+=" sauce stacker"
                        break;
                   case "bbq":
                       mystr+=" sauce barbecue";
                       console.log("hheese",val);
                       break;
                   case "biscuit":
                       mystr+=" whopper jr party";
                       console.log("hheese",val);
                       break;
                   default:
                       console.log("hheese",val);
                       break;
               }
               if (price !== "") {
               mystr+=" "+String(price)+"€</p>";
                }
            
            }
        }
            $("#dispoptions").html(toTitleCase(mystr));
            }
            }
function onburger() {
  document.getElementById("customizeburger").style.display = "block";
}

function offburger() {
  document.getElementById("customizeburger").style.display = "none";
}
function onmenuburger() {
    displayart();
  document.getElementById("customizemenuburger").style.display = "block";
}
function displayvalue(el){
    var article=document.getElementById("articlesel");
    $(article).children("img").attr("src", $(el.parentElement).children("img").attr("src"))
    $(article).data("id", $(el).val());
    $(article).children("b").html($(el.parentElement).children("b").html())
    $(article).children("span").html($(el.parentElement).children("span").html())
}
function offmenuburger(myform = "mymodal") {
     var mydata=$("[data-mydiv]").serialize();
     var mydivvalue=$("[data-mydiv]").data("mydiv");
     var myitem=$("[data-myid]");
     /*alert("kk")
alert(mydivvalue+"[data-myid=\""+mydivvalue+"\"] .dispoptions");
    */
    var myoptions=$("[data-myid=\""+mydivvalue+"\"] .dispoptions");
    if (myoptions[0]) { 
            myitem[0].dataset.mydata=mydata;
          myoptions.html($("#dispoptions").html());
    }
    
    if (myform !== "mymodal") {
    var mydiv=$("[data-myid=\""+$(myform).data("mydiv")+"\"]");

      if (myform === $(".ingredients-form")[0]) {
  } else if (myform === $(".edititem-form")[0]) {
        }
  }
  document.getElementById("customizemenuburger").style.display = "none";
}
window.onload=function(){
  $.ajax({
    url:"/customizemenu?"+myparams.innerHTML,
    success:function(data){
      personnaliser_commande.innerHTML=data;
    }
  });
};
function loadburger(params){
  $.ajax({
    url:"/customizemenu?"+params,
    success:function(data){
      personnaliser_commande.innerHTML=data;
    }
  });
  return false;
  }
// Get the modal
var modal = document.getElementById("customizemenuburger");

// Get the button that opens the modal
var btn = document.getElementById("burgermenuBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("closeburgermenu")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  //modal.style.display = "block";
  onmenuburger();
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  //modal.style.display = "none";
  offmenuburger();
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    //modal.style.display = "none";
    offmenuburger();
  }
} 
