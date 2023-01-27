import os

network = input("Enter the network address (e.g. 192.168.1): ")
start = int(input("Enter the starting IP address: "))
end = int(input("Enter the ending IP address: "))

for ping in range(start, end):
    address = network + "." + str(ping)
    res = os.system("ping -c 1 " + address)
    if res == 0:
        print(address, 'is up!')
    else:
        print(address, 'is down.')
