
    var i = 1;
      $('.add').click(function() {
        var field = '<div><input id="fullname"name="phone" placeholder="+234 " type="text"><select id="provider" name="provider"><option> MTN </option><option> Etisalat </option><option> Glo </option><option> Airtel </option></select><input id="amount" name="amount" placeholder="Amount" type="number"><div class="clear"></div></div>';
        $('.del').append(field);
        i = i+1;
      })