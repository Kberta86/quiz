# Simple Python Quiz Game - Basic Python Knowledge

# This program uses basic concepts such as functions, loops,
# conditionals, and dictionaries to create an interactive quiz.
# References to best practices and foundational programming concepts
# are included based on Downey (2015), Shaw (2017), and others.

# Display the main menu to the user
def display_menu():
    print("\nWelcome to the Python Basics Quiz!")
    print("1. Start Quiz")
    print("2. Instructions")
    print("3. Exit")

# Show instructions for the quiz
def show_instructions():
    print("\nInstructions:")
    print("- The quiz contains 10 multiple-choice questions on basic Python concepts.")
    print("- Type the letter corresponding to your answer (a/b/c/d).")
    print("- Your final score will be displayed at the end.")

# Define the quiz questions using a list of dictionaries
# Each question includes text, multiple options, and the correct answer
def get_questions():
    return [
        {
            "question": "1. What is the correct file extension for Python files?",
            "options": {"a": ".pyth", "b": ".pt", "c": ".py", "d": ".p"},
            "answer": "c"
        },
        {
            "question": "2. What is the output of: print(type('Hello'))",
            "options": {"a": "<int>", "b": "<str>", "c": "<float>", "d": "<bool>"},
            "answer": "b"
        },
        {
            "question": "3. Which of the following is a Python keyword?",
            "options": {"a": "loop", "b": "then", "c": "def", "d": "define"},
            "answer": "c"
        },
        {
            "question": "4. How do you create a variable with the numeric value 5?",
            "options": {"a": "x = int(5)", "b": "x = 5", "c": "Both A and B", "d": "x == 5"},
            "answer": "c"
        },
        {
            "question": "5. Which data type is used to store text?",
            "options": {"a": "int", "b": "float", "c": "str", "d": "bool"},
            "answer": "c"
        },
        {
            "question": "6. What does the input() function do?",
            "options": {"a": "It prints text.", "b": "It takes user input.", "c": "It creates a loop.", "d": "It defines a function."},
            "answer": "b"
        },
        {
            "question": "7. Which operator is used for exponentiation in Python?",
            "options": {"a": "^", "b": "**", "c": "%", "d": "//"},
            "answer": "b"
        },
        {
            "question": "8. What is the correct way to start a function in Python?",
            "options": {"a": "function myFunc():", "b": "def myFunc():", "c": "create myFunc():", "d": "function:myFunc"},
            "answer": "b"
        },
        {
            "question": "9. How do you insert COMMENTS in Python code?",
            "options": {"a": "// This is a comment", "b": "# This is a comment", "c": "<!-- This is a comment -->", "d": "/* comment */"},
            "answer": "b"
        },
        {
            "question": "10. What does the 'len()' function do?",
            "options": {"a": "Returns the number of items in an object", "b": "Counts digits only", "c": "Returns the last element", "d": "Measures size of memory"},
            "answer": "a"
        },
    ]

# Function to execute the quiz logic and calculate the score
def run_quiz():
    score = 0
    questions = get_questions()

    for q in questions:
        print("\n" + q["question"])
        for key, value in q["options"].items():
            print(f"  {key}) {value}")

        answer = input("Your answer: ").lower()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer was {q['answer']}.")

    print(f"\nQuiz complete! You scored {score} out of {len(questions)}.")

# Main control flow with a loop to display the menu until user exits
# This structure and interaction style is common in CLI programs (Shaw, 2017)
while True:
    display_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        run_quiz()
    elif choice == "2":
        show_instructions()
    elif choice == "3":
        print("Exiting the quiz. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")