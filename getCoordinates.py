#! /usr/bin/python3
# -*- coding: utf-8 -*-


#Ce fichier doit être utilisé quand l'étudiant doit répondre une coordonnée de point comme (2,3) ou (-5,2.6,9)

from inginious import input, feedback, rst

def is_coordinates(answer) :
        if len(answer.split(",")) != 3 : #Remplacez le "3" par le nombre de coordonnées. Exemple : pour le point (2,3), écrivez "2"
            return False
        if answer[0] != "(" or answer[-1] != ")" :
            return False
        return True
    
def is_correct(answer):
    return answer == "(1,5,-8)"  #Remplacez par la réponse correcte, si la réponse à la question est (5,6), écrivez "(5,6)"
answer = input.get_input("q1")
grade = 0


if is_coordinates(answer) == False : 
    feedback.set_problem_result("failed","q1")
    feedback.set_problem_feedback("Votre réponse n'est pas une coordonnée","q1")
    
elif is_coordinates(answer) == True :
    if is_correct(answer) == False :
        feedback.set_problem_result("failed","q1")
        feedback.set_problem_feedback("Votre réponse est incorrect","q1")
    elif is_correct(answer) == True :
        feedback.set_problem_result("success","q1")
        feedback.set_problem_feedback("Bravo!","q1")
        grade += 100
        
feedback.set_grade(grade)
if grade == 100 :
    feedback.set_global_result("success")
else :
    feedback.set_global_result("failed")