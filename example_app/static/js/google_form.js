$(document).ready( function() {
  $('.cookies-used').fadeIn();
  intert.setEvents();
});

var intert = {};

intert.setEvents = function() {
  $('.black-complete-background').click( function() {
    $('.password-reset-div').fadeOut();
  });
}

intert.showPasswordForgotten = function() {
  $('.password-reset-div').fadeIn();
}

intert.closePF = function() {
   $('.password-reset-div').fadeOut();
}