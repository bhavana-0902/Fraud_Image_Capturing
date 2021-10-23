import mysql.connector as sql
import cameramodule
import emailmodule
db=sql.connect(host='localhost',port=3308,database='project',user='root',passwd='')
mc=db.cursor()
a=input("enter the user name")
mc.execute("select email from users where username='"+a+"';")
for i in mc:
    z=i[0]
mc.execute("select password from users where username='"+a+"';")
for i in mc:
    x=i[0]
    for j in range(3):
        y=input("enter the password")
        if(y==x):
            print("login successful")
            flag=1
            break
        else:
            print("login unsuccessful")
            print("try again")
            flag=0
    if(flag==0):
        cameramodule.cameraon()
        emailmodule.email_code(z)
        break

