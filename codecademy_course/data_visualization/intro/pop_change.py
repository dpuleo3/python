city_name = "Istanbul, Turkey"
pop_1927 = 691000
pop_2017 = 15029231

pop_change = (pop_2017 - pop_1927) / pop_1927
percentage_gr = pop_change * 100
annual_gr = percentage_gr / (2017 - 1927)
print(annual_gr)

def population_growth(year_one, year_two, population_one, population_two):
  growth_rate = (((population_two - population_one)/population_one)*100)/(year_two - year_one)
  return growth_rate

set_one = population_growth(1927, 2017, pop_1927, pop_2017)
print(set_one)

pop_1950 = 983000
pop_2000 = 8831800
set_two = population_growth(1950, 2000, pop_1950, pop_2000)
print(set_two)

print(city_name + " had an annual population growth between 1927-2017 of " + str(set_one) + '%')
print(city_name + " had an annual population growth between 1950-2000 of " + str(set_two) + '%')