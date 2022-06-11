from asyncio import format_helpers
import re
done=True
while done:
    user_password=input('Enter a password : ')
    if len(user_password)<6 or len(user_password)>16:
        print('Not a valid password')
        continue
    if not re.search('[a-z]',user_password):
        print('Not a valid password')
        continue
    if not re.search('[A-Z]',user_password):
        print('Not a valid password')
        continue
    if not re.search('\d',user_password):
        print('Not a valid password')
        continue
    if not re.search('[$#@]',user_password):
        print('Not a valid password')
        continue
    done=False
    print('Valid Password')
    




