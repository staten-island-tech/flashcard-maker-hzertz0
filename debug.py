import json
import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def display_info(self):
        return f"{self.question} - {self.answer}"
    
    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer
        }

# Initialize the data
try:
    with open("questions.json", "r") as file:
        questions_data = json.load(file)
except FileNotFoundError:
    questions_data = []  # If the file doesn't exist, start with an empty list

# Check the current content of questions_data (for debugging)
print("Current questions_data before adding new flashcard:", questions_data)

# Ask for role
role = input("Are you a teacher or student? ").lower()
if role == "teacher":
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    
    # Create the new flashcard
    new_flashcard = Flashcard(question, answer)
    
    # Debug: Print the new flashcard details
    print(f"New flashcard to be added: {new_flashcard.to_dict()}")
    
    # Append the new flashcard to the data list
    questions_data.append(new_flashcard.to_dict())
    
    # Debug: Check the updated data list before writing
    print("Updated questions_data after adding new flashcard:", questions_data)
    
    try:
        # Write the updated data back to the file
        with open("questions.json", "w") as file:
            json.dump(questions_data, file, indent=2)
        print("Flashcard successfully saved to questions.json.")  # Confirmation message
    except Exception as e:
        print(f"Error saving the file: {e}")  # Error handling if something goes wrong

if role == "student":
    print("filler")