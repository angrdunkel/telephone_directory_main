import json

class AddData:

    

    def given_directory(data, path):
        
        def find_id(data):
            last_row = data[-1]
            return last_row['id']

        last_name = input('Enter Last name: ')
        first_name = input('Enter First name: ')
        midle_name = input('Enter Midle name: ')
        organization = input('Enter Organization: ')
        phone = input('Enter Phone: ')
        mobile_phone = input('Enter Mobile phone: ')

        id = find_id(data)

        new_data = {
                        "id": id + 1,
                        "first_name": first_name,
                        "last_name": last_name,
                        "midle_name": midle_name,
                        "organization": organization,
                        "phone": phone,
                        "mobile_phone": mobile_phone
                    }
        data.append(new_data)
        with open(path, "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        return True
    
    def all_date(data, path):
        with open(path, "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        return True
    
    def check_edit_request(request):
        if request == '':
            return False
        return True

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
    
    def find_all_data(data, requests):
            
        if requests == 'exit':
            return False
        else:
            requests = requests.split(' ')
            find_first_name_list = []
            find_last_name_list = []
            find_midle_name_list = []
            find_organization_list = []
            find_phone_list = []
            find_mobile_phone_list = []

            for request in requests:
                       
                find_first_name = list(filter(lambda x:x["first_name"]==request,data))
                find_first_name_list.append(find_first_name)
                
                find_last_name = list(filter(lambda x:x["last_name"]==request,data))
                find_last_name_list.append(find_last_name)
                
                find_midle_name = list(filter(lambda x:x["midle_name"]==request,data))
                find_midle_name_list.append(find_midle_name)
                
                find_organization = list(filter(lambda x:x["organization"]==request,data))
                find_organization_list.append(find_organization)

                find_phone = list(filter(lambda x:x["phone"]==request,data))
                find_phone_list.append(find_phone)

                find_mobile_phone = list(filter(lambda x:x["mobile_phone"]==request,data))
                find_mobile_phone_list.append(find_phone)

            return {
                'find_first_name': find_first_name_list,
                'find_last_name': find_last_name_list,
                'find_midle_name': find_midle_name_list,
                'find_organization': find_organization_list,
                'find_phone': find_phone_list,
                'find_mobile_phone': find_mobile_phone_list
            }
    
    def find_data(request, data, find_type):
        if find_type == 'last-name':
            print('Last name result: ')
            request_type = "last_name"
        if find_type == 'first-name':
            print('First name result: ')
            request_type = "first_name"
        if find_type == 'midle-name':
            print('Midle name result: ')
            request_type = "midle_name"
        if find_type == 'organization':
            print('Organization name result: ')
            request_type = "organization"
        if find_type == 'phone':
            print('Phone result: ')
            request_type = "phone"
        if find_type == 'mobile-phone':
            print('Pobile phone result: ')
            request_type = "mobile_phone"
        
        find_results = list(filter(lambda x:x[request_type]==request,data))
        print('Results: ', len(find_results))
        if len(find_results) != 0:
            for row, result in enumerate(find_results):
                print()
                print(row + 1)
                print(f"Id: {result['id']}")
                print(f"Last name: {result['last_name']}")
                print(f"First name: {result['first_name']}")
                print(f"Midle name: {result['midle_name']}")
                print(f"Organization: {result['organization']}")
                print(f"Phone: {result['phone']}")
                print(f"Mobile phone: {result['mobile_phone']}")
            print("Search complite")
        else:
            print('Nothing found')
            print()
            

    def check_request(request):
        if len(request.split(' ')) > 1:
            print('Eroor: Too big request (request should be no more than one word)')
            return False
        return True
    


get_data = GetData

class DisplayResult:


    def find(data):
        def display_find_result(results):
            
            row = 0
            for result in results:
                for data in result:
                    row += 1                    
                    print(f"{row}:")
                    print(f"Id: {data['id']}")
                    print(f"Name: {data['last_name']} {data['first_name']} {data['midle_name']}")
                    print(f"Organization: {data['organization']}")
                    print(f"Phone: {data['phone']}")
                    print(f"Mobile Phone: {data['mobile_phone']}")
            
        print("Start searching")
        if len(data['find_last_name'][0]) != 0:
            print()
            print('Last name result: ')
            display_find_result(data['find_last_name'])
        if len(data['find_first_name'][0]) != 0:
            print()
            print('First name result: ')
            display_find_result(data['find_first_name'])
        if len(data['find_midle_name'][0]) != 0:
            print()
            print('Midle name result: ')
            display_find_result(data['find_midle_name'])
        if len(data['find_organization'][0]) != 0:
            print()
            print('Organization name result: ')
            display_find_result(data['find_organization'])
        if len(data['find_phone'][0]) != 0:
            print()
            print('Phone result: ')
            display_find_result(data['find_phone'])
        if len(data['find_mobile_phone'][0]) != 0:
            print()
            print('Mobile_phone result: ')
            display_find_result(data['find_mobile_phone'])
        print("End search")


display_result = DisplayResult
    
class Commands():    

    def command_processing(standart_commands, search_type_command, path):
        print()
        print('Snandart commands: ')
        for row, command in enumerate(standart_commands):
            print(f'{row+1} - {command}') 
        
        while True:
            data = get_data.given_directory(path)            
            print()   
            command = input("Enter command: ")
                            
            if command == 'exit':
                print()
                print ('Аpplication completed')
                break
            elif command == 'output':
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
                if add_data.given_directory(data, path):
                    print()
                    print('New data added')
                else: 
                    print()
                    print('Error data')
            elif command == 'help':
                print()
                print('Snandart commands: ')
                for row, command in enumerate(standart_commands):
                    print(f'{row+1} - {command}')
            elif command == 'find':

                while True:
                    print()
                    print('Search types:')
                    for row, request_type in enumerate(search_type_command):
                        print(f'{row+1} - {request_type}')
                    find_command = input('Enter search request_type or exit: ')
                    if find_command == 'exit':
                        break
                    if find_command == 'all':
                        requests = input('Enter search request or exit: ')  
                        requests_result = get_data.find_all_data(data, requests)
                        if requests_result:
                            display_result.find(requests_result)
                        else:
                            print('Search canceled')
                    elif find_command == 'last-name':
                        while True:
                            request = input('Enter search reque or exit: ')
                            if request == 'exit':
                                break
                            if get_data.check_request(request):
                                get_data.find_data(request, data, find_command)
                            else:
                                break
                    elif find_command == 'first-name':
                        while True:
                            request = input('Enter search reque or exit: ')
                            if request == 'exit':
                                break
                            if get_data.check_request(request):
                                get_data.find_data(request, data, find_command)
                            else:
                                break
                    elif find_command == 'midle-name':
                        while True:
                            request = input('Enter search reque or exit: ')
                            if request == 'exit':
                                break
                            if get_data.check_request(request):
                                get_data.find_data(request, data, find_command)
                            else:
                                break
                    elif find_command == 'organization':
                        while True:
                            request = input('Enter search reque or exit: ')
                            if request == 'exit':
                                break
                            if get_data.check_request(request):
                                get_data.find_data(request, data, find_command)
                            else:
                                break
                    elif find_command == 'phone':
                        while True:
                            request = input('Enter search reque or exit: ')
                            if request == 'exit':
                                break
                            if get_data.check_request(request):
                                get_data.find_data(request, data, find_command)
                            else:
                                break
                    elif find_command == 'mobile-phone':
                        while True:
                            request = input('Enter search reque or exit: ')
                            if request == 'exit':
                                break
                            if get_data.check_request(request):
                                get_data.find_data(request, data, find_command)
                            else:
                                break
                
                    else:
                        print('Error command')
            elif command == 'edit':
                while True:
                    id = input('Enter id or exit: ')
                    last_name = input('Enter Last name or "enter" button to skip: ')
                    first_name = input('Enter Fast name or "enter" button to skip: ')
                    midle_name = input('Enter Midle name or "enter" button to skip: ')
                    organization = input('Enter Organization name or "enter" button to skip: ')
                    phone = input('Enter Phone or "enter" button to skip: ')
                    mobile_phone = input('Enter Mobile phone or "enter" button to skip: ')
                    start_edit = input('To make changes enter "Y" if cancel any other value: ')

                    if id == 'exit':
                        break
                    try:
                       
                        id = int(id)
                        not_result = True
                        line_num = 0                        
                        for row in data:
                            if row['id'] == id:
                                not_result = False
                                if add_data.check_edit_request(last_name):
                                    row['last_name'] = last_name
                                if add_data.check_edit_request(first_name):
                                    row['first_name'] = first_name
                                if add_data.check_edit_request(midle_name):
                                    row['midle_name'] = midle_name
                                if add_data.check_edit_request(organization):
                                    row['organization'] = organization
                                if add_data.check_edit_request(phone):
                                    row['phone'] = phone
                                if add_data.check_edit_request(mobile_phone):
                                    row['mobile_phone'] = mobile_phone
                                while True:
                                    if start_edit == 'Y' or start_edit == 'y':
                                        add_data.all_date(data, path)
                                        print('Changes saved')
                                        break
                                    elif start_edit == '':
                                        start_edit = input('To make changes enter "Y" or "y" if cancel any other value: ')
                                    else:
                                        print('Changes not saved')
                                        break

                                break
                        if not_result:
                            print(f'Id: {id} not found')                        
                    except:
                        print(f'Error id: {id}')
            else:
                print()                
                print('Error comand!')
                print('Snandart commands: ')
                for row, command in enumerate(standart_commands):
                    print(f'{row+1} - {command}')
                            
                
                

        #reques = input("Enter request:")
