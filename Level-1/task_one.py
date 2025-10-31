"""Level 1 of the assessment."""
from datetime import date


class Assessment:
    """Blueprint for an Assessment class."""

    def __init__(self, name: str, given_type: str, score: float):
        """Constructor for Assessment class."""
        # validators
        if given_type not in ["multiple-choice", "technical", "presentation"]:
            raise ValueError(
                "Type must be 'multiple-choice', 'technical' or 'presentation'.")
        if not 0 <= score <= 100:
            raise ValueError("Score must be in range 0-100.")

        self.name = name
        self.type = given_type
        self.score = score


class Trainee:
    """Blueprint for the Trainee class."""

    def __init__(self, name: str, email: str, date_of_birth: date,):
        """Constructor for Trainee class."""
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self) -> int:
        """Method to return the age of this trainee."""
        return date.today().year - self.date_of_birth.year - \
            ((date.today().month, date.today().day) <
             (self.date_of_birth.month, self.date_of_birth.day))

    def add_assessment(self, assessment: Assessment) -> None:
        """Method to add an assessment to a trainees list of assessments."""
        self.assessments.append(assessment)

    def get_assessment(self, name: str):
        """Method to return an assessment if found, if not return None."""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment

        return None


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
