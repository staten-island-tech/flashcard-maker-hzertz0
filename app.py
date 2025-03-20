import json

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

questions = [
    Flashcard("What are the sides you use to calculate sine?", "Opposite/Hypotenuse"),
    Flashcard("What are the sides you use to calculate cosine?", "Adjacent/Hypotenuse"),
    Flashcard("What are the sides you use to calculate tangent?", "Opposite/Adjacent")
]

try:
    with open("questions.json", "r") as file:
        questions_data = json.load(file)

except FileNotFoundError:
    questions_data = []

questions_data = [Flashcard.to_dict() for Flashcard in questions]

with open("questions.json", "w") as file:
    json.dump(questions_data, file, indent=2)

role = input("Are you a teacher or student? ").lower
if role() == "teacher":
    asked = input("Input phrase & answer: ")
if role() == "student":
    print()

