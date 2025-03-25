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
        
        ask = input("Would you like to add more flashcards? Yes/No: ").lower()
        if ask != "yes":
            break

    if role == "student":
        streak = 0
        correct = 0
        points = 0
        while True:
            random_item = random.choice(questions_data)

            print(random_item['question'])

            answer = input("What is the answer to the question? ").lower()
            if answer == random_item['answer'].lower():
                streak += 1
                correct += 1
                points = round(points + 1 + streak)
                print(f"You got it correct! Streak = {streak}, Total Correct Answers = {correct}, Points = {points}")
            else:
                print(f"You got it wrong! The correct answer was {random_item['answer']}")
                streak = 0
            
            next = input("Would you like to continue? ").lower()
            if next != "yes":
                break
        if next != "yes":
            break
    
    if role != "student" and role != "teacher":
        break

