import unittest


def is_coordinates(answer) :
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
    answer = answer.strip()
    answer = list(answer)
    simp_answer = "("
    for el in answer :
        if el in "-.,1234567890" :
            simp_answer += el
    simp_answer += ")"
    
    return simp_answer == correction


class TestFonction(unittest.TestCase) :
    
    def test_is_coordinates(self):
        "Tests de la fonction is_coordinates"
        
        self.assertEqual(is_coordinates(" (2,3) "),True,"Doit ignorer les espaces")
        self.assertEqual(is_coordinates("( 2 , 3 )"),True,"Doit ignorer les espaces")
        self.assertEqual(is_coordinates("(2;3)"),"separateur","Les coordonnées doivent être séparées par une ',' ")
        self.assertEqual(is_coordinates("(2.3)"),"separateur","Les coordonnées doivent être séparées par une ',' ")
        self.assertEqual(is_coordinates("xg"),"lettre")
        self.assertEqual(is_coordinates("(2x,5)"),"lettre","Ne doit comprendre que des chiffres")
        self.assertEqual(is_coordinates("(2.5,5.3)"),True,"Peut contenir des nombres à virgules")
        self.assertEqual(is_coordinates("(-3,9)"),True,"Peut contenir des nombres négatifs")
        self.assertEqual(is_coordinates("[1,2]"),"parenthese","Doit être des parenthèses")
        self.assertEqual(is_coordinates("1,2"),"parenthese","Doit vérifier que les panrenthèses sont présentent")

    def test_is_correct(self):
        "Tests de la fonction is_correct"
        
        self.assertEqual(is_correct("(2,2)","(2,2)"),True)
        self.assertEqual(is_correct(" (2 , 2 )","(2,2)"),True)
        self.assertEqual(is_correct("(-5, 69 )","(-5,69)"),True)
        self.assertEqual(is_correct("(2.6, 8 , -5)","(2.6,8,-5)"),True)
        
              
if __name__ == "__main__":
    unittest.main()