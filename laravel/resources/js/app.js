let louding_element = document.getElementById("louding_screen");

let data, time;
let error = null;

window.addEventListener("load", function() {
    let test = fetch("/lesson_data").then(response => response.json()).then(d => {
        data = d.data
        time = d.time
        error = d.error

        louding_element.classList.add("hidden");

        if(error) {
            let errore_element = document.getElementById("errore_warning");
            let errore_element_input = document.getElementById("errore_warning_input");

            errore_element.classList.remove("hidden");
            errore_element_input.innerHTML = error;
        }
    });
});