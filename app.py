# notes application. register and login system.

import colorama
from colorama import Fore

from auth import authService

initialMessage = '''
Available actions

- register
- login
- exit
'''

attempts = 0

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
      userCredentials = authService.GetCredentials(request)
      result = authService.login(userCredentials['email'], userCredentials['password'])
      print(type(result))

   elif len(request) == 0:
      print('Any action selected')
      print('--------------')
      init(initialMessage)

   else:
      print('select an available action')
      print('--------------')
      init(initialMessage)

print(Fore.CYAN + 'Bye')