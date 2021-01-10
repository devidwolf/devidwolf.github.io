$(function() {

  let md = parseInt( getComputedStyle(document.documentElement).getPropertyValue('--breakpoint-md'));
  // console.log($(window).width(), md);

  $(window).on('load resize', function() {

    if ($(window).width() < md) {
      $('nav details').attr('open', false);
      $('nav details summary').unbind('click');
    } else {
      $('nav details').attr('open', true);
      $('nav details summary').click(function(event) {
        event.preventDefault();
      });
    }

  });

});
