
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
  myid = '2'; // TODO: get this from form
  $.post('/it/makerequest', {
      'id': myid,
      'itemid': id,
      'itemnumber': number
    },
      function(data) {
        alert(data);
    });
}
