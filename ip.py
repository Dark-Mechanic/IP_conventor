import socket as s
host = input("Enter the website: ")
print(f'IP of {host} is {s.gethostbyname(host)}')