$(function() {

  let videos, currentVideoIndex;
  videos = [
    './media/videos/landing-vid.webm',
    './media/videos/landing-19163600.webm',
    './media/videos/landing-21054100.webm',
    './media/videos/landing-17392000-1.webm',
    './media/videos/landing-00331700.webm',
  ];
  // if not set already set random starting video index
  // console.log(utils.getCookie('sessionVid'));
  videoIndex = utils.getCookie('sessionVid') ? utils.getCookie('sessionVid') : utils.setCookie('sessionVid', Math.floor(Math.random() * videos.length));

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
