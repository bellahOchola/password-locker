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

def save_credentials(credential):
    '''
    Function that saves an account
    '''
    credential.save_credential()


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

def main():
    print('Heey!!! Welcome to your Password Manager.')
    # print('\n')
    print('To continue enter one of the following.')
    
    print('ca ---- create new account and lo ---login')
    ans = input().lower()
    if ans == 'ca':
        print('Create an Account')
        print('Username:')
        username = input()
        print('password:')
        password = input()
        save_account(create_account(user_name,password))
        print(f'Hello {user_name} your account has been created and your password is {password}')

    elif ans == 'lo':
        print('Enter your username')
        user_name = input()
        print('Enter your password')
        password = input()
        login = find_user(user_name,password)
        if find_user == login:
            print(f'Heey {user_name} , Welcome to your locker account')
    while True:
        print("Use these short codes : cc - create a new credential, vc - view credentials, fc -find a credential, dc -delete a credential, ex -exit the credential list ")
        short_code = input().lower()
        if short_code == 'cc':
            print('New Credential Account')
            print('Enter the account name and password')
            print('Name of account')
            account_name = input()
            print('Your password')
            password = input ()
            print('\n')
            print(f'Your {account_name} account has been successfully created')
            save_credentials(create_credentials(account_name,password))

        elif short_code == 'vc':
            if display_credentials():
                print('Here is a list of your credentials')
                print('\n')
                for credential in display_credentials():
                    print(f'{credential.account_name} ..... {credential.password}')

            else:
                print('\n')
                print("Don't have an account yet")
        
        elif short_code == 'fc':
            print('Enter the name of account you want to search for')
            search_account = input().lower()
            if find_account(search_account):
                search_credential = find_account(search_account)
                print(f'Your {search_account} account  password is: {search_credential.password}')

            else:
                print('That account does not exist.')

        elif short_code == 'dc':
            print('Enter the name of account you want to delete')
            name = input().lower()
            if find_account(name):
                search = find_account(name)
                search.delete_credential()
                print(f'Your {search.account_name} has been deleted')
            else:
                print('That account does not exist')

        elif short_code == 'ex':
            print('See you soon........')
        break        



    



    

if __name__ == '__main__':
    main()