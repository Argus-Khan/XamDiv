# XamDiv
## Project idea

A "secure" portable exam taking device (XamDiv) where the professor plugs it in and the device does the rest.

## User Interface

[DEMO](https://www.figma.com/proto/UfVC45NWZMSGn9mdEnhyEO/XamDiv?type=design&node-id=9-88&scaling=min-zoom&page-id=7%3A15&starting-point-node-id=9%3A88) |
[Detailed view](https://www.figma.com/file/UfVC45NWZMSGn9mdEnhyEO/XamDiv?type=design&node-id=7%3A15&t=cKvBjVW5s9DpsngA-1)

## Functionality
- The users (professors and students) can connect to the device's network (Wi-Fi) and access the XamDiv webapp.
- Students can take exams on the webapp.
- Professors can create, delete, modify, view and conduct exams. 
 
## Technical specifiction

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
