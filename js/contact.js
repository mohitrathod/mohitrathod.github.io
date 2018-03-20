
$(document).ready(function () {

  $('#feedbacks-click').click(function(){
    $.get("/html/feedbacks.html", function(data){
      $('#feedbacks-div').html(data);
    });
  });



});
