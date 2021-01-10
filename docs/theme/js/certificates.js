let index = 0;
let languages = ['html', 'css', 'javascript', 'jquery', 'python', 'php', 'sql'];
function printLanguage() {
  if (index === languages.length) index = 0;  $('input[type="search"]').attr('placeholder', languages[index]);
  index++;
}
printLanguage();
window.setInterval(printLanguage, 1500);

/**
 * @param query {string} searchquery
 */
function search(query) {
  $('#results').empty(); // remove results from last search

  if (query === '') return false; // exit

  // console.log($('#results'));
  query = query.toLowerCase();
  // console.log(query);
  jQuery.each(certificates, function(index, path) {
    let basename, li, a;
    basename = utils.basename(path);
    basenameLower = basename.toLowerCase();
    if (
      basenameLower.includes(query) &&
      $(`#results a[href="${path}"]`).length == 0
    ) {
      // console.log(basenameLower, query);
      li = $('<li></li>');
      a = $('<a></a>').attr({
        href: path,
        target: '_blank',
        title: 'open PDF in new tab'
      });
      a.text(basename);
      $('#results').append(li.append(a));
    }
  });
}
