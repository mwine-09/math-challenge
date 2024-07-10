Mathematics Challenge System

Overview

The Mathematics Challenge System is developed to organize and manage a national mathematics competition for primary school children. It provides an integrated platform for administrators, school representatives, and participants to streamline registration, challenge management, and reporting processes. The system includes both a web interface and a command-line interface for comprehensive user interaction.

Features

School Registration
Admin Functionality: Administrators can upload schools into the system, including:
	School name
	District
	School registration number
	Email of representative
	Name of representative
Validation: School representatives must be validated before registration is completed.

Question Management
	Excel Uploads: Administrators upload questions and answers via Excel documents:
	questions.xlsx: Contains the challenge questions.
	answers.xlsx: Contains the corresponding answers and marks.
	Random Selection: For a 10-question challenge, 100 questions are uploaded to ensure each attempt presents a unique set of random questions.


Challenge Setup
	Parameters: Administrators set parameters for each challenge, including:
	Open and close dates
	Duration of the challenge
	Number of questions presented in each attempt
	Participation: Participants can log in and attempt the challenges during the open period.
 
Participant Registration
CLI Registration: Pupils register using the command line interface with the following details:
	Username
	First name
	Last name
	Email address
	Date of birth
	School registration number
	Image file (e.g., image_file.png)
Instructions Menu: Provides detailed instructions for registration, viewing challenges, and participation.

School Representative Confirmation
Confirmation Process: Representatives confirm or reject participants via the command line interface.
	Accepted participants are added to the database.
	Rejected participants are moved to a rejected table and are prevented from re-registering under the same school.

Challenge Participation
Viewing Challenges: Participants can view all valid challenges.
Attempting Challenges: Participants can attempt challenges:
	Random questions are presented one by one with time tracking.
Marks are awarded or deducted based on the answers provided.
Completion Report: Upon challenge completion, participants receive a PDF report via email detailing their performance.

Automated Reporting
End-of-Challenge Reports: Automatic generation and emailing of performance reports to participants.
Recognition: The top two winners are recognized on the website.

Analytics and Reporting
Performance Insights:
	Most correctly answered questions.
	School rankings.
	Performance tracking over time.
	Question repetition percentage.
	Lists of best and worst-performing schools.
	Participants with incomplete challenges.
	Additional reports for project value enhancement.
