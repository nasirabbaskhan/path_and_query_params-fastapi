from fastapi import FastAPI # type: ignore
import uvicorn # type: ignore

app= FastAPI()


students: list[dict[str, int | str]]= [
    {
    "userName":"nasir Abbas",
     "Roll No":23
     },
    {
    "userName":"ali",
     "Roll No":15
     },
]

@app.get("/getPathVariable")
def gettingParams():
    return "welcom to our new fast api calling"


# getting variable from dynamic path
@app.get("/getPathVariable/{id}")
def gettibgId(id):
    return { 
            "id":id
            } 
    


# getting multiple variables from dynamic path
@app.get("/getPathVariable/{userName}/{rollNo}")
def dettingMultiplesvariable(userName:str,rollNo:int):
    return { 
            "userName": userName,
            "Roll No":rollNo
            } # http://127.0.0.1:8080/getPathVariable/nasir/87
    
    



# getting variable from query params
@app.get("/getQueryParams")
def getQueryparams(id:int):
    return {
        "id":id
        } # http://127.0.0.1:8080/getQueryParams?id=3


# getting multiple variables from query params
@app.get("/getmultipleQueryParams")
def getMultyVariable(userName:str,rollNo:int):
    return { 
            "UserName":userName,
            "Roll No": rollNo
            } # http://127.0.0.1:8080/getmultipleQueryParams?userName=nasir&rollNo=67
    
    
@app.get("/students")
def getStudents():
    return students   # http://127.0.0.1:8080/students

   
#appent the userName and rollno into students list
@app.get("/addStudents")
def getStudent(userName:str,rollNo:int):
    global students
    students.append({"userName":userName,
            "Roll No":rollNo})
    return  {
             "userName":userName,
            "Roll No":rollNo
            
            }  # http://127.0.0.1:8080/addStudents?userName=nasir&rollNo=12
    
  #appent nested path variable  
@app.get("/getStudents/{student_id}/assignment/{assignment_id}")
def nestedValues(student_id:int,assignment_id:int):
    return {
        "student_id":student_id,
        "assignment_id":assignment_id,
        
    } # http://127.0.0.1:8080/getStudents/5/assignment/8
    
# getting both path and query params
@app.get("/getStudents/{student_id}/assignment/{assignment_id}")
def bothValues(student_id:int,assignment_id:int,userName:str,rollNo:int):
    return {
        "student_id":student_id,
        "assignment_id":assignment_id,
        "userName":userName,
        "rollNo":rollNo,
        
    }  # http://127.0.0.1:8080/getStudents/5/assignment/8?userName=nasir&rollNo=66

def start():
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8080, reload= True)
    