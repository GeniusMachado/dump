Write a SQL query to find studenName with highest score in each subject StudentMarks

Student table
Id, student_name, subject_id, marks
1, lily, 1, 65
2 lily, 2, 80
3 lily, 3, 70
4, isabella, 1, 50
5, isabella, 2, 70
6, isabella, 3, 90
7, olivia, 1, 55
8, olivia, 2, 60
9, olivia, 3, 89


Subjects table:
Subject_id, subject_name
1, Maths
2, Science
3, English




select * from student 	groupby marks having count(student_)>1


selct * from (select student.student_name where count(studen_id)>1 order by DESC limit 1 ;




									highest scorer student in Maths | Highest scorer in Science | Highest SCRORER IN English

lily												79														-															65
isabella 										90															91													66




SELECT STUDENT_TABLE.STUDENT_NAME, STUDENT_TABLE.MARKS, SUBJECT_TABLE.SUBJECT_ID FROM STUDENT_TABLE JOIN SUBJECT_TABLE ON STUDENT_TABLE.SUBJECT_ID = SUBJECT_TABLE.SUBJECT_ID GROUP BY 




sample.json file
{
  "id": "6c8b32f9-22a4-44b1-8e31-897d91e3e5bc",
  "isActive": true,
  "balance": 2450.75,
  "age": 28,
  "name": "Alex Mercer",
  "gender": "non-binary",
  "company": "TechInnovate Ltd",
  "email": "alex.mercer@techinnovate.com",
  "phone": "+1 (555) 019-2834",
  "address": {
    "street": "123 Innovation Way",
    "city": "Tech City",
    "state": "CA",
    "zipcode": "94016",
    "coordinates": {
      "latitude": 37.7749,
      "longitude": -122.4194
    }
  },
  "tags": [
    "developer",
    "remote",
    "premium-user",
    "beta-tester"
  ],
  "preferences": {
    "theme": "dark",
    "notifications": {
      "email": true,
      "sms": false,
      "push": true
    },
    "maxDevices": 5
  },
  "loginHistory": [
    {
      "timestamp": "2026-06-01T08:34:21Z",
      "ipAddress": "192.168.1.50",
      "success": true
    },
    {
      "timestamp": "2026-06-02T14:12:05Z",
      "ipAddress": "192.168.1.72",
      "success": true
    }
  ],
  "referredBy": null
}



from fastapi import FastAPI 
import request
import datetime
import JSON
import fastapi.pydantic
import schemas 

app = fastAPI()


class validation(BaseModel):
	name = str
  date = date

@app.get("/home ")
def inputParser(raw_json):
	df = json.jsonify(raw_json)
  








