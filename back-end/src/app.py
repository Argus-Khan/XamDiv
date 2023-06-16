from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from datetime import datetime
import os, subprocess, json, random, string, hashlib

app = FastAPI()

class Test(BaseModel):
    Exam_Id: str
    Std_Id: str
    Q_Num: int
    Code: str

class Exam(BaseModel):
    professor: str
    date: str
    marks: int
    time: int
    triesAllowed: int
    studentsIds: str

def match_token():
    pass

def hash_pass(pswd):
    hs = hashlib.new("SHA256")
    hs.update(pswd.encode())
    return hs.hexdigest()

@app.get("/api/Stdlogin")
def home(Std_Id: str , Exam_Id: str):
    Exam_Dir = os.path.abspath('..')+"/database/Exams_Data/"+Exam_Id
    if(os.path.exists(Exam_Dir)):
        with open(Exam_Dir+"/Students.json","r") as xd:
            Std_Data = json.loads(xd.read())
            if Std_Id in Std_Data:
                token = hash_pass(str(datetime.now()))
                Std_Data[Std_Id]["Access_Token"] = token
                with open(Exam_Dir + "/Students.json", "w") as  xd:
                    json.dump(Std_Data, xd)
                return {"Response":"GoodLuck!" , "AccessToken" : token}
            else:
                return {"Response": "Invaild Student ID"}
    else:
        return {"Response": "Invaild Exam ID"}


@app.get("/api/getExam")
def exam(Exam_Id: str):
    Exam_Dir = os.path.abspath('..')+"/database/Exams_Data/"+Exam_Id
    if(os.path.exists(Exam_Dir)):
        with open(Exam_Dir+"/Exam.json","r") as xd:
            return json.loads(xd.read())
    else:
        return {"Response": "Invaild Exam ID"}


@app.post("/api/makeExam")
def makeExam(Crnt_Exam : Exam):
    s = string.ascii_lowercase+string.digits
    ExamId = "".join(random.sample(s,5))
    Exam_Dir = os.path.abspath('..')+"/database/Exams_Data/"+ExamId
    while(os.path.exists(Exam_Dir)):
        ExamId = "".join(random.sample(s,5))
        Exam_Dir = os.path.abspath('..')+"/database/Exams_Data/"+ExamId
    os.makedirs(Exam_Dir)

    students_list = Crnt_Exam.studentsIds.replace(" ","")
    students_list = students_list.split(',')
    students_data = {}


    for std in students_list:
        os.makedirs(Exam_Dir+"/"+std)
        students_data[std] = {"attended" : False , "marks": 0 , "Questions_Attemped": 0 , "Status": "Not attemped", "Time_Taken":0, "Access_Token" : "", "Additioanl_time_awarded" : 0}

    Crnt_Exam.studentsIds = students_list
    Crnt_Exam = dict(Crnt_Exam)

    with open(Exam_Dir + "/Students.json", "w") as  xd:
        json.dump(students_data, xd)

    with open(Exam_Dir + "/Exam.json", "w") as  xd:
        json.dump(Crnt_Exam, xd)

    return {"Response": "Exam made successfully", "ExamID" : ExamId}


@app.post("/api/compileTest")
def compileTest(Crnt_Test : Test):
    Compile_Dir = str(os.path.abspath('..'))+"/answers/" + Crnt_Test.Std_Id
    if not os.path.exists(Compile_Dir):
        os.makedirs(Compile_Dir)
    Crnt_Src = Compile_Dir+"/Q"+str(Crnt_Test.Q_Num)+".cpp"

    with open(Crnt_Src,"w") as fl:
        fl.write(Crnt_Test.Code)

    cmd = "g++ '" + Crnt_Src + "'"

    output = subprocess.run(cmd,shell=True,capture_output=True)
    if (output.stderr):
        return {"Response": output.stderr}
    else:
        return {"Response": "Successful Compile"}

