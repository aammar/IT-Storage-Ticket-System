var allitems = [];

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

  allitems = $(".availableitem");
});

function login() {
  var username = $("#username")[0].value;
  var password = $("#password")[0].value;
  if (username != "" && password != "") {
    $.post('/it/login/', {
      'username': username,
      'password': password,
    }, function (data) {
      if (data == "ok") {
        location.reload();
      } else {
        $("#loginerror")[0].innerHTML = data;
      }
    });
  }
}

function logout() {
  $.post('/it/logout/', {
  }, function (data) {
    location.reload();
  });
}

function toggleCat(catid) {
  var container = $("#container-"+catid);
  if ($("#icon-"+catid).hasClass('glyphicon-minus')) {
    $("#icon-"+catid).removeClass('glyphicon-minus');
    $("#icon-"+catid).addClass('glyphicon-plus');
  } else {
    $("#icon-"+catid).removeClass('glyphicon-plus');
    $("#icon-"+catid).addClass('glyphicon-minus');
  }
  container.slideToggle();
  return false;
}

function update_search() {
  var text = $("#searchtext")[0].value.toLowerCase();
  if (text == "") {
    $("#categories").show();
    $("#search-container").hide();
  } else {
    $("#categories").hide();
    $("#search-container").show();

    var result = "<div>";
    for (var i = 0; i < allitems.length; i++) {
      var item = $(allitems[i]).find('h3 > a')[0];
      var itname = item.innerHTML.toLowerCase();
      if (itname.indexOf(text) != -1)
        result += '<div class="col-sm-6 col-md-4">' + allitems[i].innerHTML + '</div>';
    }
    result += "</div>";
    $("#searchables")[0].innerHTML = result;
  }
}

function itemRemover(id) {
  $(id).remove();
}

function onAddItem(number, itemTitle) {
  var id = "item-" + number;
  var item = "<div id='" + id + "'>";
  item += "<h3><a onclick='itemRemover(\"#"+id+"\")'><span class='glyphicon glyphicon-remove'></span></a> " + itemTitle + "</h3>";
  item += "</div>";
  $("#request-summary")[0].innerHTML += item;
}

function onMakeRequest() {
  var idobj = $("#employeeid");
  var desc = $("#request-desc");
  if (idobj[0].value == "") {
    $("#employeeiderror")[0].innerHTML = "Please enter your employee ID";
    return;
  }
  if (desc[0].value == "") {
    $("#employeeiderror")[0].innerHTML = "Please enter a description for the request";
    return;
  }
  var myid = idobj[0].value;
  if (myid != "") {
    var items = $("#request-summary > div");
    var list = [];
    for (var i = 0; i < items.length; i++) {
      var idtext = $(items[i]).attr('id').substring(5);
      var number = idtext.substring(0);
      list += [number];
    }
    $.post('/it/makerequest', {
        'id': myid,
        'items': JSON.stringify(list),
        'desc': desc[0].value
      }, function(data) {
          if (data == "ok") {
            $("#employeeiderror")[0].innerHTML = "";
            $("#request-summary")[0].value = "";
            $("#employeeid")[0].value = "";
          }
      });
  }
}

// send an accept_req POST request to the server.
function accept_req(reqid) {
  var desc = $("#request-response-"+reqid)[0].value;
  $.post('/it/accept_req/', {
    'reqid': reqid,
    'desc': desc,
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
  var desc = $("#request-response-"+reqid)[0].value;
  $.post('/it/reject_req/', {
    'reqid': reqid,
    'desc': desc,
  }, function(data) {
    if (data == "ok") {
      // refresh the page to update the view
      location.reload();
    } else {
      alert("Failed to do action: " + data);
    }
  });
}

function on_return(itid) {
  $.post('/it/return_item/', {
    'itid': itid,
  }, function(data) {
    if (data == "ok") {
      // refresh the page to update the view
      location.reload();
    } else {
      alert("Failed to do action: " + data);
    }
  });
}

function on_lost(itid) {
  $.post('/it/lost_item/', {
    'itid': itid,
  }, function(data) {
    if (data == "ok") {
      // refresh the page to update the view
      location.reload();
    } else {
      alert("Failed to do action: " + data);
    }
  });
}

function delete_user(uid) {
  $.post('/it/delete_user/', {
    'uid': uid,
  }, function(data) {
    if (data == "ok") {
      // refresh the page to update the view
      location.reload();
    } else {
      alert("Failed to do action: " + data);
    }
  });
}

function on_new_item() {
  $("#newitem").show();
  $("#restockitem").hide();
  $("#newitemtab").addClass('active');
  $("#restocktab").removeClass('active');
}

function on_restock() {
  $("#newitem").hide();
  $("#restockitem").show();
  $("#newitemtab").removeClass('active');
  $("#restocktab").addClass('active');
}

function submit_new_item(url) {
  $.get(url, {
    "itemid": $("#itemid")[0].value,
    "itemnumber": $("#itemnumber")[0].value,
    "itemmake": $("#itemmake")[0].value,
    "itemmodel": $("#itemmodel")[0].value,
    "itemcat": $("#itemcat")[0].value,
    "itemurl": $("#itemurl")[0].value,
    "itemdesc": $("#itemdesc")[0].value,
  }, function(data) {
    if (data == "ok") {
      location.reload();
    } else {
      $("#newitemerror")[0].innerHTML = data;
    }
  });
}

function submit_restock(url) {
  $.get(url, {
    "itemid": $("#itemid-restock")[0].value,
    "itemnumber": $("#itemnumber-restock")[0].value,
  }, function(data) {
    if (data == "ok") {
      $("#itemid-restock")[0].value = "";
      $("#newitemerror")[0].innerHTML = "";
    } else {
      $("#newitemerror")[0].innerHTML = data;
    }
  });
}

function organize_reqitems() {
  var container = $("#reqitems");
  var items = $(".reqitemcontainer");

  var newcode = "";
  for (var i = 0; i < items.length/3; i++) {
    newcode += "<div class='row'>";
    for (var j = i * 3; j < items.length && j < i * 3 + 3; j++)
      newcode += items[j].innerHTML;
    newcode += "</div>";
  }
  container[0].innerHTML = newcode;
}

function get_relative_time(t) {
  var cur_time = new Date();
  var in_time = new Date(t);
  var deltaMS = cur_time.getTime() - in_time.getTime();
  var deltaSec = deltaMS / 1000.0;
  var deltaMin = deltaSec / 60.0;
  var deltaHr = deltaMin / 60.0; deltaMin = deltaMin % 60;
  var deltaDay = deltaHr / 24.0; deltaHr = deltaHr % 24;

  if (deltaDay > 30)
    return gettext("more than a month ago");
  if (deltaDay > 1) {
    if (deltaDay < 2)
      return gettext("yesterday");
    return interpolate(gettext("%s days ago"), [Math.floor(deltaDay)]);
  } else {
    if (deltaHr > 1)
      return interpolate(gettext("%s hours %s minutes ago"), [Math.floor(deltaHr), Math.floor(deltaMin)]);
    else if (deltaMin > 1) {
      if (deltaMin < 2)
        return interpolate(gettext("%s minutes ago"), [Math.floor(deltaMin)]);
      return interpolate(gettext("%s minutes ago"), [Math.floor(deltaMin)]);
    } else
      return gettext("just now");
  }
}
