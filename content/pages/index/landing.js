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

  // random starting video on every page load
  videoIndex = Math.floor(Math.random() * videos.length);

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
