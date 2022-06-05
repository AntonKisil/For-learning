user_login={'First':'Anton', 'first':'Andrey'}
enter_login=''
while enter_login not in user_login:
    enter_login=input('Enter the login : ')
    print(f"Hello, {user_login[enter_login]}" if enter_login in user_login else 'Invalid login!!!')
    # if enter_login in user_login:
    #     print(f"Hello, {user_login[enter_login]}")
    # else:
    #     print('Invalid login!!!')