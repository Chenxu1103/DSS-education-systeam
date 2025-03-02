import pandas as pd


class UserInput:
    def __init__(self):
        self.learning_goal = ""
        self.problem_statement = ""
        self.feedback = ""

    def get_user_input(self):
        self.learning_goal = input("Please enter your learning goal: ")
        self.problem_statement = input("Please describe your problem: ")
        self.feedback = input("Any feedback to enhance learning experience? ")

    def display_input(self):
        print(f"Learning Goal: {self.learning_goal}")
        print(f"Problem Statement: {self.problem_statement}")
        print(f"Feedback: {self.feedback}")

    def load_sample_input(self, filepath):
        # 从CSV文件加载样本输入
        data = pd.read_csv(filepath)
        return data
