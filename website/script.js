let time = 25 * 60;

const timer = document.getElementById("timer");
const button = document.getElementById("startBtn");

button.onclick = function () {

    const interval = setInterval(function () {

        time--;

        let minutes = Math.floor(time / 60);
        let seconds = time % 60;

        timer.textContent =
            String(minutes).padStart(2, "0")
            + ":"
            + String(seconds).padStart(2, "0");

        if (time <= 0) {
            clearInterval(interval);
            alert("Pomodoro finished!");
        }

    }, 1000);

};