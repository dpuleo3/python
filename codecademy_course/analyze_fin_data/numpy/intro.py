import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])

#import from .csv fyle
test_2 = np.genfromtxt('test_2.csv', delimiter = ',')

test_3 = np.array([87, 85, 72, 90, 92])

#two extra points for test_3
test_3_fixed = test_3 + 2
print(test_3_fixed)

#Average 
total_grade = test_1 + test_2 + test_3_fixed
final_grade = total_grade / 3
print('Average grades: ', final_grade)

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

tanya_test_3 = student_scores[2, 0]
print(tanya_test_3)

cody_test_scores = student_scores[:, -1]
print(cody_test_scores)

#-------------------------------------------------------------------------------------------

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]
hot = porridge[porridge > 80]
just_right = porridge[(porridge>60) & (porridge<80)]

print(cold)
print(hot)
print(just_right)

#------------------------------------------------------------------------------------------

temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')
print(temperatures)

temperatures_fixed = temperatures + 3
print(temperatures_fixed)

monday_temperatures = temperatures_fixed[0,:]
print(monday_temperatures)

thursday_friday_morning = temperatures_fixed[3:5,1]
print(thursday_friday_morning)

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]
print(temperature_extremes)