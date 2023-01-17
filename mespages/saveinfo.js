function saveinfo(){
        var $formName  = "info-form";

    $.ajax({type:'post',url: "/saveinfo?",
        data:$("."+$formName).serialize(),
        success:function(data){
            console.log(data.url);
                if (data.sauve === "1") {
 // Get the snackbar DIV
  var x = document.getElementById("infosmodif");

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 2000);
  
            }else {
                  document.querySelector(".email-error").innerHTML = "Cet utilisateur n'existe pas"; document.querySelector(".email-error").style.display = "block";            
	      document.querySelector(".email-error").style.color = "red";            
	      document.querySelector("#email").style.border = "1px solid red";            
	      document.querySelector("label[for=email]").style.color = "red";            
	      var x = document.querySelector("label[for=email]");
              if (!x.innerHTML.includes("*")) {
                  x.innerHTML = x.innerHTML + " *";
              }  
                }
            
        },error:function(xhr){
            var err = JSON.parse(xhr.responseText);
            console.log(err.data);            
        }
        }
        );
    }
