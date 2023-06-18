# XamDiv (still writing it -ron)
A portable and easy to use exam taking device (abbreviated to XamDiv) that makes the lives of professors and students easier by streamlining the exam taking process. <br>
_[How to setup XamDiv](https://github.com/Argus-Khan/XamDiv/tree/main#installation-and-setup)._

## Functionality
For the XamDiv to work it only needs to be connected to power. Once it is turned on it will autostart all the processes which are required for proper functioning, all that is left to do for students and professors is to connect to XamDiv's network using WiFi. Upon connection to the device, <ins>(the default browser will open the website with the URL www.XamDix.edu)/<ins>.

## Current limitations
- The professors can only view submitted exams but not create new ones via the website.
- For creating and starting exams, it is necessary to manually go through the api. It is not implemented within the website.
- Creating an exam with more/less than 5 questions doesn't work.
- The console (Compiling the code within the website) works only on Linux and it does not work on Windows (but since everything is hosted on the Raspberry Pi this doesn't matter).

## Technical specification

## Installation and setup
Requirements:
- Python (VERSION)
- Node.js (VERSION)
- Vue CLI (VERSION)

**Installing the needed python libraries:** <br>
`pip install fastapi` <br>
`pip install uvicorn` <br>

<ins>**MAYBE ADD A VENV**</ins>

**How to run the front-end:** <br>
`cd front-end` <br>
`npm run serve` <br>

**How to run the back-end:** <br>
`cd back-end/src` <br>
`uvicorn app:app --reload` <br>

**How to create a new exam**
To be able to enter as a student




**Login screen** _(LANDING PAGE)_

- As soon as a user connects to the webapp, they can log in using their username.
- Students use their student ID to connect to an exam session, only one exam session per student ID.
- Professors can log in with their username, after which they have to use their password (which they create themself).
 
**Student portion**

- Initially the student should be prompted with the main note from the professor (implemented as a pop-up).
- Questions and the exam are going to be split view initially, but either window can take the whole viewport at any time.
- Timer should be on the exam and starts counting down as soon as the main note is closed (when counter hits 0, auto-submit the code and the login session is deleted).
 
**Professor portion**

- Professor can create an exam, meaning: Main note, exam questions, schedule (date/time), student attending list and exam time.

## Video ideas
- 80/90's advertisement vibe.

## OPTIONAL STUFF

A) Past exams
- View student submissions.
- View their marks.
- Modify student data (modify marks, etc).

B) Exam creation and modification
- Create new exams.
- Modify already existing exams.
- Generate passwords for that particualar exam session (student selection is given)

C) Conducting exam
- Exams should be scheduled / or not.
- Professor has access to the counter.

- Automatically open the device page on connection to the network.
- Have multiple exams (ideally).
