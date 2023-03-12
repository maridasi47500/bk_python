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
// Get the modal
var modal = document.getElementById("customizemenuburger");

// Get the button that opens the modal
var btn = document.getElementById("burgermenuBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("closeburgermenu")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
} 
