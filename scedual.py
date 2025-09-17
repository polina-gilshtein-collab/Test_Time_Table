from prettytable import PrettyTable
import constant
def print_week(matrix):
    myTable = PrettyTable(constant.days)
    for hour in matrix :
        myTable.add_row(hour)

    return myTable



