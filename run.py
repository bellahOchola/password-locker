#!/usr/bin/env python3.6
from password import *

def create_account(user_name, password):
    '''
    function to create a new account
    '''
    new_user = User(user_name, password)
    return new_user

def save_account(user):
    '''
    Function that saves an account
    '''
    user.create_account()

def find_user(user_name, password):
    '''
    function that checks if the user exists
    '''
    return User.login(user_name, password)

def create_credentials(account_name, password):
    '''
    function that create accounts credentials
    '''
    new_credential = Credentials(account_name, password)
    return new_credential

def display_credentials():
    '''
    function returns all saved credentials
    '''
    return Credentials.display_credentials()

def delete_credential(credential):
    '''
    function that deletes accounts credentials
    '''
    credential.delete_credential()

def find_account(account_name):
    '''
    function that takes in an account name and returns password
    '''
    return Credentials.find_by_accountname(account_name)

