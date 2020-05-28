#importing the Yagmail library
import yagmail

try:
    #initializing the server connection
    yag = yagmail.SMTP(user='your email', password='your pwd')
    #sending the email
    yag.send(to='srank2000@gmail.com', subject='Machine Learning Model Details', contents='Congratulations! Model Built Successfully!')
    print("Email sent successfully")
except:
    print("Error, email was not sent")
    
