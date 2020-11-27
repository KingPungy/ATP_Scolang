# ATP_Scolang
 python interpreter for a new programming language


Gekozen taal: Eigen Taal "Scolang"   
Turing-compleet omdat:   

Code is geschreven in functionele stijl.   

##Taal ondersteunt:   
Loops? Voorbeeld: [while.txt](voorbeelden/while.txt) - [regel 4]     
Goto-statements? Voorbeeld: [if.txt](voorbeelden/if.txt) - [regel 4]   
Lambda-calculus? Voorbeeld: [lambdaCalc.txt](voorbeelden/lambdaCalc.txt) - [regels 9 , 11]    

##Bevat:    
Classes met inheritance: bijvoorbeeld [nodes.py](nodes.py) - [regels: 7,16,31]      
Object-printing voor elke class: [__ja__/~nee~]      
Decorator: functiedefinitie op [lex.py](lex.py) - [regel: 72], toegepast op [interpreter.py] - [regel: 94-95]     
Type-annotatie: Haskell-stijl in comments: [~ja~/__nee__]; Python-stijl in functiedefinities: [__ja__/~nee~]     
Minstens drie toepassingen van hogere-orde functies:    
1. [lex.py](lex.py) - [regels: 17,52-55,66]  
2. [parser_atp.py](parser_atp.py) - [regel 184]     
3. [token_types.py](token_types.py) - [regels: 50,52]    

##Interpreter-functionaliteit Must-have:  
Functies: [één per file / meer per file]  
Functie-parameters kunnen aan de interpreter meegegeven worden door:    
Functies kunnen andere functies aanroepen: zie voorbeeld [file] - [regel]    
Functie resultaat wordt op de volgende manier weergegeven:    

##Interpreter-functionaliteit (should/could-have):    
[Gekozen functionaliteit] geïmplementeerd door middel van de volgende functies: a) [functie] in [file] op regel [regel]   
[Extra functionaliteit overlegd met docent, goedkeuring: datum e-mail; overeengekomen max. aantal punten: X]   

