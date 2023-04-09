

def idiotcheck_name():
    while True:
        s = input('Whrite your name: ')
        try:
            if s.isalpha():
                break
        except:
            if s.isdecimal():
                print("IS IT DIG?!")
            else:
                print(f"%%#??")
    return s


def idiotcheck_f_name():
    while True:
        s = input('Whrite your family name: ')
        try:
            if s.isalpha():
                break
        except:
            if s.isdecimal():
                print("IS IT DIG?!")
            else:
                print(f"%%#??")
    return s


def idiotcheck_dig():
    while True:
        s = input('Whrite your phone number: ')
        try:
            if s.isdecimal():
                break
        except:
            if s.isalpha():
                print("IS IT WORD?!")
            else:
                print(f"%%#??")
    return s


def start():

    while True:
        s = input(
            'What do you wan to do: write, find, delite, change or check all?: ')
        s = s.lower()
        try:
            if s == 'write':
                return 1
                break
            else:
                if s == 'find':
                    return 2
                    break
                else:
                    if s == 'delite':
                        return 3
                        break
                    else:
                        if s == 'check all':
                            return 4
                            break
                        else:
                            if s == 'change':
                                return 5
                                break
        except:
            if s.isdecimal():
                print("IS IT DIG?!")
            else:
                print(f"%%#??")


def add_new_contact():
    with open('dz8\ new_text.txt', 'a') as f:
        f.write(idiotcheck_f_name())
        f.write(' ')
        f.write(idiotcheck_name())
        f.write(' ')
        f.write(idiotcheck_dig())
        f.write(' ')
        f.write('\n')


def find_1():
    a = input("Whar do you want to find (name, family name, or number): ")
    with open('dz8\ new_text.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if a in line:
                print(line)
                break


def delite():
    while True:
        a = input("What do you want to delite: ")
        try:
            with open('dz8\ new_text.txt', 'r') as f:
                lines = f.readlines()
                with open('dz8\ new_text.txt', 'w') as fw:
                    for line in lines:
                        if a not in line.strip('\n'):
                            fw.write(line)

                    print("Deleted")
                    break 

        except:
            print("Oops! something error")


def change():
    while True:
        a = input("What do you want to change?: ")
        b = input('What the change?: ')
        try:
            with open('dz8\ new_text.txt', 'r') as f:
                lines = f.readlines()
                with open('dz8\ new_text.txt', 'w') as fw:
                    for line in lines:
                        fw.write(line.replace(a, b))

                    print("Changed")
                    break 
        except:
            print("Oops! something error")  


def print_all():
    with open('dz8\ new_text.txt', 'r') as f:
        print(f.readlines())


def final():
    a = start()
    if a == 1:
        add_new_contact()
    else:
        if a == 2:
            find_1()
        else:
            if a == 3:
                delite()
            else:
                if a == 4:
                    print_all()
                else:
                    if a == 5:
                        change()


final()
