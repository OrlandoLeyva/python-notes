# notes application. register and login system.
#TODO: modify all the init message system.

from termcolor import colored, COLORS

from auth import auth
from models import users
from notesSystem import notesHandler
from database.queries import duplicateEmailMessage

authService = auth.Auth()

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

while True:
   if request == 'register':
         authService.register()
         init(initialMessage)

   if request == 'login':
      userData = authService.login()
            # return users.User(userData[1], userData[2], userData[3])
      user = users.User(userData[1], userData[2], userData[3]) 
      user.selectAction(userData[0])

   if request == 'exit':
      exit('Bye')

   if not request in ['register', 'login', 'exit']:
      print(colored('\nselect an available action', 'red'))
      init(initialMessage)