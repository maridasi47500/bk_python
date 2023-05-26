// Get the modal
window.onload=function(){
var modal = document.getElementById("myModalPolicy");

// Get the button that opens the modal
var btn = document.getElementById("myBtnPolicy");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("closepolicy")[0];

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
btn.hidden=true;
btn.click();
}
