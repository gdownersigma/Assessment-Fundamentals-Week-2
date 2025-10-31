"""Level 1 of the assessment"""
from datetime import date


class Assessment:
    """Blueprint for an Assessment class"""

    def __init__(self, name: str, type: str, score: float):
        # validators
        if type not in ["multiple-choice", "technical", "presentation"]:
            raise ValueError(
                "Type must be 'multiple-choice', 'technical' or 'presentation'.")
        if not 0 <= score <= 100:
            raise ValueError("Score must be in range 0-100.")


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
