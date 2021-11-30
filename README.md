# Fraud_Image_Capturing
This is an desktop application which is used to capture the person who is trying to falsly accessing your account and send that picture to the registered email in the database for the correponding username
Main Requirements:
1.Text editor(pycharm Recommended)
2.local server(any local server wamp recommended)
3.PIP must be installed

Step:1
1.Install any local server(Wamp Server) in your local System 
2.Create a database and  a table in it with the following feilds(username,password,email)
3.insert the values into that database
  The table looks like this :
  |-------------|------------|---------------|
  | Username    | password   |     email     |     
  |-------------|------------|---------------|
  |             |            |               |
  |             |            |               |
  |-------------|------------|---------------|
Step:2
In order to make your application work the following to be installed into your system
1.Install mysql connector in order to connect your application to your local server wamp
  you can use pip to install mysql connector like-"pip install mysql-connector-python"
2.Install opencv inorder to capture the image of the person if he/she fails to attempt the correct password for three times
  you can install opencv using the command="pip install opencv-python"

Step:3
A)Login_module:
    1.In login module you need to initially install the mysql connector using the command mentioned above
    2.Install the opencv in the terminal
    3.To connect your application to the database created in wamp server we use 
           sql.connect(host='localhost',port=3308,database='project',user='root',passwd='')
                1.port number should be the port alloted to your mysql
                2.database should be the database name you created in mysql
                3.user should be 'root' and password should be empty by default
     4.This module allows you to login with your credentials ,if anyone fails to enter the correct password for three onsecutive times then camera_module captures the picture of that person
 B)Camera_module:
    1.the camera module runs after the login_module
    2.This module captures the picture of the person who is failing to enter the password for three consecutive times and stores in the jpg file
 C)email_module:
    1.In this module the captured photo will be send to the registered email of coressponding username
    2.In email_module the following line of code changes ,you need to create an mail id and provide that mail Id and password
           ---server.login("createnewmail@gmail.com","mail_password")
    3.In that mail account under account-->settings-->enable less secure app access permission
 now you can see the picture of that person in the mail of corresponding username
       
                
            
               



