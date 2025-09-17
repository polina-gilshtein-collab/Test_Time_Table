import constant
def build_matrix(num_hours_in_day):
    matrix=[]
    for i in range(5):
        day=[]
        for j in range(num_hours_in_day):
            day.append("free")
        matrix.append(day)
    return matrix
def enter_club(matrix,club):
    for i in range (club["time"]):
        matrix[club["day"]][club["start"]- constant.start_hour+i]= club["name"]


def enter_hour_per_day(matrix, list_of_hour):
    for i in range(len(matrix)):
        for j in range(list_of_hour[1]-list_of_hour[0]):
            matrix[i][list_of_hour[0]-constant.start_hour+i] = "school"



