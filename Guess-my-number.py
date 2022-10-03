#Input player answer
answer = int(input("Enter your answer: "))
#Input User Guess
guess = int(input("Enter your Guess: "))
#Conditions to meet
if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"
