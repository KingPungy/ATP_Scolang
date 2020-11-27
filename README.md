# ATP_Scolang
 Python interpreter for a new programming language

## Bestanden
 - <b>[interpreter.py](interpreter.py) :</b> In deze file staat het interpret gedeelte, dus het doorlopen van de AST en uiteindelijk een output genereren.
 - <b>[lex.py](lex.py) :</b> In deze file staat het lexer gedeelte, het omvormen van de file met text naar bruikbare tokens.
 - <b>[nodes.py](nodes.py) : </b> In deze file staan alle mogelijke nodes van de AST, dit zijn puur classes voor het opslaan van data en hebben alleen een __str__() functie maar geen andere methods.
 - <b>[operators.py](operators.py) :</b> In deze file staan alle operators o.a. voor +,-,= maar ook voor bijvoorbeeld de if en functies om de program state te bewerken.
 - <b>[parser_scolang.py](parser_scolang.py) :</b> In deze file staan alle functies om te parsen(de token lijst omvormen naar een AST), de file name is parser_scolang.py omdat parser.py een build in python functie.
 - <b>[program_state.py](program_state.py) :</b> In deze file staat de class voor mijn program state waarin ik de huidige staat van het programma bij houd zoals bijvoorbeeld het huidige regelnummer en de variabelen.
 - <b>[token_class.py](token_class.py) :</b> In deze file staat de basis token klasse die gebruikt wordt om tokens aan te maken in de lexer.
 - <b>[token_types.py](token_types.py) : </b> In deze file staat een enum met alle verschillende token types zoals een NUMBER en een OPERATOR_MULTIPLY bijvoorbeeld.

De test.py file en de .txt files zijn voornamelijk voor testen tijdens het maken van het project.



# opdracht
Gekozen taal: Eigen Taal "Scolang"   
Turing-compleet omdat:   

Code is geschreven in functionele stijl.   

taal bevat:





### Taal ondersteunt:   
Loops? Voorbeeld: [while.txt](voorbeelden/while.txt) - [regel 4]     
Goto-statements? Voorbeeld: [if.txt](voorbeelden/if.txt) - [regel 4]   
Lambda-calculus? Voorbeeld: [lambdaCalc.txt](voorbeelden/lambdaCalc.txt) - [regels 9 , 11]    

### Bevat:    
Classes met inheritance: bijvoorbeeld [nodes.py](nodes.py) - [regels: 7,16,31]      
Object-printing voor elke class: [__ja__/~nee~]      
Decorator: functiedefinitie op [lex.py](lex.py) - [regel: 72], toegepast op [interpreter.py](interpreter.py) - [regel: 94-95]     
Type-annotatie: Haskell-stijl in comments: [~ja~/__nee__]; Python-stijl in functiedefinities: [__ja__/~nee~]     
Minstens drie toepassingen van hogere-orde functies:    
1. [lex.py](lex.py) - [regels: 17,52-55,66]  
2. [parser_scolang.py](parser_scolang.py) - [regel 184]     
3. [token_types.py](token_types.py) - [regels: 50,52]    

### Interpreter-functionaliteit Must-have:  
Functies: [één per file / meer per file]  
Functie-parameters kunnen aan de interpreter meegegeven worden door:    
Functies kunnen andere functies aanroepen: zie voorbeeld [file] - [regel]    
Functie resultaat wordt op de volgende manier weergegeven:    

### Interpreter-functionaliteit (should/could-have):    
[Gekozen functionaliteit] geïmplementeerd door middel van de volgende functies: a) [functie] in [file] op regel [regel]   
[Extra functionaliteit overlegd met docent, goedkeuring: datum e-mail; overeengekomen max. aantal punten: X]   







