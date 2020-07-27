#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(1, '/course/common')

from inginious import input, feedback, rst
from parsingDomain import compareDomains

correct = "]-4;2]"					# INSERER ICI LA BONNE REPONSE

answer = input.get_input("q1")
grade = 0

result = compareDomains(answer, correct)

if result[0]:
    feedback.set_problem_result("success","q1")
    feedback.set_problem_feedback("Bravo!","q1")
    grade += 100
else:
    feedback.set_problem_result("failed","q1")
    feedback.set_problem_feedback(result[1],"q1")

feedback.set_grade(grade)
if grade == 100 :
    feedback.set_global_result("success")
else :
    feedback.set_global_result("failed")