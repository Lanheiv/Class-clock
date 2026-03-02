const louding_element = document.getElementById("louding_screen");
const select_element = document.getElementById("underline_select");
const select_gruop_element = document.getElementById("underline_select_gruop");

let data, time;
let error = null;
let tt_num = 0, lesson_id = 0;

window.addEventListener("load", function() {
    let test = fetch("/lesson_data").then(response => response.json()).then(d => {
        data = d.data
        error = d.error
        time = d.time

        louding_element.classList.add("hidden");

        if(error) {
            let errore_element = document.getElementById("errore_warning");
            let errore_element_input = document.getElementById("errore_warning_input");

            errore_element.classList.remove("hidden");
            errore_element_input.innerHTML = error;
        }

        time_select()
        show_grop_lessins()
    });
});

select_element.addEventListener("change", function() {
    tt_num = this.value;

    set_grop_lessins();
    show_grop_lessins()
});
select_gruop_element.addEventListener("change", function() {
    lesson_id = this.value;

    show_grop_lessins();
});

function time_select() {
    let array_data = data.r.groups;
    array_data.forEach((g, index) => {
        const option = document.createElement("option");

        option.textContent = g.name;
        option.value = g.tt_num;
        
        if(g.tt_num === data.r.default_num) {
            option.selected = true;
            tt_num = g.tt_num;
        }

        select_element.appendChild(option);
    });
    set_grop_lessins();
}
function set_grop_lessins() { 
    const group_lessons_data = data.r.groups.find(g => g.tt_num == tt_num);
    
    select_gruop_element.options.length = 0;
    
    if (group_lessons_data && group_lessons_data.lessons) {
        group_lessons_data.lessons.forEach((lesson, index) => {
            const option = document.createElement("option");
            option.textContent = lesson.name;
            option.value = index;
            
            select_gruop_element.appendChild(option);
        });
    }
}
function show_grop_lessins() {
    const thead = document.getElementById("header_row");
    thead.innerHTML = "";

    const th_time = document.createElement('th');
    th_time.className = "p-4 border-b border-slate-300 bg-slate-50";
    th_time.innerHTML = "<p class='block text-sm font-normal leading-none text-slate-800'>Dienas</p>";
    thead.appendChild(th_time);

    const time_data = Object.values(time[0].time);
    time_data.forEach(element => {
        const th_time = document.createElement('th');
        th_time.className = "p-4 border-b border-slate-300 bg-slate-50";
        th_time.innerHTML = `<p class="block text-sm font-normal leading-none text-slate-500">${element.value}</p>`;
        thead.appendChild(th_time);
    });

    const tbody = document.getElementById("lesson_data");
    tbody.innerHTML = "";

    const group_lessons_data = data.r.groups.find(g => g.tt_num == tt_num);
    const selected_lesson = group_lessons_data.lessons[lesson_id];

    selected_lesson.days.forEach(element => {
        const tr_lessons = document.createElement('tr');

        const td_day = document.createElement('td');
        td_day.className = "p-4 border-b border-slate-200 py-5";
        td_day.innerHTML = `<p class="text-sm text-slate-500 font-semibold">${element.short}</p>`;
        tr_lessons.appendChild(td_day);

        element.day_lesson.forEach(element => {
            for(let x=1; x <= element.durationperiods; x++) {
                const td_lessons = document.createElement('td');
                td_lessons.className = "p-4 border-b border-slate-200 py-5";
                td_lessons.innerHTML = `<p class="block font-semibold text-sm text-slate-800">${element.subject}</p>`;

                tr_lessons.appendChild(td_lessons);
            }
        });

        tbody.appendChild(tr_lessons);
    });
}