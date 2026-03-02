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
    const group_lessons_data = data.r.groups.find(g => g.tt_num == tt_num);
    const selected_lesson = group_lessons_data?.lessons[lesson_id];

    const tbody = document.getElementById('lesson_tabel');
    tbody.innerHTML = '';

    time.forEach(element => {
        
    });
}









function show_grop_lessins() {
    const group_lessons_data = data.r.groups.find(g => g.tt_num == tt_num);
    const selected_lesson = group_lessons_data?.lessons[lesson_id];

    const tbody = document.getElementById('lesson_tabel');
    tbody.innerHTML = '';

    let time = ["8:30-9:50", "10:10-11:30", "11:30-12:30", "12:30-13:50", "14:00-15:20", "15:30-16:50", "15:30-16:50"];
    
    time.forEach((timeSlot, rowIndex) => {
        // Create new row
        const row = document.createElement('tr');
        
        // Time column (Laiks)
        const timeCell = document.createElement('td');
        timeCell.className = 'p-4 border-b border-slate-200 py-5';
        timeCell.innerHTML = `<p class="block font-semibold text-sm text-slate-800">${timeSlot}</p>`;
        row.appendChild(timeCell);
        
        // 5 day columns
        const days = ['Pirmdiena', 'Otrdiena', 'Trešdiena', 'Ceturtdiena', 'Piektdiena'];
        days.forEach((dayName, dayIndex) => {
            const dayCell = document.createElement('td');
            dayCell.className = 'p-4 border-b border-slate-200 py-5';
            
            // Show lesson subject or empty
            const lessonData = selected_lesson?.[rowIndex];
            if (lessonData && lessonData.subject) {
                dayCell.innerHTML = `<p class="text-sm text-slate-500">${lessonData.subject}</p>`;
            }
            
            row.appendChild(dayCell);
        });
        
        tbody.appendChild(row);
    });
}

