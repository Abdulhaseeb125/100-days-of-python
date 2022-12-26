from Day_16_Question import question_data


class Quiz:
    def __init__(self):
        self.true_counter = 0
        self.false_counter = 0
        self.Again = True
        self.input = None
        self.total_questions = len(question_data)
        self.asked = 0

    def Counter(self):
        print(f"Your Score is {self.true_counter}/{self.asked}, True/False: ")

    def user_input(self):
        while self.Again:
            for question in question_data:
                self.asked += 1
                self.input = input(f'Q.No {self.asked}: {question["text"]}')
                if self.asked == self.total_questions:
                    self.Again = False
                if self.input == question["answer"]:
                    self.true_counter += 1
                    print("You got it right!")
                    print(f"The correct answer was {question['answer']}")
                    self.Counter()
                else:
                    self.false_counter += 1
                    print("That's Wrong..!")
                    print(f"The correct answer was {question['answer']}")
                    self.Counter()


    def Completed(self):
        print("You have completed the quiz.")
        self.Counter()


quiz = Quiz()

quiz.user_input()
print("\n")
quiz.Completed()

