# team2-Question-Library

WayScript Approach

WayScript is a “drag and drop programming platform” that lets users build programs while it takes care of third party APIs and allows cloud access.

How The Question Bank Works
The approach is simple, you add questions to the bank and instructors will add solutions to those challenges. You can also have access to the Question Bank or if you need help, it will walk you through the guidelines.

The Architecture

The main function has a token that is triggered when ever a text is passed to the slack channel. There are specific guidelines for adding questions, answers, or inquiring for help, which are indicated later in the documentation. 





That text is then going to be split based on a special character (~). If 
Based on the first character, it is going to take the logic of either being processed as a question or an answer. If it is a question or an answer, it is then going to be added to the CSV where it is stored. A confirmation message will be sent from WayScript to the channel. If the input is asking for the CSV, “SHOW”, then an email is going to be sent to the admin and the email address of the user is going to be added into another CSV to later be addressed by the admin. This is in the Beta version of WayScript, once access is granted for it from google accounts, it will be able to automatically send the question bank (the CSV) to users email. If the input is asking for help, “HELP”, then a message that describes the guidelines to use the app is displayed from the WayScript bot to the channel. 
ADD                 SHOW    HELP

Writing Guidelines:

Adding a Question:       Q ~'ID' ~'Week#' ~'Topic' ~'Question'
Adding a Solution:         A ~'ID' ~'Week' ~'Topic' ~'Link to codeshare containing the answer code'
Inquiring for the bank:   Show~ ‘Your name’ ~ ‘email_address'
Inquiring for help:          Help
