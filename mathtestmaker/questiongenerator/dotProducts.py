"""
This file contains functions for generating linear equations and a class that can summarize the available functions and call a selected
subset of the efunctions based on user input.

As of June 21st, 2017, the function returns a dictionary:
{
    "question_name": "The name of the question",
    "problem_statement": "The statement of the problem",
    "correct_answer": "The solution to the question",
    "solution": [
        (equation1, "first step to solve the problem"),
        (equation2, "second step to solve the problem"),
        ...,
        (equationN, "the final solution")
    ]
}
"""
import random
import utility # "import questiongenerator.utility as utility" does not work; I get ModuleNotFoundError; i am running Python 3.7.4
import inspect
from fractions import Fraction
#from returnVerifier import returnVerifier
"""
Class for finding the dot products of two vectors

--- Abbreviations ---
DP: dot product
v1: first vector
v2: second vector

--- Naming Conventions ---
Function names should indicate the type of question the function generates. Concepts are written in camelCase and different
concepts in a given function are separated by an underscore.
e.g. A question about finding an integer x intercept of a linear equation in slope-intercept form with a non-zero slope is called
findIntegralXIntercept_SIF_NonZeroM

--- Return values ---
All of the methods that generate questions need to return a dictionary containing:
1. problem_statement
2. correct_answer
3. solution

The problem statement and solution should return strings that can be used by LaTeX to format output. The formatting of these
strings may change in the future to allow for flexibility, but for now we are just using primitive LaTex syntax.
"""
class DotProducts(object):
    def __init__(self): # THIS IS TWO UNDERLINES BEFORE AND AFTER __init__()
        self.questions = dict([("Calculate the dot product of these two vectors whose elements are integers.",
        self.findDotProduct_NonZero),
        ("Calculate the dot product of these two vectors whose elements are fractions.",
        self.findDotProduct_NonZeroF)])
        self.codeName = "dot_products"
        self.displayName = "Dot Products"
        self.categoryInformation = "A set of questions involving the dot products of vectors whose elements are integers or fractions."

    def getQuestionNames(self):
        """
        @return: A list of all the questions available
        """
        return self.questions.keys() # returns a view object that displays a list of all the keys in the dictionary

    def getQuestion(self, name, numChoices, points):
        """
        TBD
        """
        return self.questions[name](numChoices, points) # self.questions is a dictionary

    def findDotProduct_NonZero(self, numChoices, points): 
        # calculate three random numbers for each vertex
        a = random.randint(-20, 20)
        b = random.randint(-20, 20)
        c = random.randint(-20, 20)

        d = random.randint(-20, 20)
        e = random.randint(-20, 20)
        f = random.randint(-20, 20)
        # create a tuple for each
        v1 = (a, b, c)
        v2 = (d, e, f)
        # create a variable storing the sum of both tuples
        v3 = ((v1[0] + v2[0]), (v1[1] + v2[1]), (v1[2] + v2[2]))
        # create dictionary w/ problemStatement,correctAnswer,correctAnswerIdx,wrongAnswers,points,solution
        d = {}
        
        # solutions property should show solution as a string step-by-step 
        problemStatement = "Find the dot product of {} and {} ."
        d["problemStatement"] = problemStatement.format(v1, v2)
        d["correctAnswer"] = v3 # this is good; you can assign a tuple as as value
        d["correctAnswerIdx"] = utility.getCorrectAnswerIndex(numChoices)
        d["wrongAnswers"] = utility.generateWrongAnswers(numChoices, v3, "tup") # what are 2nd + 3rd parameters; make sure this
        # doesn't break generateWrongAnswers() function because v3 is a tuple
        d["points"] = points
        d["solution"] = [
            ("{} and {}".format(v1, v2), "Find the corresponding entries of the two vectors."),
            ("({} + {}, {} + {}, {} + {})".format(v1[0],v2[0],v1[1],v2[1],v3[2],v3[2]), "Add the corresponding entries of the two vectors."),
            ("{}".format(v3), "This is the final answer.")
        ]
        return d                      

    def findDotProduct_NonZeroF(self, numChoices, points):
        """
        In Python 3, they made the / operator do a floating-point division, and added the // operator to do integer division
        (i.e. quotient without remainder); whereas in Python 2, the / operator was simply integer division, unless one of the operands
        was already a floating point number.
        """

        v1_1_n = 0
        v1_2_d = 0
        v1_3_n = 0
        v1_4_d = 0
        v1_5_n = 0
        v1_6_d = 0

        v2_1_n = 0
        v2_2_d = 0
        v2_3_n = 0
        v2_4_d = 0
        v2_5_n = 0
        v2_6_d = 0

        while ((v1_1_n == 0) and (v1_2_d == 0) and (v1_3_n == 0) and (v1_4_d == 0) and (v1_5_n == 0) and (v1_6_d == 0)):
            v1_1_n = random.randint(-30, 30)
            v1_2_d = random.randint(-30, 30)
            v1_3_n = random.randint(-30, 30)
            v1_4_d = random.randint(-30, 30)
            v1_5_n = random.randint(-30, 30)
            v1_6_d = random.randint(-30, 30)

        while ((v2_1_n == 0) and (v2_2_d == 0) and (v2_3_n == 0) and (v2_4_d == 0) and (v2_5_n == 0) and (v2_6_d == 0)):
            v2_1_n = random.randint(-30, 30)
            v2_2_d = random.randint(-30, 30)
            v2_3_n = random.randint(-30, 30)
            v2_4_d = random.randint(-30, 30)
            v2_5_n = random.randint(-30, 30)
            v2_6_d = random.randint(-30, 30)

        v1 = ((v1_1_n / v1_2_d), (v1_3_n / v1_4_d), (v1_5_n / v1_6_d))
        v2 = ((v2_1_n / v2_2_d), (v2_3_n / v2_4_d), (v2_5_n / v2_6_d))

        # create a variable storing the sum of both tuples
        v3 = ((v1[0] + v2[0]), (v1[1] + v2[1]), (v1[2] + v2[2]))
        # create dictionary w/ problemStatement,correctAnswer,correctAnswerIdx,wrongAnswers,points,solution
        d = {}
        
        # solutions property should show solution as a string step-by-step 
        problemStatement = "Find the dot product of {} and {} ."
        d["problemStatement"] = problemStatement.format(v1, v2)
        d["correctAnswer"] = v3
        d["correctAnswerIdx"] = utility.getCorrectAnswerIndex(numChoices)
        d["wrongAnswers"] = utility.generateWrongAnswers(numChoices, v3, "ints") # what are 2nd + 3rd parameters; make sure this
        # doesn't break generateWrongAnswers() function
        d["points"] = points
        d["solution"] = [
            ("{} and {}".format(v1, v2), "Find the corresponding entries of the two vectors."),
            ("({} + {}, {} + {}, {} + {})".format(v1[0],v2[0],v1[1],v2[1],v3[2],v3[2]), "Add the corresponding entries of the two vectors."),
            ("{}".format(v3), "This is the final answer.")
        ]
        return d     