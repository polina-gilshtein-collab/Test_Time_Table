
days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def get_tests():
    tests_dict = {}
    tests_amount = int(input("How many tests do you have this week?"))
    for i in range(tests_amount):
        subject = input(f'Enter the subject of test number {i}: ')
        day = input(f'Enter the day of test number {i}: ')
        tests_dict[day] = subject
    return tests_dict

def get_school_hours(days):
    for i in range(len(days)):
        class_start_hour = input(f'If you have a class in {days[1]}, Enter the starting hour: ')



