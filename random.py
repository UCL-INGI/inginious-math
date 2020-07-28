#!/bin/python3
# -*- coding: utf-8 -*-

# Ce fichier doit être utilisé pour un exercice de type 'random' à un seul sous-problème

import re
#import math                Si nécessaire
from sympy import sympify, simplify
from sympy.parsing.latex import parse_latex
from inginious import input, feedback, rst


# Intégrer les variables que vous avez définie dans le sous-problème

# nom_de_variable = int(input.get_input("@random")[indice]*100)

# Ce qui correspond à l'exemple d'énoncé du TUTO (à remplacer) :

somme = 10000*int(input.get_input("@random")[0] * 100 + 1)
plus2 = 1000*int(input.get_input("@random")[1] * 100 + 1)
minus3 = 1000*int(input.get_input("@random")[2] * 100 + 1)


# Définir comment la réponse correcte sera vérifiée avec les différents paramètres

# Ce qui correspond à l'exemple du TUTO (à remplacer) :

correct_equation = str(somme) + " = x + x + " + str(plus2) + " + x  + " + str(plus2)  + " - " + str(minus3)



def parse_equation(latex_str):
    latex_str = re.sub("(\\\left|\\\\right)", "", latex_str)
    return parse_latex(latex_str)

def is_equal(eq1, eq2):
    return simplify(eq1) == simplify(eq2) or simplify(sympify(str(eq1))) == simplify(sympify(str(eq2)))

try:
    student_answer = parse_equation(input.get_input("math1")) #Inscrire l'id du sous-problème à la place de 'math1'
    correct_answer = parse_equation(correct_equation)
except LaTeXParsingError as e:
    feedback.set_global_result("failed")
    feedback.set_global_feedback("parsing error")

if is_equal(student_answer, correct_answer):
    feedback.set_global_result("success")
else:
    feedback.set_global_result("failed")
    feedback.set_global_feedback("wrong answer")