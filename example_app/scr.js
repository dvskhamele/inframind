import $ from 'jquery';
import 'fullcalendar';

$(function() {

  // page is now ready, initialize the calendar...

  $('#calendar').fullCalendar({
    // put your options and callbacks here
  })

});

$('#calendar').fullCalendar({
  weekends: false // will hide Saturdays and Sundays
});

$('#calendar').fullCalendar({
  dayClick: function() {
    alert('a day has been clicked!');
  }
});

// a convenient utility for getting the calendar object.
// you can call methods on the calendar object directly.
var calendar = $('#calendar').fullCalendar('getCalendar');

calendar.on('dayClick', function(date, jsEvent, view) {
  console.log('clicked on ' + date.format());
});

$('#calendar').fullCalendar('next');

var calendar = $('#calendar').fullCalendar('getCalendar');

calendar.next();