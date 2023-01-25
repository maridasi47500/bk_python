function refresh() {
  $.ajax({
    url:"/orders/refresh",
    success:function(data){
      if (data.length > 0){
        document.getElementById("mydiv").innerHTML = data;
      }

    }
  })
}
