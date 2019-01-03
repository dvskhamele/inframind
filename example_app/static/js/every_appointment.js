
    function booked(){
    createRow("Your appointment is booked!, You want any changes?");
    }

    var myCalendar;
    var logObj;
    var logInd = 0;
    var logData = [];
    var logInd = 0;

function confirmTime(){
time_input = document.getElementById("timeInput").value;
hrs = time_input.slice(0, 2);
min = time_input.slice(3, 5);
AM = time_input.slice(5, 7);
console.log(":"+time_input);
if(hrs > 17 || hrs < 10 )
{
alert('The time must be between 10:00 AM to 5:00 PM');
}
else{
alert("Your appointment is booked, Thanks :)");
createRow('Thanks :)')
}
}
    function doOnLoad() {
      console.log(currentTime);
      myCalendar = new dhtmlXCalendarObject("calendarHere");
      myCalendar.hideTime();
document.getElementById("calendarCase").style.height = "321px";
document.getElementById("calendarHere").text = "Please book an appointment here,";
document.getElementById("calendarHere").style.height = "300px";
document.getElementById("timeCase").style.display = "block";

      myCalendar.show();
      var date = new Date();
      var currentDate = date.toISOString().slice(0,10);
      var currentTime = date.getHours() + ':' + date.getMinutes();
      console.log(currentTime);
      

      myCalendar.setInsensitiveDays(["2018-09-08","2018-10-13","2018-09-22","2018-13-08","2018-10-27","2018-11-10","2018-11-24","2018-12-08","2018-12-22","2018-12-25"]);
      myCalendar.setSensitiveRange(new Date(),null );
      myCalendar.disableDays("week", 7);

      myCalendar.attachEvent("onChange", function(d){
        logData.push(myCalendar.getFormatedDate("%d-%m-%Y",d));
        writeLog();
      console.log(myCalendar.getFormatedDate("%d-%m-%Y",d));
      });
      myCalendar.attachEvent("onArrowClick", function(d_old,d_new){
        logData.push(myCalendar.getFormatedDate("%d-%m-%Y",d_new));
        writeLog();
      console.log(myCalendar.getFormatedDate("%d-%m-%Y",d_new));
      });
    
    
    function writeLog() {
      if (!logObj) logObj = document.getElementById("ChatInput");
      var t = "";
      for (var q=logData.length-1; q>=Math.max(logData.length-6,0); q--) t += logData[q]+"<br>";
            console.log(t);
    }
    
    function set_date_with_input(){
      myCalendar.setFormatedDate("%d-%m-%Y", document.getElementById("ChatInput").value);
            console.log(document.getElementById("ChatInput").value);
    }
    }