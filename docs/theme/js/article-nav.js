$(function() {

  /**
   * built article contents navigation of headlines
   * give each article headline refererencing link
   */

  let headlines = $('.entry-content h1, .entry-content h2, .entry-content h3, .entry-content h4, .entry-content h5, .entry-content h6');

  // fill navigation
  if (headlines.length !== 0) {
    headlines.each(function(index, element) {
      // console.log(index, element);
      $(element).attr('id', index);
      let link = $(`<li><a href='#${index}'>${$(this).text()}</a></li>`);
      $(`<a href='#${index}'><i class='icon'>link</i></a>`).appendTo(element);
      link.appendTo('aside nav ul');
    });
  }
  // no headings - no navigation, go hide it
  else {
    $('aside nav').hide();
  }

})
