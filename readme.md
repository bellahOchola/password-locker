# Password Locker.
#### This application enables user access their password credentials 10/11/2019
#### bellahOchola
## Description
This application enables user login to the site or simply create an account if they do not have any. After logging in they are given options of viewing their already existing credentials,creating a new  credential account , finding the content of an account using that accounts name or simply deleting their credentials if they no longer need them.
## Setup/Installation Requirements
* open the terminal in your desktop
* navigate to where you want to save the folder
* go back to github 
* clone this repo to your pc
* run it on the terminal.
## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./run.py```|Hello Welcome to your Accounts Password Store... <br>* CA ---  Create New Account * LO ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LO  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```DC```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```EX```| The application exits|
## Technologies Used
* Python - used in the building of tests and classes.
## Support and contact details
If in any case you come across any isssues when using this application, kindly contact me. Incase of any contributions too just reach out @ [bellahkenya@gmail.com]
### License
This project is under the MIT license
Copyright (c) 2019  
Christabel ochola