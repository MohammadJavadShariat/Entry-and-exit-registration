import datetime

# List of incoming persons
person1 = []

# List of people's arrival time
Time1 = []

# List of outgoing persons
person2 =[]

# List of departure time of people
Time2 = []

while (True):  #To ask for input again
    name = input("Employee login *** first and last name (enter the word 'end' to finish):\n ")
    
    # To finish and not ask questions again
    if name == "end":
        break
    
    # To save the time of arrival of people
    t1 = datetime.datetime.now()
    t2 = t1.hour
    t3 = t1.minute
    t4 = t1.second
    
    # Save the name and time of entry of the person
    person1.append(name)
    Time1.append(f"{t2}:{t3}:{t4}")

print("\n\n\n")
while (True): # To ask for output again
    name = input("Exit Employee *** First and last name (enter the word 'end' to finish):\n ")

    # To finish and not ask questions again
    if name == "end":
        break

    # To record the time of people's departure
    t1 = datetime.datetime.now()
    t2 = t1.hour
    t3 = t1.minute
    t4 = t1.second

    #Save the person's name and exit time
    person2.append(name)
    Time2.append(f"{t2}:{t3}:{t4}")
    
# Checking the equality of inputs with outgoing people
if len(person1) == len(person2):
    # Convert to set
    S1 = set(person1)
    S2 = set(person2)

#If the members of two groups are not equal
#(For the situation where, for example, Ali and Hassan entered and Sajjad and Hassan left.)
    if not S1 == S2:
      
# Print people who have left and people 
#who have not registered their entry. 
        S3 = S1.difference(S2)
        S4 = S2.difference(S1)
        
        #One person is a singular sentence
        if len(S3) == 1 and len(S4) == 1 :
            print(f"\nEmployee {S3} has not left the office.")
            print(f"\nEmployee {S4} has not logged in.")

        #Dunfar to the top of the plural sentence
        else:
            print(f"\nEmployees with the names {S3} have not left the office.")
            print(f"\nEmployees with the names {S4} have not logged in.")

# If the number of input and output is not equal
else:

    # Convert to set
    S1 = set(person1)
    S2 = set(person2)

    # If inputs are more than outputs.
    if len(person1) > len(person2):

#The person's print has not been removed
        S3 = S1.difference(S2)
        
        #One person is a singular sentence
        if len(S3) == 1 : 
            print(f"\nEmployee {S3} has not left the office.\n")
            
        #Dunfar to the top of the plural sentence
        else:
            print(f"\nEmployees with the names {S3} have not left the office.\n")
            
    # If the outputs are more than the inputs.
    elif len(person1) <len(person2):

# Print the person who did not register the entry
        S3 = S2.difference(S1)
        
        #One person is a singular sentence
        if len(S3) == 1 : 
            print(f"\nEmployee {S3} has not logged in.\n")
            
        #Dunfar to the top of the plural sentence
        else:
            print(f"\nEmployees named {S3} have not logged in.\n")

# Print inputs and outputs and time of entry and exit
print("\n************************Inputs************************\n")
for i in range(len(person1)):
    print(f"{person1[i]}, entry time: {Time1[i]}")
print("\n************************Outputs************************\n")
for i in range(len(person2)):
    print(f"{person2[i]}, departure time: {Time2[i]}")