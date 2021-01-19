$(function() {

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
