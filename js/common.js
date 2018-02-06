
$(document).ready(function () {

  var path = window.location.pathname.substring(1);
  path = '/' + path;
  $('.scrollmenu>a[href=" + ' + path + '"]').addClass('active');

});
