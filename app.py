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

def init(message):
   global request
   print(message)
   request = input('What do you want to do? ').lower().strip()

init(initialMessage)

while request != 'exit':
   if request == 'register':
      userCredentials = authService.GetCredentials(request)
      result = authService.register(userCredentials['username'], userCredentials['email'], userCredentials['password'])

      if type(result) == Exception:
            print(Fore.RED + str(result))
            init()
      else: 
         print(Fore.GREEN + '¡Successfully registered!')
         # init()

   elif request == 'login':
      userCredentials = authService.GetCredentials(request)
      result = authService.login(userCredentials['email'], userCredentials['password'])
      print(type(result))

   # elif request == 'exit':
   #    print(Fore.CYAN + 'Bye')

   elif len(request) == 0:
      print(Fore.CYAN + 'Any action selected')

print(Fore.CYAN + 'Bye')