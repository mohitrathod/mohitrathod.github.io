
$(document).ready(function () {

  var path = window.location.pathname.substring(1);

  $('.scrollmenu>a[href="/ + ' + path + '"]').addClass('active');

});
