import json

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

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

questions_data = [Flashcard.to.dict() for flashcard in questions]

with open("questions.json", "w") as file:
    json.dump(questions_data, file, indent=2)

role = input("Are you a teacher or student? ").lower
if role() == "teacher":
    print("test")
if role() == "student":
    print("test2")

