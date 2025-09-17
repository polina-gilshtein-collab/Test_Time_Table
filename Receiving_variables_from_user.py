
days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def get_tests():
    tests_dict = {}
    tests_amount = int(input("How many tests do you have this week?"))
    for i in range(tests_amount):
        subject = input(f'Enter the subject of test number {i}: ')
        day = input(f'Enter the day of test number {i}: ')
        tests_dict[day] = subject
    return tests_dict


def get_learning_hours():
    list_hours=[]
    for i in range(5):
        mini_list=[]
        start=input(f"enter start hour of learning day {i+1}:")
        end=input(f"enter ending hour of learning day {i+1}:")
        while not not_earlier(start,end):
            end = input(f"end hour cant be earlier than start hour. enter ending hour of learning day {i + 1}:")
        mini_list.append(start)
        mini_list.append(end)
        list_hours.append(mini_list)
    print(list_hours)


def not_earlier(start,end):
    return start<end


def main():
    get_learning_hours()

if __name__=="__main__":
    main()