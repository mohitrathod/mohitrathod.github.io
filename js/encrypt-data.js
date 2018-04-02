
$(document).ready(function () {

  var data = "mmmooohhhiit";
  var encrypted_data = sjcl.encrypt("password", data);
  console.log(encrypted_data);

  console.log(sjcl.decrypt("password", encrypted_data));

});
