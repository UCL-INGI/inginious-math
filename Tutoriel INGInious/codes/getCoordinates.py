#! /usr/bin/python3
# -*- coding: utf-8 -*-

#Ce fichier doit être utilisé quand l'étudiant doit répondre une coordonnée de point comme (2,3) ou (-5,2.6,9)

from inginious import input, feedback, rst

def is_coordinates(answer) :
    """ Vérifie que la réponse est bien une coordonnée écrite sous la forme '(x,y)', x et y étant des réels
        
        pre: aucune
        post: retourne 'lettre' si une lettre est présente dans la réponse, 'parenthese' s'il n'y a pas de parenthèse, 'separateur' si le séparateur
              n'est pas une virgule et 'True' si la réponse est sous la bonne forme
    """
    answer = answer.strip()
    if answer[0] != "(" or answer[-1] != ")" :
        if answer[0].isalpha() :
            return "lettre"
        return "parenthese"
    if len(answer.split(",")) == 1 :
        return "separateur"
    answer = list(answer)
    for el in range(1,len(answer)-1) :
        try :
            int(answer[el])
        except :
            if answer[el] not in ["-"," ",",","."] :
                if answer[el].isalpha() :
                    return "lettre"
                return "separateur"
    return True
        
def is_correct(answer,correction):
    """ Vérifie si la réponse de l'étudiant est la réponse attendue
  
        pre: aucune
        post: renvoie 'True' si la réponse est juste, 'False' sinon
    """
    answer = answer.strip()
    answer = list(answer)
    simp_answer = "("
    for el in answer :
        if el in "-.,1234567890" :
            simp_answer += el
    simp_answer += ")"
    
    return simp_answer == correction  

answer = input.get_input("q1") #Remplacez tous les 'q1' par l'ID du sous-problème 
grade = 0
check = is_coordinates(answer)

if check != True : #Renvoie un feedback personnalisé en fonction des erreurs rencontrées
    feedback.set_problem_result("failed","q1") #Ici
    if check == "parenthese" :
        feedback.set_problem_feedback("Votre réponse doit contenir des parenthèses pour délimiter le point","q1") #Ici
    if check == "lettre" :
        feedback.set_problem_feedback("Votre réponse ne doit contenir que des chiffres","q1") #Ici
    if check == "separateur":
        feedback.set_problem_feedback("Les coordonnées doivent être séparées par une virgule","q1") #Ici
    
elif check == True :
    if is_correct(answer,"(2,2)") == False : #Remplacez '(2,2)' par la réponse correcte, si la réponse à la question est (5,6), écrivez "(5,6)"
        feedback.set_problem_result("failed","q1") #Ici
        feedback.set_problem_feedback("Votre réponse est incorrect","q1") #Ici
    elif is_correct(answer,"(2,2)") == True : #Remplacez '(2,2)' par la réponse correcte, si la réponse à la question est (5,6), écrivez "(5,6)"
        feedback.set_problem_result("success","q1") #Ici
        feedback.set_problem_feedback("Bravo!","q1") #Ici
        grade += 100
        
feedback.set_grade(grade)
if grade == 100 :
    feedback.set_global_result("success")
else :
    feedback.set_global_result("failed")
