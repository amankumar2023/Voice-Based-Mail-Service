################ VOICE BASED EMAIL SERVICE #################

# importing all the necessary library
 
import os                                             # For using environment variable
import smtplib                                        # connect to the mail server
from email.message import EmailMessage                # To send mail
import speech_recognition                             # For converting speech to text                  
import pyttsx3                                        # For converting text to speech  
from tkinter import *                                 # For creating GUI 
import PIL                                            # For image processing
from PIL import ImageTk                                 
from PIL import Image


# EDITH is our voice assistant this function run whenever we want hear from pc

def EDITH(sentence):
    edith = pyttsx3.init()
    edith.setProperty('rate', 135)
    edith.say(sentence)
    edith.runAndWait()
    print(sentence)


# cleaning function filter and add necessary character for an email id

def cleaning(k):
    k = k.replace(" ","")
    k = k.replace("+",".")
    for char in k:
      if(char == '-'):
         k = k.replace("-",d)
         d=char 
    k=k+"@gmail.com"
    print(k)
    return k


# speech_recognizer function to recognised the speech user said

def speech_recognizer():
    recognizer  = speech_recognition.Recognizer()
    while TRUE:
        try:
            with speech_recognition.Microphone() as mic:

                print("recognising: ")
                recognizer.adjust_for_ambient_noise(mic , duration=0.2)
                voice = recognizer.listen(mic)

                content = recognizer.recognize_google(voice)
                content = content.lower()
                print(f"CONTENT: {content}")
                return content
        except:
            EDITH("Voice is not recognised please say louder")
            recognizer  = speech_recognition.Recognizer()
            continue
        


# Storing the user address and password

EMAIL_ADDRESS = os.environ.get('USER')
EMAIL_PASSWORD = os.environ.get('PASSWORD')


# Interface will be executed when the button is click

def Interface():
    EDITH("Hello this EDITH your voice assistant")
    ask = 'no'
    
    while ask == 'no':
        EDITH("Do you want to log in")
        ask = speech_recognizer()
        ask = ask.lower()
        
        if( ask=='yes'):
            msg = EmailMessage()
            m = 'no'
           
            while m == 'no':
                EDITH("Please enter the subject of mail")
                msg['Subject']= speech_recognizer()              # Initialising Subject of the mail
                EDITH("Please enter the body of mail")
                body = speech_recognizer()                       # Initialising body of the mail
                print("subject: " + msg['subject'])
                print("body :" + body)
                EDITH("subject is")
                EDITH(msg['subject'])
                EDITH("body is")
                EDITH(body)
                EDITH("Is subject and body is correct")          # Check weathar the body and subject is correct 
                m = speech_recognizer()                          # if not than process repeat again 
                m= m.lower()
                
                if(m=='yes'):
                    m = 'yes'
                else:
                    print ("please repeat  the  process again")
                    m = 'no'
            msg.set_content(body)
            msg['From']=EMAIL_ADDRESS                           # Initialising the email address of user
            m='no'
           
            while m == 'no':               
                EDITH("reciever id is :")
                reciever_id=speech_recognizer()                 # Initialising the email address to whom user want to send mail
                EDITH(reciever_id)
                EDITH("Is reciever id is correct")              # Check weathar the reciever email id is correct 
                m = speech_recognizer()                         # if not than process repeat again 
                m= m.lower()
                
                if(m=='yes'):
                    m = 'yes'
                else:
                    print ("please repeat  the  process again")
                    m = 'no'
            
            if(reciever_id == 'myself'):
                msg['To']='aman.pearls.01@gmail.com'
            else :
                msg['To'] = cleaning(reciever_id)                   # filter and add necessary character for an email id
            EDITH("do you want to send this email")
            p = speech_recognizer()
            p= p.lower()
            
            if(p == 'yes'):
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:    # Using a secure connection
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)   # logged in

                    smtp.send_message(msg)                       # mail send
                    EDITH("mail send succesfully")
                    print("Mail send succesfully")
                    ask = 'no'
            else:
                print("Mail is not send")
                ask = 'no'
        else:
            ask='yes'
            EDITH("HAVE A NICE DAY")



GUI= Tk()
GUI.title("Voice_Based_Mail_Service")                           # Title of the page of size 626*375
GUI.geometry("626x375")                                         


# importing jpf file stored in download folder

img= ImageTk.PhotoImage(Image.open("C://Users//user//Downloads//voices.jpg"))    
label = Label(image=img)
label.pack()

print("GUI EXECUTED")


# creating button with some customization

button = Button(GUI, text="Speak", padx=20, pady=30 , fg='RED', bg ='BLACK',command=Interface)   
button.place(x= 272, y= 139)       # giving the location of the button

GUI.mainloop()                    # infinte loop used to run the application