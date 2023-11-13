function animateText(element) {
  var text = $(element).text().split('');
  $(element).html('');
  $.each(text, function(index, letter) {
    $(element).append('<span style="display: none;">' + letter + '</span>');
  });
  $(element).find('span').each(function(index) {
    $(this).delay(20 * index).fadeIn();
  });
}

animateText('#animated-title')