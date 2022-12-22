# notes application. register and login system.

from auth import authService

initialMessage = '''
Available actions

- register
- login
'''

print(initialMessage)

answer = input('What do you want to do? ').lower()

if answer == 'register':
    username = input('Insert your username: ').strip()
    email = input('Insert your email: ').strip()
    password = input('Insert your password: ').strip()
    result = authService.register(username, email, password)
    print(result)
