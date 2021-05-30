$(function() {
  let videos, currentVideoIndex;

  videos = [
    './media/videos/landing-vid.webm',
    './media/videos/landing-19163600.webm',
    './media/videos/landing-21054100.webm',
    './media/videos/landing-17392000-1.webm',
    './media/videos/landing-00331700.webm',
    './media/videos/00532700.webm',
    './media/videos/00072300.webm',
    './media/videos/20424700.webm',
    './media/videos/02084900.webm',
    './media/videos/21091400.webm',
    './media/videos/02560300.webm',
    './media/videos/22115200.webm',
    './media/videos/05484600.webm',
    './media/videos/23005500.webm',
    './media/videos/05541400.webm',
    './media/videos/23161000.webm',
    './media/videos/19343100.webm',
    './media/videos/23591700.webm',
  ];

  // if not set already set random starting video index
  // console.log(utils.getCookie('sessionVid'));
  if (utils.getCookie('sessionVid')) {
    videoIndex = utils.getCookie('sessionVid');
  } else {
    videoIndex = Math.floor(Math.random() * videos.length);
    utils.setCookie('sessionVid', videoIndex);
  }
  // console.log(videoIndex);

  $('#landing-vid').attr('src', videos[videoIndex]);
  $('#landing-vid').trigger('play');

  // video autoplay playlist
  // https://stackoverflow.com/a/17522421/13765033
  $('#landing-vid').on('ended', function() {
    videoIndex++;
    if (videoIndex === videos.length) videoIndex = 0;
    // console.log(videos[videoIndex]);
    $(this).attr('src', videos[videoIndex]);
    $(this).trigger('play');
  });

});
