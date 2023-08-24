from utils import Commands
import json

commands = Commands

standart_commands = [
    'add',
    'find',
    'edit',
    'output',
    'exit',
    'help'    
]

search_type_command = [
    'all',
    'last-name',
    'first-name',
    'midle-name',
    'organization',
    'phone',
    'mobile-phone',
    'exit'
]

path = 'directory.json'

if __name__ == "__main__":    
    commands.command_processing(standart_commands, search_type_command, path)
