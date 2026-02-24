import traceback
import json

from .file_function import *

def raw_data_formatting():
    formated_data_store_path = "laravel/storage/app/json/formatted_data.json" # old path "scoper/files/formatted_data.json"
    lesson_data = {"r": {}}

    try:
        TTViewerData_data = json.loads(read_file('scoper/files/raw/TTViewerData.json'))
    except Exception:
        write_errore_file("Failed to read/parse TTViewerData.json:\n" + traceback.format_exc())
        return

    lesson_data["r"] = { "default_num": TTViewerData_data["r"]["regular"]["default_num"], "groups": [], "lesson_time":[] }
    for fordata in TTViewerData_data["r"]["regular"]["timetables"]:
        lesson_data["r"]["groups"].append({ "name": fordata["text"], "tt_num": fordata["tt_num"], "year": fordata["year"], "lessons": [] })

    regularttGetDatalist_data = []
    for fordata in lesson_data["r"]["groups"]:
        try:
            regularttGetDatalist_data.append(json.loads(read_file(f'scoper/files/raw/regularttGetData_{fordata["tt_num"]}.json')))
        except Exception:
            write_errore_file(f"Failad to read/parse regularttGetData_{fordata["tt_num"]}.json:\n" + traceback.format_exc())
            return

    for count, group in enumerate(lesson_data["r"]["groups"]):
        dbiAccessorRes = regularttGetDatalist_data[count]["r"]["dbiAccessorRes"]["tables"]

        row_data = dbiAccessorRes[12]["data_rows"]
        day_data = dbiAccessorRes[7]["data_rows"]

        for row in row_data:
            group["lessons"].append({
                "id": row["id"],
                "name": row["name"],
                "class_teacher": get_teacher(row["teacherid"], dbiAccessorRes),
                "days": [
                    {
                        "id": day["id"],
                        "day": day["name"],
                        "short": day["short"],
                        "day_lesson": get_lessons(row["id"], day["id"], dbiAccessorRes)
                    }
                    for day in day_data
                ]
            })
    try:
        lesson_data["r"]["lesson_time"] = json.loads(read_file('scoper/files/time.json'))
    except Exception:
        write_errore_file("Failed to read time data" + traceback.format_exc())
        return

    write_file(formated_data_store_path, lesson_data)

def get_teacher(teacher_id, dbiAccessorRes):
    teacher_data = dbiAccessorRes[14]["data_rows"]
    
    for teacher in teacher_data:
        if teacher["id"] == teacher_id:
            return teacher["name"]

def get_subject(subject_id, dbiAccessorRes):
    subject_data = dbiAccessorRes[13]["data_rows"]
    
    for subject in subject_data:
        if subject["id"] == subject_id:
            return subject["name"]

def get_lessons(group_id, day_index, dbiAccessorRes):
    day_index = int(day_index)
    lesson_array = []

    lessons = dbiAccessorRes[18]["data_rows"]
    cards = dbiAccessorRes[20]["data_rows"]

    for lesson in lessons:
        if group_id in lesson["classids"]:
            for card in cards:
                if card["lessonid"] == lesson["id"]:
                    mask = card["days"]

                    if mask and day_index < len(mask):
                        if mask[day_index] == "1":
                            lesson_dict = {
                                "subject": get_subject(lesson["subjectid"], dbiAccessorRes),
                                "teacher": [],
                                "period": card["period"],
                                "durationperiods": lesson["durationperiods"]
                            }

                            for teacher in lesson["teacherids"]:
                                lesson_dict["teacher"].append(get_teacher(teacher, dbiAccessorRes))
                            lesson_array.append(lesson_dict)

    return lesson_array