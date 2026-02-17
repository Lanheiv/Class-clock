from datetime import datetime, timedelta

from functions.file_function import *
from functions.session_function import * 

delete_files()

url = "https://pteh.edupage.org"
paths = [
    'scoper/files/raw/TTViewerData.json',
    'scoper/files/raw/mainDBIAccessor.json',
    'scoper/files/raw/'
]

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    "Origin": url,
    "Referer": url + "/"
}
TTViewerData = [
    "/timetable/server/ttviewer.js?__func=getTTViewerData",
    {"__args":[None,2025],"__gsh":"00000000"}
]

result = get_post_data(url, headers, TTViewerData)
write_file(paths[0], result)

data = json.loads(read_file(paths[0]))
timetables = [{"default_num": data["r"]["regular"]["default_num"]}, []]
for f in data["r"]["regular"]["timetables"]:
    timetables[1].append({"tt_num": f["tt_num"], "year": f["year"]})

today = datetime.today()
monday = today - timedelta(days=today.weekday())
sunday = monday + timedelta(days=6)
date = [monday.strftime("%Y-%m-%d"), sunday.strftime("%Y-%m-%d")]

mainDBIAccessor = [
    "/rpr/server/maindbi.js?__func=mainDBIAccessor",
    {"__args":[None,2025,{"vt_filter":{"datefrom":date[0],"dateto":date[1]}},{"op":"fetch","needed_part":{"teachers":["short","name","firstname","lastname","callname","subname","code","cb_hidden","expired"],"classes":["short","name","firstname","lastname","callname","subname","code","classroomid"],"classrooms":["short","name","firstname","lastname","callname","subname","code"],"igroups":["short","name","firstname","lastname","callname","subname","code"],"students":["short","name","firstname","lastname","callname","subname","code","classid"],"subjects":["short","name","firstname","lastname","callname","subname","code"],"events":["typ","name"],"event_types":["name","icon"],"subst_absents":["date","absent_typeid","groupname"],"periods":["short","name","firstname","lastname","callname","subname","code","period","starttime","endtime"],"dayparts":["starttime","endtime"],"dates":["tt_num","tt_day"]},"needed_combos":{}}],"__gsh":"00000000"}
]

result = get_post_data(url, headers, mainDBIAccessor)
write_file(paths[1], result)

for f in timetables[1]:
    regularttGetData = [
        "/timetable/server/regulartt.js?__func=regularttGetData",
        {"__args":[None, f["tt_num"]], "__gsh":"00000000"}
    ]

    result = get_post_data(url, headers, regularttGetData)

    regularttGetData_path = f'{paths[2]}regularttGetData_{f["tt_num"]}.json'
    write_file(regularttGetData_path, result)






















"""
for n in data[:-1]:
    result = session.post(
        url + n[0],
        headers=headers,
        json=n[1],
    )

    with open('scoper/files/raw/data.json', 'w') as f:
        json.dump(result.json(), f)

print("Status:", result.status_code)

data = result.json()
print(json.dumps(data, indent=2))

data = json.loads(data)
for item in data["r"]["regular"]["timetables"]:
    print("tt_num:", item["tt_num"])
    print("year:", item["year"])

    len(data["r"]["regular"]["timetables"])

#print("Status:", result.status_code)
#print("Cookies:", session.cookies.get_dict())

#data = result.json()
#print(json.dumps(data, indent=2))
"""