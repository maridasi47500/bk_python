function myfunc2(){
        var $formName  = "sign-up-form";

    $.ajax({type:'post',url: "/checkuser.json",
            data: {email: (email.value)},
        success:function(data){
            
                if (confidentialite.checked === true && data.usernotexist === "1") {
                document.forms[$formName].submit();
            }else if(data.usernotexist === "0") {
                  document.querySelector(".email-error").innerHTML = "Cet utilisateur existe";
	      document.querySelector(".email-error").style.display = "block";            
	      document.querySelector(".email-error").style.color = "red";            
	      document.querySelector("#email").style.border = "1px solid red";            
	      document.querySelector("label[for=email]").style.color = "red";
              var x = document.querySelector("label[for=email]");
              if (!x.innerHTML.includes("*")) {
                  x.innerHTML = x.innerHTML + " *";
              }
              }else if(data.usernotexist === "1") {
                  document.querySelector(".email-error").innerHTML = "";
	      document.querySelector(".email-error").style.display = "block";            
	      document.querySelector(".email-error").style.color = "black";            
	      document.querySelector("#email").style.border = "1px solid black";            
	      document.querySelector("label[for=email]").style.color = "black";            
              }
              if (confidentialite.checked !== true) {
	      document.querySelector("#confidentialite").style.border = "1px solid red";  
              document.querySelector(".confidentialite-error").innerHTML = "Vous devez accepter la politique de confidentialité et les conditions d'utilisation avant de vous inscrire.";
	      document.querySelector(".confidentialite-error").style.display = "block";            
	      document.querySelector(".confidentialite-error").style.color = "red";            
	      document.querySelector("label[for=confidentialite]").style.color = "red";            

                }else{
	      document.querySelector("#confidentialite").style.border = "1px solid black";  
              document.querySelector(".confidentialite-error").innerHTML = "";
	      document.querySelector(".confidentialite-error").style.display = "block";            
	      document.querySelector(".confidentialite-error").style.color = "black";            
	      document.querySelector("label[for=confidentialite]").style.color = "black";            

                }
                
            
        },error:function(xhr){
            var err = JSON.parse(xhr.responseText);
            console.log(err.data);            
        }});
    };
function myfunc(){
        var $formName  = "sign-in-form";

    $.ajax({type:'post',url: "/checkemail",
            data: {email: (email.value)},
        success:function(data){
            console.log(data.url);
                if (data.correctemail === "1") {
                document.forms[$formName].submit();
            }else {
                  document.querySelector(".email-error").innerHTML = "Cet utilisateur n'existe pas";
	      document.querySelector(".email-error").style.display = "block";            
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
window.onload=function(){
    if (document.getElementById("myform") && myform.name=== "sign-in-form") {
    myform.addEventListener('submit', function(e){
    e.preventDefault();
    myfunc();
    });
    }
    if (document.getElementById("myform") && myform.name=== "sign-up-form") {
    myform.addEventListener('submit', function(e){
    e.preventDefault();
    myfunc2();
    });
    }

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
};
function validatecode(e){
    if (e.target.value.length === 6) {
        $.ajax({type:'post',url: "/validatecode",
            data: {code: (e.target.value),userid: String(e.target.dataset.userid)},
        success:function(data){
            console.log(data.url);
                if (data.correcturl === "1") {
                     $.ajax({
                         url:"/setcookie?user="+String(data.id),
                         success:function(datadata){
                             window.location = data.url;
                         }
                         });
                        
                    
                }else {
                  document.querySelector(".code-error").innerHTML = "Le code que vous avez entré ne correspond pas au code que nous avons envoyé. Vérifiez vos messages et essayez de les saisir à nouveau.";
	      document.querySelector(".code-error").style.display = "block";            
	      document.querySelector(".code-error").style.color = "red";            
	      document.querySelector("#code").style.border = "1px solid red";            
	      document.querySelector("label[for=code]").style.color = "red";            
	      var x = document.querySelector("label[for=code]");
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
    return false;
}


