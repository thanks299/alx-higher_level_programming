$(function() {
  $('#btn_translate').on('click', function() {
    translate();
  });
  $('#language_code').on('keypress', function(event) {
    if (event.key === 'Enter') {
      translate();
    }
  });
});

function translate() {
  var languageCode = $('#language_code').val();
  $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + languageCode, function(data) {
    $('#hello').text(data.hello);
  });
}
