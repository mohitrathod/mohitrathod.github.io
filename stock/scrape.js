$(document).ready(function () {

  var mohit_json;


  $.ajax({url: "https://api.myjson.com/bins/1166d9", success: function(result){
            console.log(result);
            mohit_json = result;
            if (!mohit_json.mohit_data.data) {
              mohit_json.mohit_data.data = [];
            }
            // var data1 = 'mmo';
            // mohit_json.mohit_data.data.push(data1);
            push_data(mohit_json);
        }});

var push_data = function (mohit_json) {
  $.ajax({
        url: "https://api.myjson.com/bins/1166d9",
        type: "PUT",
        data: JSON.stringify(mohit_json),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        crossDomain: true,
        success: function (result, textStatus, jqXHR) {
          console.log(result);
        },
        error: function (jqXHR, exception) {

            console.log(jqXHR.status)
            console.log(exception);

        },
    });
}






});
