
$(document).ready(function () {

  var path = window.location.pathname.substring(1);
  path = '/' + path.trim();
  $('.scrollmenu>a[href="' + path + '"]').addClass('active');
  alert(path);
});
