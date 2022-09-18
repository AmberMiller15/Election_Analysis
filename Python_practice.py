# What is the score?
score = int(input("What is your test score? "))
# Determine the grade
if score >= 90:
    print ('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is D.')
else:
    print('Your grade is an F.')

counties = ['Arapahoe', 'Denver', 'Jefferson']
if "Arapahoe" in counties or "El Paso" not in counties:
    print ("Onluy Arapahoe is in the list of counties")
else:
    print ("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#x = 0
#while x <= 5:
 #   print (x)
  #  x=x+1

#for county in counties:
  #  print(county)

#numbers = [0,1,2,3,4]
#for num in numbers:
 #   print (num)

#for num in range (5):
    print (num)

for i in range(len(counties)):
    print(counties[i])

counties_tuple = ('Arapahoe', 'Denver', "Jefferson")
for county in counties_tuple:
    print(county)

counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson':432438}
# for counties in counties_dict.keys():
#     print (counties)
# for voters in counties_dict.values():
#     print(voters)
# for counties,voters in counties_dict.items():
#     print(counties, 'county has', voters, 'registered voters.')
#Edited to use F-strings
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")



voting_data = [{'county':'Arapahoe' , 'registered_voters':422829},
                {'county': 'Denver', 'registered_voters':463353},
                {'county': 'Jefferson', 'registered_voters':432438}]
# for county_dict in voting_data:
#     print (county_dict)
# for county_dict in voting_data:
#     #for value in county_dict.values():
#         #print (value)
# for county_dict in voting_data:
    # print(county_dict[county])


#OG voter percentage code
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#Edited to use F-strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Multiline F-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes.")

print(message_to_candidate)