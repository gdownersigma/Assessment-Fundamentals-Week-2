"""Level 3 of the assessment."""
from datetime import date


class Assessment:
    """Blueprint for an Assessment class."""

    def __init__(self, name: str, score: float):
        """Constructor for Assessment class."""
        # validators
        if not 0 <= score <= 100:
            raise ValueError("Score must be in range 0-100.")

        self.name = name
        self.score = score
        self.weight = 0

    def calculate_score(self):
        """Method to return the calculated score."""
        return self.score * self.weight


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
        if not isinstance(assessment, Assessment):
            raise TypeError(
                "An assessment should be a subclass of Assessment.")
        self.assessments.append(assessment)

    def get_assessment(self, name: str):
        """Method to return an assessment if found, if not return None."""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment

        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """Method to return all assessments of a given type the trainee has."""

        if type.lower() not in ["multiple-choice", "technical", "presentation"]:
            raise ValueError(
                "Type must be 'multiple-choice', 'technical' or 'presentation'.")

        assessments_of_type = []
        for assessment in self.assessments:
            print(type)
            print(assessment.__str__())
            if type in assessment.__str__():
                assessments_of_type.append(assessment)
        return assessments_of_type


class MultipleChoiceAssessment(Assessment):
    """Blueprint for a multiple choice type of assessment."""

    def __init__(self, name: str, score: float):
        """Constructor method for multiple choice assessment."""
        super().__init__(name, score)
        self.weight = 0.7

    def __str__(self):
        return f"<multiple-choice Assessment: {self.name}>"

    def __repr__(self):
        return self.__str__()


class TechnicalAssessment(Assessment):
    """Blueprint for a technical type of assessment."""

    def __init__(self, name: str, score: float):
        """Constructor method for technical assessment."""
        super().__init__(name, score)
        self.weight = 1

    def __str__(self):
        return f"<technical Assessment: {self.name}>"

    def __repr__(self):
        return self.__str__()


class PresentationAssessment(Assessment):
    """Blueprint for a presentation type of assessment."""

    def __init__(self, name: str, score: float):
        """Constructor method for presentation assessment."""
        super().__init__(name, score)
        self.weight = 0.6

    def __str__(self):
        return f"<presentation Assessment: {self.name}>"

    def __repr__(self):
        return self.__str__()


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        pass


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
