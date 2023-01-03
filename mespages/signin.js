
window.onload=function(){
document.addEventListener('input', function(event) {
  if (event.target.nodeName && event.target.nodeName === "INPUT") {
    if (event.target.value) {
      event.target.setAttribute('filled', 'true')
    } else {
      event.target.removeAttribute('filled')

    }
  }
});
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    /* Toggle between adding and removing the "active" class,
    to highlight the button that controls the panel */
    this.classList.toggle("active");

    /* Toggle between hiding and showing the active panel */
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}
function validatecode(){
    
}
};