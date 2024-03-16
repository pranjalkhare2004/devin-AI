import random

def random_program():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)
    
    # Print the random number
    print("Random number:", num)
    
    # Generate a random list of 5 numbers between 1 and 100
    num_list = random.sample(range(1, 101), 5)
    
    # Print the random list
    print("Random list:", num_list)
    
    # Generate a random letter from the alphabet
    letter = random.choice('abcdefghijklmnopqrstuvwxyz')
    
    # Print the random letter
    print("Random letter:", letter)
    
# Call the random_program function
random_program()