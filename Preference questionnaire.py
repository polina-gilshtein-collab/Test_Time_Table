def quiz(test):
    question_answers = {"subject": test}
    hours = int(input("hours a day do you want to dedicate to studying this subject?"))
    while not hours_24(hours):
        hours = int(
            input("put a number between 1-6.How many hours a day do you want to dedicate to studying this subject?"))
    question_answers["hours"] = hours
    days_before = int(input("How many days before the test do you want to start studying?"))
    question_answers["days"] = days_before
    day = input("Do you want to study the day before the test? yes/no")
    question_answers["day_before"] = day
    return question_answers


def hours_24(hours):
    return 0 < hours <= 6


def main():
    print(quiz("bio"))


if __name__ == "__main__":
    main()