# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
a = user_input.find("21")
b = user_input.find("12")
answer = "No"
if a * b < 0:
    answer = "No"
else:
    if abs(a - b) > 1:
        answer = "Yes"
    else:
        ui2 = user_input.replace("21", "0", 1)
        if ui2.find("12") > -1:
            answer = "Yes"
        else:
            ui2 = user_input.replace("12", "0", 1)
            if ui2.find("21") > -1:
                answer = "Yes"
print(answer)
