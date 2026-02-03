# Problem 1
#devices = []

#while True:
#    device_names = str(input('Device Name: ')).lower()
#    if device_names == 'done':
#        break

#    devices.append(device_names)

#print(devices)


# Problem 2

#while True:
#    status = input('Status Report: ').lower()
#    if status == 'up':
#        print('System Up')
#        break
#    if status == 'down':
#        print('System Down')
#        break
#    else:
#        continue

# Problem 3

#correct_password = 'admin123'
#n = 0
#while n <= 3:
#    n += 1
#    pwd = input('Enter password: ')
#    if pwd == correct_password:
#        print('Access granted')
#        break
#    elif n == 3:
#        print('Account Locked.')
#        break

# Problem 4

#open_ports = []
#while True:
#    port_numbers = int(input('Enter used port numbers: '))
#    if port_numbers == 0:
#        break
#    open_ports.append(port_numbers)

#print(f'{open_ports}\nThere are {len(open_ports)} ports.')

# Problem 5
#notice = """
#    Enter rules 'Accept' or 'Deny'
#"""
#print(notice)

#while True:
#    action = input("What is the current firewall rule action: ").lower()
#    if action == 'accept':
#        print('Firewall rule set to ACCEPT')
#        break
#    if action == 'deny':
#        print('Firewall rule set to DENY')
#        break
#    else:
#        continue

# Problem 6 Added some dictionary to the mix

#devices = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
#status_report = {}

#while devices:
#    device = devices.pop()
#    print(device)
#    status = str(input('What is the status of device: ')).lower()
#    print(f'The status of {device} is {status}')

#    status_report[device] = status

#print(status_report)


#Problem 7

#policies = []
#id = {}

#while True:
#    policy_id = int(input('Create policy IDs: '))
#    #allowed = int(input('allowed ports'))
#    if policy_id == -1:
#        break
#    policies.append(policy_id)

#print(policies)

#for policy in policies:
#    allowed = input('allowed ports: ')
#    id[policy] = allowed

#print(list(id))

#for k,v in id.items():
#    if '22' in v or '443' in v:
#        print(f'Policy_id {k} port secured\n')
#    else:
#        print(f'Policy_id {k} port review Required\n')