#importing the Yagmail library
import yagmail

try:
    #initializing the server connection
    yag = yagmail.SMTP(user='testingpyp@gmail.com', password='Test_1234')
    #sending the email
    yag.send(to='sabarishsabarish244@gmail.com', subject='Machine Learning Model Details', contents='Congratulations Model Built Successfully!')
    print("Email sent successfully")
except:
    print("Error, email was not sent")
    
