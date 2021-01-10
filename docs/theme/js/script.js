$(function() {

  /**
   * allow open/closing of nav groups
   */
  let md = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--breakpoint-md'));
  // console.log($(window).width(), md);
  $(window).on('load resize', function() {
    if ($(window).width() < md) {
      $('nav details').attr('open', false);
      $('nav details summary').attr('tabindex', 0);
      $('nav details summary').unbind('click');
    } else {
      $('nav details').attr('open', true);
      $('nav details summary').attr('tabindex', -1);
      $('nav details summary').click(function(event) {
        event.preventDefault();
      });
    }
  });

  /**
   * highlight active nav item
   */
  let url = window.location.href;
  // console.log(links);
  $('nav a').each(function(index, link) {
    // console.log(link);
    if (link.href === url) {
      link.dataset.active = true;
      link.removeAttribute('href');
      return false; // https://stackoverflow.com/a/5515211/13765033
    }
  });

});
