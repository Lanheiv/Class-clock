const hour = document.getElementById('hour');
const sec = document.getElementById('sec');
const min = document.getElementById('min');
const clockBox = document.getElementById('clock');
const ml = document.getElementById('ml');
let ampm = document.querySelector(".pm");


function clock() {
    let date = new Date();
    let h = date.getHours();
    let s = date.getSeconds();
    let m = date.getMinutes();
    let mll = date.getMilliseconds();

    updateTheme(h);
    if (h < 10) {

        hour.innerHTML = '0' + h;

    }
    else {
        hour.innerHTML = h;
    }


    if (h >= 12) {
        ampm.innerHTML = "PM";
        if (h > 12) h -= 12;
    } else {
        ampm.innerHTML = "AM";
    }



  
    if (s < 10) {


        sec.innerHTML = '0' + s;
    }
    else {
        sec.innerHTML = s;
    }
    if (m < 10) {


        min.innerHTML = '0' + m;
    }
    else {
        min.innerHTML = m;
    }

    ml.innerHTML = mll;


};
function updateTheme(h) {
    if (h >= 6 && h < 18) {
        document.body.style.backgroundColor = "#f8f9fa"; // Light mode
        document.body.style.color = "#333";
    } else {
        document.body.style.backgroundColor = "#212529"; // Dark mode
        document.body.style.color = "#fff";
    }
}
function playTickSound() {
    let sound = document.getElementById("tick-sound");
    sound.play();
}
function updateDate() {
    let date = new Date();
    let options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    document.getElementById("date").innerHTML = date.toLocaleDateString('en-US', options);
}
updateDate();

clock();
setInterval(clock, 1);
setInterval(playTickSound, 1000);
