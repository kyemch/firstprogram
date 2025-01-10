import random  # Import the random module

# Define the questions and answers
questions = [
    {
        "question": "How do you prefer to spend your weekend?",
        "options": {
            "a": "Going out with friends",
            "b": "Reading a book",
            "c": "Trying out a new hobby",
            "d": "Relaxing at home"
        },
        "scores": {
            "a": "extrovert",
            "b": "introvert",
            "c": "adventurous",
            "d": "relaxed"
        }
    },
    {
        "question": "What is your favorite type of movie?",
        "options": {
            "a": "Action",
            "b": "Romantic",
            "c": "Documentary",
            "d": "Comedy",
            "e": "Dramas"
        },
        "scores": {
            "a": "adventurous",
            "b": "romantic",
            "c": "intellectual",
            "d": "fun-loving",
            "e": "dramatic"
        }
    },
    {
        "question": "What kind of music do you enjoy listening to?",
        "options": {
            "a": "Rock",
            "b": "Musicals",
            "c": "Techno",
            "d": "Opera"
        },
        "scores": {
            "a": "energetic",
            "b": "artistic",
            "c": "intellectual",
            "d": "dramatic"
        }
    },
    {
        "question": "Hey, do you have the time?",
        "options": {
            "a": "I'd be happy to tell you!",
            "b": "Sorry, I don't know.",
            "c": "Look it up on your phone.",
            "d": "It's the Quarternary period of the Cenozoic Era."
        },
        "scores": {
            "a": "sympathetic",
            "b": "unaware",
            "c": "rude",
            "d": "smart-ass"
        }
    },
    {

        "question": "What kind of pet do you like most?",
        "options": {
            "a": "dogs",
            "b": "cats",
            "c": "birds",
            "d": "fish"
        },
        "scores": {
            "a": "energetic",
            "b": "relaxed",
            "c": "extrovert",
            "d": "introvert"
        }

    },
    {
      
        "question": "What's your favorite flavor profile?",
        "options": {
            "a": "spicy",
            "b": "sour",
            "c": "salty",
            "d": "sweet",
            "e": "bitter"
            
        },
        "scores": {
            "a": "adventurous",
            "b": "smart-ass",
            "c": "extrovert",
            "d": "fun-loving",
            "e": "relaxed"
        }
        
    },
    # Add more questions as needed
]

# Personality types and counters for each type
def reset_scores():
    return {
        "extrovert": 0,
        "introvert": 0,
        "adventurous": 0,
        "relaxed": 0,
        "romantic": 0,
        "intellectual": 0,
        "fun-loving": 0,
        "artistic": 0,
        "dramatic": 0,
        "sympathetic": 0,
        "unaware": 0,
        "rude": 0,
        "smart-ass": 0,
        "energetic": 0
    }

personality_scores = reset_scores()

# Define dynamic personality combinations
dynamic_personalities = {
    frozenset(["extrovert", "fun-loving"]): "Life of the Party",
    frozenset(["introvert", "intellectual"]): "Thoughtful Thinker",
    frozenset(["energetic", "adventurous"]): "Fearless Explorer",
    frozenset(["relaxed", "introvert"]): "Meditative",
    frozenset(["relaxed", "romantic"]): "Chill Romantic",
    frozenset(["artistic", "dramatic"]): "Creative Visionary",
    frozenset(["artistic", "smart-ass"]): "Witty Poet",
    frozenset(["sympathetic", "smart-ass"]): "Empathetic Wit",
    # Add more combinations as needed
}


# Function to prompt for the number of questions
def get_number_of_questions():
    while True:
        try:
            num_questions = int(input("How many questions would you like to answer? (1-5): "))
            if 1 <= num_questions <= len(questions):
                return num_questions
            else:
                print(f"Please choose a number between 1 and {len(questions)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to display questions and get user input
def ask_questions(num_questions=3): # Change this number to the desired number of questions
    global personality_scores
    # Shuffle the questions
    random.shuffle(questions)

    # Limit the number of questions
    selected_questions = questions[:num_questions]

    for q in selected_questions:
        print(q["question"])
        for option, answer in q["options"].items():
            print(f"{option}) {answer}")
        choice = input("Enter your choice (a/b/c/d): ").lower()

        # Ensure valid input
        while choice not in q["options"]:
            print("Invalid choice, please choose again.")
            choice = input("Enter your choice (a/b/c/d): ").lower()

        # Update the personality score
        selected_personality = q["scores"][choice]
        personality_scores[selected_personality] += 1

# Function to calculate the personality result
def calculate_result():
    # Find the highest score(s)
    max_score = max(personality_scores.values())
    top_traits = [key for key, value in personality_scores.items() if value == max_score]
    
    # Check for predefined dynamic personalities
    if len(top_traits) > 1:
        for combination, description in dynamic_personalities.items():
            if combination.issubset(set(top_traits)):
                return description  # Return the dynamic personality
    
    # If no predefined combination matches, return individual traits
    return top_traits if len(top_traits) > 1 else top_traits[0]

# Function to display the result
def display_result(result):
    if isinstance(result, str):  # If the result is a dynamic personality
        print(f"Your personality type is: {result}")
    elif len(result) == 1:  # Single dominant trait
        print(f"Your personality type is: {result[0]}")
    else:  # Multiple dominant traits
        print("You have multiple dominant personality traits:")
        for res in result:
            print(f"- {res}")


# Function to restart the quiz
def restart_quiz():
    global personality_scores
    while True:
        restart = input("Would you like to play again? (yes/no): ").lower()
        if restart == "yes":
            personality_scores = reset_scores()
            run_quiz()
            break
        elif restart == "no":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Main function to run the quiz
def run_quiz():
    print("Welcome to the Personality Quiz!")
    num_questions = get_number_of_questions()  # Get the user's preferred number of questions
    ask_questions(num_questions=num_questions)  # Pass it to the ask_questions function
    result = calculate_result()
    display_result(result)
    restart_quiz()

# Run the quiz
if __name__ == "__main__":
    run_quiz()
