from utils import Commands
import json

commands = Commands

standart_commands = [
    'add',
    'find',
    'edit',
    'output',
    'exit'    
]

path = 'directory.json'

if __name__ == "__main__":

    
    commands.command_processing(standart_commands, path)
    #json_data = get_data.given_directory('directory.json')
    #print(json_data)
    
    
    #data = 'Test'
    #add_data.add_given_directory(data)
    #data = []
    #json_data = {
    #    "name": 'name',
    #    "phone": 'phone',
    #}
    #data = json.load(open("db.json"))
    #data.append(json_data)
    #with open("db.json", "w") as file:
    #    json.dump(data, file, indent=2, ensure_ascii=False)
