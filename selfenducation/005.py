inn = int(input("max: "))
user_answer = input("Even / Odd ").lower().strip()
def get_bool(user_answer):
    while True:
        try:
           if user_answer == "even": return 1
           elif user_answer == "odd": return 0
        except KeyError:
           print("Invalid input please enter even or odd!")
        except ValueError:
           print("Thats not an integer silly!")


def check(a,b):
    count = 0
    if b ==1:
        while count < a:

            if count % 2 == 0:
                if count != 0:
                    print(count, end=' ')
            count += 1
    else:
        while count < a:

            if count % 2:
                 print(count, end=' ')
            count += 1


check(inn, get_bool(user_answer))