import json
import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer
        }

try:
    with open("questions.json", "r") as file:
        questions_data = json.load(file)
except FileNotFoundError:
    questions_data = []

role = input("Are you a teacher or student? ").lower()
while True:
    if role == "teacher":
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")

        new_flashcard = Flashcard(question, answer)
        questions_data.append(new_flashcard.to_dict())

        with open("questions.json", "w") as file:
            json.dump(questions_data, file, indent=2)
        
        ask = input("Would you like to add more flashcards? Yes/No: ")
        if ask == "No":
            break

if role == "student":
    print()

