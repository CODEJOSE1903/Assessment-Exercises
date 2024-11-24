#Advanced program: ignoring capitalisation
 
answer = input("What is the capital of france? ").strip().lower


if answer == "paris":
    print("correct!")
else:
    print("Wrong, the capital of France is Paris.")

#quiz with Multiple Queestions

#Dictionary of Questions (countries and capitals)
quiz = {
    "France": "Paris",
    "Germany":"Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Norway": "Oslo",
}

#Initialise score

score = 0

#Ask questions in a loop

print("Welcome to the European Capitals quiz!\n")

for country, capital in quiz.items():
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer ==capital.lower():
        print("Correct")
        score += 1
    else:
        print(f"Wrong! The capital of {country} is {capital}.")

#Display the final score

print(f"nYou got {score}/{len(quiz)} question correct!")