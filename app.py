# notes application. register and login system.
#TODO: welcome message when you login.

import colorama
from colorama import Fore

from auth import authService
from notesSystem import notesHandler

initialMessage = '''
Available actions

- register
- login
- exit
'''

attempts = 0
loginAttempts = 0

# handling

def init(message):
   global request
   print(message)
   request = input('What do you want to do? ').lower().strip()

init(initialMessage)

while request != 'exit':
   if request == 'register':
      if not attempts == 3:
         userCredentials = authService.GetCredentials(request)

         try:
            authService.register(userCredentials['username'], userCredentials['email'], userCredentials['password'])
            print('¡Successfully registered!')
            print('---------------')
            init(initialMessage)
         except ValueError as e:
            print('----------------')
            print(str(e))
            attempts += 1

         except Exception as e:
            print('Internal error')

      else:
         print('3 incorrect attempts')
         init(initialMessage)
         attempts = 0

   elif request == 'login':
      if not loginAttempts == 3:
         userCredentials = authService.GetCredentials(request)
         try:
            user = authService.login(userCredentials['email'], userCredentials['password'])
            print(f"\nwelcome, {user['username']}. Let's get started")
            notesResult = notesHandler(user['id'])
            if notesResult == 'exit':
               request = 'exit'
         except ValueError as e:
            print('---------------')
            print(str(e))
            loginAttempts += 1
         except Exception as e:
            print('Internal error')
            request = 'exit'
      else:
         print('3 incorrect attempts')
         init(initialMessage)
         loginAttempts = 0

   elif len(request) == 0:
      print('Any action selected')
      print('--------------')
      init(initialMessage)

   else:
      print('select an available action')
      print('--------------')
      init(initialMessage)

print(Fore.CYAN + 'Bye')