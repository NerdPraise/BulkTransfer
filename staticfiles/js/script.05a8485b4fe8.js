
var i = 1;
$('.add').click(function () {
  var field = '<hr><input id="phone" name="phone_' + i + '" placeholder="+234 " type="text"><select id="provider" name="provider_' + i + '"><option> Select a Provider </option><option> MTN </option><option> Etisalat </option><option> Glo </option><option> Airtel </option></select><input id="amount" name="amount_' + i + '" placeholder="Amount" type="number"><div class="clear"></div>';
  $('.del').append(field);
  i = i + 1;
})

var AlertBox = function(id, option) {
  this.show = function(msg) {
    if (msg === ''  || typeof msg === 'undefined' || msg === null) {
      throw '"msg parameter is empty"';
    }
    else {
      var alertArea = document.querySelector(id);
      var alertBox = document.createElement('DIV');
      var alertContent = document.createElement('DIV');
      var alertClose = document.createElement('A');
      var alertClass = this;
      alertContent.classList.add('alert-content');
      alertContent.innerText = msg;
      alertClose.classList.add('alert-close');
      alertClose.setAttribute('href', '#');
      alertBox.classList.add('alert-box');
      alertBox.appendChild(alertContent);
      if (!option.hideCloseButton || typeof option.hideCloseButton === 'undefined') {
        alertBox.appendChild(alertClose);
      }
      alertArea.appendChild(alertBox);
      alertClose.addEventListener('click', function(event) {
        event.preventDefault();
        alertClass.hide(alertBox);
      });
      if (!option.persistent) {
        var alertTimeout = setTimeout(function() {
          alertClass.hide(alertBox);
          clearTimeout(alertTimeout);
        }, option.closeTime);
      }
    }
  };

  this.hide = function(alertBox) {
    alertBox.classList.add('hide');
    var disperseTimeout = setTimeout(function() {
      alertBox.parentNode.removeChild(alertBox);
      clearTimeout(disperseTimeout);
    }, 500);
  };
};

// Sample invoke
var alertShowMessage = document.querySelector('#alertShowMessage');
var alertMessageBox = document.querySelector('#alertMessageBox');
var alertbox = new AlertBox('#alert-area', {
  closeTime: 5000,
  persistent: false,
  hideCloseButton: false
});
var alertboxPersistent = new AlertBox('#alert-area', {
  closeTime: 5000,
  persistent: true,
  hideCloseButton: false
});
var alertNoClose = new AlertBox('#alert-area', {
  closeTime: 5000,
  persistent: false,
  hideCloseButton: true
});


$(".btnss").click(function() {
  event.preventDefault()
  let form_url = $("#form").attr("form-data-url")
  formdata = {}
  tot = (($("form input").length - 1) +  (($("form input").length - 1)/2))/3
  for (i=0; i<tot; i++){
    formdata["phone_"+ i] = $('input[name=phone_' + i +']').val()
    formdata["amount_"+ i] = $('input[name=amount_' + i +']').val()
    formdata["provider_"+ i] = $('select[name=provider_' + i +']').val()
  }
  $.ajax({
    url: form_url,
        type: "POST",
        data: formdata,
        success: function (data) {
            if (data.error) {
                alert(data.error)
            }
            if (data.success) {
              for (i of data.success)
                alertbox.show(i);
                $("form")[0].reset()
            }
        },
  })

})
