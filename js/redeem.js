function addredeem() {
  // Get the snackbar DIV
  var x = document.getElementById("add_redeem");

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}
function myFunction1() {
  // Get the snackbar DIV
  var x = document.getElementById("remove_redeem");

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}
window.onload=function(){
addredeem();
}
