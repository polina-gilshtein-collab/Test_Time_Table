def enter_studies(week,test_info_dict,test_dict):
    for i in range (test_dict["day"]- test_info_dict["days"], test_dict["day"] - test_info_dict["day_before"]):
        hours_added = 0
        for j in range(len(week[i])):
            if hours_added == test_info_dict["hours"]:
                break
            elif week[i][j] == "free":
                week[i][j] = test_info_dict["subject"]
                hours_added += 1





