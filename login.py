import random
import smtplib
import pyfiglet
import getpass
import pymysql
import hashlib
import re
import time
otp = ''.join([str(random.randint(0, 9)) for i in range(8)])


def signin():
    print('Login Page')
    mailentry = input("Your email --> ")

    try:
        passentry = getpass.getpass("Your Password --> ")
        hashed_password = hashlib.sha256(passentry.encode())
        final_password = hashed_password.hexdigest()
    except Exception as error:
        print('Error!! ', error)
    try:
        if mailentry == '' or passentry == '':
            print('Error!! All Fields Are Required')
            return False

        else:

            con = pymysql.connect(
                host='localhost', user='root', password='', database='register')
            cur = con.cursor()
            cur.execute('select * from person where email=%s and mdp=%s',
                        (mailentry, final_password))
            row = cur.fetchone()
            if row == None:
                print('Error!!  Invalid Email or Password')
                return False

            else:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                password = 'xtybuzzpsvcudjuu'
                server.login('projetssigl4@gmail.com', password)
                msg = 'Hello, Your OTP is ' + str(otp)
                sender = 'projetssigl4@gmail.com'
                receiver = mailentry
                server.sendmail(sender, receiver, msg)

                def login():
                    if otpentry == '':
                        print('Error!! All Fields Are Required')
                        return False
                    elif otpentry != otp:
                        print('Error!! Invalid OTP')
                        return False
                    else:
                        print('Success  Welcome')
                        return True

                otpentry = input('OTP Verification --> ')
                x = login()
                server.quit()
                cur.execute(
                    'select username from person where email = %s', mailentry)
                username = cur.fetchone()
            con.close()
            if (x == True):
                print(pyfiglet.figlet_format("Hello "+username[0]))
                time.sleep(2)
                return username[0]
            else:
                return False

    except Exception as e:
        print('Error', f"Error due to: {e}")


def signup():
    print('SignUp Page')
    entryusername = input("Your username --> ")
    entryemail = input("Your email --> ")

    try:
        entrypassword = getpass.getpass("Your Password --> ")
        hashed_password = hashlib.sha256(entrypassword.encode())
        final_password = hashed_password.hexdigest()
    except Exception as error:
        print('Error!! ', error)
    try:
        entryconfirmpassword = getpass.getpass("Confirm Your Password --> ")

    except Exception as error:
        print('Error!! ', error)
    if entryusername == '' or entryemail == '' or \
            entrypassword == '' or entryconfirmpassword == '':
        print('Error!! All Fields Are Required')

    elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+[a-zA-Z0-9.]*\.[a-zA-Z]*$)", entryemail):
        print('Error!! Invalid Email')

    elif entrypassword != entryconfirmpassword:
        print('Error!! Password Mismatch')

    else:
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='', database='register')
            cur = con.cursor()
            cur.execute('select * from person where email=%s', entryemail)
            row = cur.fetchone()
            if row != None:
                print('Error!! User Already Exists')
            else:
                cur.execute(
                    'insert into person (username,email,mdp) values(%s,%s,%s)',
                    (entryusername, entryemail, final_password))
                con.commit()
                con.close()
                print('Success Registration Successful')

        except Exception as e:
            print('Error', f"Error due to: {e}")
