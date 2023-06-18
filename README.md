# XamDiv (still writing it -ron)
A portable and easy to use exam taking device that makes the lives of professors and students easier by streamlining the exam taking process. <br><br>
_[How to setup XamDiv](#installation-and-setup)._

## Functionality
For the XamDiv to work it only needs to be connected to power. Once it is turned on it will autostart all the processes which are required for proper functioning, all that is left to do for students and professors is to connect to XamDiv's network using WiFi. Upon connection to the device, <ins>(the default browser will open the website with the URL www.XamDix.edu)/<ins>.

## Current limitations
Due to time constraints our project has the following limitations:
- The professors can only view submitted exams but not create new ones via the website.
- For creating and starting exams, it is necessary to manually go through the api (it is not implemented within the website).
- Creating an exam with more/less than 5 questions doesn't work.
- The console (compiling the code within the website) works only on Linux and it does not work on Windows (but since everything is hosted on the Raspberry Pi this doesn't matter).

## Technical specification
For creating the project we have used the following technologies: <br>
- **Front-end**: Vue.js, vuetify and axios.
- **Back-end**: Python, fastapi and uvicorn.
- **Webserver**: Nginx.
- **Operating system**: Manjaro.
- **Server**: Raspberry Pi.

## Installation and setup
**Requirements:**
- Python v3.11.4
- Node.js v20.3.0

**Installing the needed Python libraries:** <br>
`pip install fastapi` <br>
`pip install uvicorn` <br>

**Installing the needed Node.js packages:** <br>
`cd front-end` <br>
`cd npm install` <br>

**How to run the back-end:** <br>
`cd back-end/src` <br>
`uvicorn app:app --reload` <br>

**How to run the front-end:** <br>
`cd front-end` <br>
`npm run serve` <br>

**_Note:_** For the above listed commands you have to be in the main directory of the project. <br>

**How to create a new exam:** <br>
To be able to enter an exam as a student, the exam must first be created from the back-end. <br>
1. Start by running the back-end. <br>
2. Afterwards go to **localhost:8000/docs**, there you will find **/api/makeExam** where you will be prompted to create an exam. <br>
3. After creating an exam you will also have an **ExamID**, this ID is needed to log in as a student/professor. <br>

**_Note:_** In the **questionsNotesMarks** variable you have to first write a question then a note and then the marks, delimited using the **\`** symbol. _(Example: "This is question 1\`This is Note 1\`10\`This is question 2\`This is Note 2\`5")_

**How to start an exam:** <br>
After having created an exam you now need to start the exam to be able to enter it. <br>
1. In **localhost:8000/docs** click on **/api/startExam*. <br>
2. In the **Exam_Id** field enter the ExamID which you generated. <br>
3. Using the student IDs which you entered and the ExamID which you generated, you will now be able to log in.
