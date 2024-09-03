#Lecture of 09/03/2024
money = 14
movie_cost = 20

if(money>movie_cost):
    print('We can see the movie')

else:
    print('We cannot see the movie')

print('I am out of the if statement')

#Second part of the lecture
#elif works to put different answer to the same questions without breaking the main if
grade = 65

if (grade >= 90):
    print('You got an A in the course')
elif (grade >= 80):
    print('You got an B in the course')
elif (grade >= 70):
    print('You got an C in the course')
elif (grade >= 60):
    print('You got an D in the course')
else:
    print('You got an F in the course')

#Third part of the lecture

fuel_level = 100
weather_temperature = 80

if(fuel_level > 80):
    print('Fuel level is a good')
if(weather_temperature > 60):
    print('Weahter is good')
elif(weather_temperature < 60):
    print('Blast off... see you in Houston')