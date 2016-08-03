
$(document).ready(function () {
    // Ajax setup to forward the CSRF token
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            // generate CSRF token using jQuery
            var csrftoken = $.cookie('csrftoken');
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('#signInModal').on('shown.bs.modal', function () {
        $('#login_text').focus();
    });
});

function onSelectItem(number, id) {
  idobj = $("#employeeid");
  if (idobj[0].value == "") {
    $("#employeeiderror")[0].innerHTML = "Please enter your employee ID";
    return;
  }
  myid = idobj[0].value;
  $.post('/it/makerequest', {
      'id': myid,
      'itemid': id,
      'itemnumber': number
    },
      function(data) {
        $("#employeeiderror")[0].innerHTML = "";
        alert(data);
    });
}

// send an accept_req POST request to the server.
function accept_req(reqid) {
  $.post('/it/accept_req/', {
    'reqid': reqid,
  }, function(data) {
    if (data == "ok") {
      // refresh the page to update the view
      location.reload();
    } else {
      alert("Failed to do action: " + data);
    }
  });
}

// send a reject_req POST request to the server.
function reject_req(reqid) {
  $.post('/it/reject_req/', {
    'reqid': reqid,
  }, function(data) {
    if (data == "ok") {
      // refresh the page to update the view
      location.reload();
    } else {
      alert("Failed to do action: " + data);
    }
  });
}

