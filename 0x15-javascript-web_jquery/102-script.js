$(function() {
  $('#btn_translate').on('click', function() {
    var languageCode = $('#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + languageCode, function(data) {
      $('#hello').text(data.hello);
    });
  });
});
