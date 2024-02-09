import sys
sys.path.append(r'C:\Users\HAMZAT\Desktop\Python Learning\_UnitTests')

import Add_Subfunction

def overall(obj, practical, project):
    return (
        ((80/100)*obj) + ((10/100)*practical) + ((10/100)*project)
        )
obj_numbers = [11,18,20,15,18,20,13,19,20,18,19,18]
result = Add_Subfunction.add(*obj_numbers)
obj_score = (result/240) * 100

practical_number = 17
practical_score = (practical_number/20) * 100

project_score = 68

round_off_overall = round((overall(obj_score, practical_score, project_score)),2)
print (round_off_overall,'%')