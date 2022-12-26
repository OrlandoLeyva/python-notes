from database import queries


availableActionsMessage = '''
Available actions

- create note (create)
- show notes (show)
- remove note (remove)
- exit
'''

emptyRequestMessage = '''
any action selected, try again

Available actions

- create note (create)
- show notes (show)
- remove note (remove)
- exit
'''

def actionsMessage(message):
    print(message)
    global request
    request = input('What do you want to do?: ').lower().strip()

def notesHandler(userId: int):
    actionsMessage(availableActionsMessage)

    while request != 'exit':
       # print('request: ', request)
        if request == 'create':
            print('Creating a new note...')
            note = createNote(userId)
            if not note:
                actionsMessage(availableActionsMessage)
            else:
                try:
                    queries.insertNote(note)
                    print('\n'+ 'Note successfully created')
                    actionsMessage(availableActionsMessage)
                except Exception as e:
                    print(e)
                    availableActionsMessage(actionsMessage)

        if request == 'show':
            showNotes(userId)
            actionsMessage(availableActionsMessage)

        if request == 'remove':
            removeNote()
            actionsMessage(availableActionsMessage)

        if request == 'exit':
            return 'exit'

        if len(request) == 0:
            actionsMessage(emptyRequestMessage)

        else:
            print('select an available action')
            print('--------------')
            actionsMessage(availableActionsMessage)
    return 'exit'

# Returns a the note If it was successfully created or False If it wasn't. 
def createNote(userId: int):
    attempts = 0
    note = {}

    while attempts < 3:
        global titleIsCreated
        titleIsCreated = False
        title = input('Type the title: ')
        if valueIsEmpty(title):
            print('\n'+ 'Title cannot be empty')
            attempts += 1
        else:
            titleIsCreated = True
            note['title'] = title
            break

    if titleIsCreated:
        attempts = 0
        while attempts < 3:
            text = input('type your note: ')
            if valueIsEmpty(note):
                print('\n'+ 'Note cannot be empty')
                attempts += 1
            else:
                note['text'] = text
                note['userId'] = userId
                return note

    print('3 incorrect attempts')
    return False

# prints the notes out if everything went well and False if not.
def showNotes(userId: int):
    try:
        notes = queries.getNotesByUserId(userId)
        print(f'---------------\n')
        print('Your notes: ' + '\n')
        if len(notes) == 0:
            print('Any notes yet')
            print(f'---------------\n')
            return True
        for note in notes:
            print(f"title: {note[1]}\ntext: {note[2]}\n")
        print(f'---------------\n')
    except Exception as e:
        print(e)
        return False

def removeNote():
    attempts = 0
    while attempts < 3:
        global noteRemoved
        noteRemoved = False
        title = input('Type the tile of the note: ')
        if valueIsEmpty(title):
            print('\n'+ 'Title cannot be empty')
            attempts += 1
        else:
            try:
                queries.removeNote(title)
                print('Note successfully removed')
                noteRemoved = True
                break
            except Exception as e:
                print(e)
                break
    if noteRemoved == False and attempts == 3:
        print('3 incorrect attempts')
        
def valueIsEmpty(value: str):
    if len(value) == 0:
        return True
    else:
        return False