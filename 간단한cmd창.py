import os
def cmd(command) :
    if command == 'dir' :
        os.system('dir')
    elif command == 'cls' :
        os.system('cls')
    elif command == 'ipconfig' :
        os.system('ipconfig')
    elif command == 'ping 8.8.8.8' :
        os.system('ping 8.8.8.8')
    else : 
        print('잘못된 입력')
        
userin = input("명령어 입력 : ")
cmd(userin)