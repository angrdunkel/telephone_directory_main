import json

class AddData:

    def given_directory(data):

        print(True)

add_data = AddData

class GetData():

    def given_directory(path):
        try:
            data = json.load(open(path))
        except:
            data = [] 
            with open("db.json", "r") as file:
               json.dump(data, file, indent=2, ensure_ascii=False)
        return data
    
    def test():
        print('Test')

get_data = GetData
    
class Commands():    

    def command_processing(standart_commands, path):
        print('Snandart commands: ')
        for row, command in enumerate(standart_commands):
            print(f'{row+1} - {command}')
        while True: 
            print()   
            command = input("Enter command: ")
            if command not in standart_commands:
                print()                
                print('Error comand!')
                print('Snandart commands: ')
                for row, command in enumerate(standart_commands):
                    print(f'{row+1} - {command}')
            elif command == 'exit':
                print()
                print ('Аpplication completed')
                break
            elif command == 'output':
                data = get_data.given_directory(path)
                if len(data) == 0:
                    print()
                    print('Records are missing')
                else:
                    for row, record in enumerate(data):
                        print()
                        print(f"{row+1} - ID: {record['id']}")
                        print(f"Name: {record['last_name']} {record['first_name']} {record['midle_name']}")
                        print(f"Organization: {record['organization']}")
                        print(f"Phome: {record['phone']}")
                        print(f"Mobile phone: {record['mobile_phone']}")
            elif command == 'add':
                data = get_data.given_directory(path)
                last_name = input('Enter Last name: ')
                first_name = input('Enter First name: ')
                midle_name = input('Enter Midle name: ')
                organization = input('Enter Organization: ')
                phone = input('Enter Phone: ')
                mobile_phone = input('Enter Mobile phone: ')
                new_data = {
                        "id": "3",
                        "first_name": first_name,
                        "last_name": last_name,
                        "midle_name": midle_name,
                        "organization": organization,
                        "phone": phone,
                        "mobile_phone": mobile_phone
                    }
                data.append(new_data)
                print(data)
                with open(path, "w") as file:
                    json.dump(data, file, indent=2, ensure_ascii=False)

        #reques = input("Enter request:")
