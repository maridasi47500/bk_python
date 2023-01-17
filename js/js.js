function on() {
  document.getElementById("menu").style.display = "block";
  document.getElementById("menubtn").outerHTML = "<span class=\"menu\" id=\"menubtn\" onclick=\"off();return false;\">&#10005;</span>";
}

function off() {
  document.getElementById("menu").style.display = "none";
  document.getElementById("menubtn").outerHTML = "<span class=\"menu\" id=\"menubtn\" onclick=\"on();return false;\">&#9776;</span>";

} 
