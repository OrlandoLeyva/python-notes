# notes application. register and login system.

from colorama import Fore, Style
from termcolor import colored, COLORS

from auth import authService
from notesSystem import notesHandler
from database.queries import duplicateEmailMessage

initialMessage = colored('''
Available actions

- register
- login
- exit
''', 'cyan')

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
            print(colored('¡Successfully registered!', 'green'))
            print('---------------')
            init(initialMessage)
         except ValueError as e:
            print('----------------')
            if str(e).startswith(duplicateEmailMessage):
               print(colored('Email already taken', 'red'))
               print()
            else:
               print(e)
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
            print('---------------')
            print(colored(f"\nwelcome, {user['username']}. Let's get started", 'green'))
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