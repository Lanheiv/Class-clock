from datetime import datetime, timedelta
import traceback
import sys

from functions.file_function import *
from functions.session_function import * 
from functions.formatting_function import * 

delete_files()

data_url = "https://pteh.edupage.org"

TTViewerData_path = "scoper/files/raw/TTViewerData.json"
mainDBIAccessor_path = "scoper/files/raw/mainDBIAccessor.json"
raw_path = "scoper/files/raw/"

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    "Origin": data_url,
    "Referer": data_url + "/"
}
TTViewerData = [
    "/timetable/server/ttviewer.js?__func=getTTViewerData",
    {"__args":[None,2025],"__gsh":"00000000"}
]

try:
    result = get_post_data(data_url, headers, TTViewerData)
    if not result:
        write_errore_file("TTViewerData request returned empty")
        sys.exit()

    write_file(TTViewerData_path, result)
except Exception:
    write_errore_file(traceback.format_exc())
    sys.exit()

data = json.loads(read_file(TTViewerData_path))
timetables = [{"default_num": data["r"]["regular"]["default_num"]}, []]
for fordata in data["r"]["regular"]["timetables"]:
    timetables[1].append({"tt_num": fordata["tt_num"], "year": fordata["year"]})

today = datetime.today()
monday = today - timedelta(days=today.weekday())
sunday = monday + timedelta(days=6)
date = [monday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")]

mainDBIAccessor = [
    "/rpr/server/maindbi.js?__func=mainDBIAccessor",
    {"__args":[None,2025,{"vt_filter":{"datefrom":date[0],"dateto":date[1]}},{"op":"fetch","needed_part":{"teachers":["short","name","firstname","lastname","callname","subname","code","cb_hidden","expired"],"classes":["short","name","firstname","lastname","callname","subname","code","classroomid"],"classrooms":["short","name","firstname","lastname","callname","subname","code"],"igroups":["short","name","firstname","lastname","callname","subname","code"],"students":["short","name","firstname","lastname","callname","subname","code","classid"],"subjects":["short","name","firstname","lastname","callname","subname","code"],"events":["typ","name"],"event_types":["name","icon"],"subst_absents":["date","absent_typeid","groupname"],"periods":["short","name","firstname","lastname","callname","subname","code","period","starttime","endtime"],"dayparts":["starttime","endtime"],"dates":["tt_num","tt_day"]},"needed_combos":{}}],"__gsh":"00000000"}
]

try:
    result = get_post_data(data_url, headers, mainDBIAccessor)

    if not result:
        write_errore_file("mainDBIAccessor request returned empty")
        sys.exit()

    write_file(mainDBIAccessor_path, result)
except Exception:
        write_errore_file(traceback.format_exc())
        sys.exit()

for fordata in timetables[1]:
    regularttGetData = [
        "/timetable/server/regulartt.js?__func=regularttGetData",
        {"__args":[None, fordata["tt_num"]], "__gsh":"00000000"}
    ]

    try:
        result = get_post_data(data_url, headers, regularttGetData)

        if not result:
            write_errore_file(f"regularttGetData {fordata["tt_num"]} request returned empty")
            sys.exit()

        regularttGetData_path = f'{raw_path}regularttGetData_{fordata["tt_num"]}.json'
        write_file(regularttGetData_path, result)
    except Exception:
            write_errore_file(traceback.format_exc())
            sys.exit()

raw_data_formatting()