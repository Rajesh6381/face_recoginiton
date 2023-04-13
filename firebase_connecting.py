import firebase_admin
from firebase_admin import db


from datetime import datetime



# firebase connecting
def firebase_connectings(key):
    print("databse started")
    if not firebase_admin._apps:
        cred_obj = firebase_admin.credentials.Certificate('attendance-34c91-firebase-adminsdk-n1vj8-18f67ea82c.json')
        default_app = firebase_admin.initialize_app(cred_obj,{
            'databaseURL': 'https://attendance-34c91-default-rtdb.firebaseio.com/'
        })

    #  the root of the database
    ref = db.reference("/")

    #To get the data using keys
    f = ref.child(str(key)).get()

    # To get the current data
    date = str(datetime.now().strftime("%d-%m-%Y"))

    attendanceList =[]

    for i in f['Attendance']:
        attendanceList.append(i['Date'])

    print(attendanceList)

    if(str(date) not in attendanceList):
        #append the status to the existing data
        f['Attendance'].append({'AttendanceStatus': 'p', 'Date': date})

        print(f)

        #After appending to update the database
        ref.child(str(key)).update(f)

        print(key,"key  is successfully update data in database")

    else:
        print(key ," The key  is already in database")


    # open the json data and set
    #with open("data.json", "r") as f:
    #    file_contents = json.load(f)

    # update the data in realtime database  --> update , child , remove , get
    #ref.set(file_contents)
