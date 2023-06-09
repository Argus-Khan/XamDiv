from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
import os, subprocess

app = FastAPI()

class Test(BaseModel):
    Std_Id: str
    Q_Num: int
    Code: str



# def compileSrc(Src: str):
#     cmd = "g++ " + Src +" -o exec"
#     CompileProcess = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     output, err = CompileProcess.communicate()
#     if (output.len > 1 ):
#         return output
#     else:
#         return "Successfully Compiled"

@app.get("/api/login")
def home():
    return {"Data":"Heya!"}

@app.get("/api/exam")
def exam():
    return {"Data": os.getcwd()}

@app.post("/compileTest")
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

