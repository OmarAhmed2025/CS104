#Average of an unknown number of testscores

# Initialize:
average=0
total=0
howManyEntered=0
testscore=0

# Ask user to input number of test scores
howMany=int(input(' How many test scores would you like to average?'))

# Start loop to enter all test scores:
while howManyEntered < howMany:
    #input('Enter testscore')
    testscore=int(input('Enter testscore '))
    total = total + testscore
    howManyEntered = howManyEntered + 1

# Compute average test score:
average= total/howMany

# Display results:
print('The average for the test scores you entered is:')
print(average)
print('All Done!')
 
     


    



