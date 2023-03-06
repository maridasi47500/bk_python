function on() {
  document.getElementById("overlayburger").style.display = "block";
}

function off() {
  document.getElementById("overlayburger").style.display = "none";
}

function onburger() {
  document.getElementById("customizeburger").style.display = "block";
}

function offburger() {
  document.getElementById("customizeburger").style.display = "none";
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