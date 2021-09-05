#!/usr/bin/env python3.8
from credential import Credential
from user import User
import random


#credentials

def create_credentials(fname,lname,user_name,password,email):
    '''
    Function for creating new credential
    '''
    new_credential = Credential(fname,lname,user_name,password,email)
    return new_credential


def save_credential(credential):
    '''
    Function that saves credential
    '''
    credential.save_credential()


def delete_credential(credential):
    '''
    Function that deletes credential
    '''
    credential.delete_credential()



def find_credential(email):
    '''
    Function that finds credential by email
    '''
    return Credential.find_email(email)



def checking_existing_credentials(email):
    '''
    Function that check if credentials exists with that email and return a Boolean
    '''
    return Credential.credential_exit(email)



def display_credential():
    '''
    Function that return all saved credential
    '''
    return Credential.display_credential()


#user

def create_user(user_name,email,password):
    '''
    function of creating new user
    '''
    new_user = User(user_name, email, password)
    return new_user


def save_user(user):
    '''
    Function that saves user details
    '''
    user.save_user()


def display_user():
    '''
    Function that displays user
    '''
    return User.display_users()

def main():
    print("Hi There!! Welcome to Password Locker, Have fun!!!  \n")
    
    while True:
        print( "\n Choose an option below to proceed: \n \n cc - create account with a user_defined password \n dc - display credential \n cg -create account with" 
              " auto-generated password \n ex -exit \n") 
        short_code = input().lower()

        if short_code == "cc":
           
            print("=" * 25)
            print("Enter account name:")
            acc = input()
                                        
            print("Enter your First name ....")
            fname = input()

            print("Enter your Last name ...")
            lname = input()

            print("Enter your username ...")
            user_name = input()

            print("Enter your email Address ...")
            email = input()

            print("Enter your password")
            password = input()

            save_user(create_user(user_name, email, password))
            save_credential(create_credentials(fname, lname, user_name, password, email))
            print("\n")
            print(f"A new {acc} account by {fname} has successfully been created")
            print(f"username :{user_name} \npassword :{password}")
            print("\n")
        elif short_code == "dc":

            if display_credential   ():
               print("Here is a list of all your user credentials accounts")
               print("\n")

               for credentials in display_credential():
                   print(f" \nFirst name : {credentials.first_name}\nLast name : {credentials.last_name}\nUser name : {credentials.user_name} \nAccount name : {acc}")
               print("\n")
            else:
                print("\n")
                print("It looks like no account credentials exist at the moment. Consider creating one or more ")
                print("\n")

        elif short_code == "cg":
            print("New user")
            print("-" * 10)
            print("Enter account name:")
            acc = input()
            print("********************************")

            print("Enter your First name: ")
            fname = input()

            print("Enter your Last name :")
            lname = input()

            
            print("Email Address ...")
            email = input()

            print("Enter your username ...program will generate a password for you")
            user_name = input()

            password_generator = "12345678910!@#$%^&*()+-?><abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            password = "".join(random.sample(password_generator, 8))
            print("\nnew account created with generated Password")

            save_user(create_user(user_name, email, password))
            save_credential(create_credentials(fname, lname, user_name, email, password))
            print("\n")
            print(f"Username :{user_name}  \nPassword :{password}")
            print("\n")
        elif short_code == "ex":                
            print("thank you and welcome")
            break
        else:
            print("Invalid command")

if __name__ == '__main__':
    main()

