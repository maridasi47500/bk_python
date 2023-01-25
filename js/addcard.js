function myfuncaddcard(){
$.ajax({
  url: "/savepayment",
  type:"post",
  data:$("form").serialize(),
  success: function(data){
    if (data.ok === "1"){
      //overlay carte enregistrée
      // Get the snackbar DIV
       var x = document.getElementById("messageaddcard");

       // Add the "show" class to DIV
       x.className = "show";

       // After 3 seconds, remove the show class from DIV
       setTimeout(function(){ x.className = x.className.replace("show", ""); }, 2000);
     }else{
       on()
    }
  }
})
}
function myfuncaddgiftcard(){
  $.ajax({url:"/savegiftcard",
  type:"post",
  data:$("form").serialize(),
  success: function(data){
    if (data.ok === "1"){
      // overlay carte enregistrée
      // Get the snackbar DIV
       var x = document.getElementById("messageaddgiftcard");

       // Add the "show" class to DIV
       x.className = "show";

       // After 3 seconds, remove the show class from DIV
       setTimeout(function(){ x.className = x.className.replace("show", ""); }, 2000);
    }else{
      on()
    }
  }
})
}
function on() {
  document.getElementById("overlay").style.display = "block";
}

function off() {
  document.getElementById("overlay").style.display = "none";
}
