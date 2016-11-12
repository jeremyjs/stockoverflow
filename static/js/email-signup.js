$(function () {
  $('.email-signup.button').click(function (e) {
    var email = $('input.email').val();
    if (email === '') return;
    $('input.email').attr('disabled', true).addClass('disabled');
    var original_signup_message = $('.email-signup.button').html();
    $('.email-signup.button').html('<i class="fa fa-lg fa-circle-o-notch fa-spin"></i>');
    var signup_url = '/email/signup/' + email;
    $.get(signup_url)
    .done(function (res) {
      res = JSON.parse(res);
      console.log(res);
      if (res.success) {
        window.setTimeout(function () {
          $('input.email').val('');
          $('input.email').attr('disabled', false).removeClass('disabled')
          $('.email-signup.button').html('<i class="fa fa-lg fa-check-circle-o"></i>');
          var cancelResetSignupButton = window.setTimeout(function () {
            $('.email-signup.button').html(original_signup_message);
          }, 2000);
        }, 1500);
      } else {
        $('.email.message').html(res.message);
      }
    })
    .fail(function (err) {
      console.log(err);
      $('.email.message').html(err.message);
    });
  });
});
