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



# Opdracht
Gekozen taal: Eigen Taal "Scolang"   
Turing-compleet omdat:   

Code is geschreven in functionele stijl.   

## Taal bevat:
### Operators
|operator|uitleg|C equivalent|
|:-:|:-:|:-:|
|var1 <b>plus</b> var2| berkent de optelling van de 2 variabeles| var1 + var2|
|var1 <b>min</b> var2| trekt de 2 variabelen van elkaar af| var1 - var2|
|var1 <b>ddivide</b> var2| berkent de deling van de 2 variabeles| var1 / var2|
|var1 <b>times</b> var2| berkent de vermenigvuldiging van de 2 variabeles| var1 * var2|
|var1 <b>power</b> var2| berkent var1 tot de macht var2 (var1<sup>var2</sup>) |pow(var1,var2)|
|var1 <b>smaller_than</b> var2| geeft 1 als var1 kleiner is dan var2 anders 0| var1 < var2|
|var1 <b>greater_than</b> var2| geeft 1 als var1 groter is dan var2 anders 0| var1 > var2|
|var1 <b>equal_to</b> var2| geeft 1 als var1 gelijk is aan var2 anders 0| var1 == var2|
|var1 <b>not_equal_to</b> var2| geeft 1 als var1 niet gelijk is aan var2 anders 0| var1 != var2|
|var1 <b>greater_equal</b> var2| geeft 1 als var1 gelijk is aan of groter is dan var2 anders 0| var1 >= var2|
|var1 <b>smaller_equal</b> var2| geeft 1 als var1 gelijk is aan of kleiner is dan var2 anders 0| var1 <= var2|
|var_name <b>is</b> const/expr/var_name| slaat de waarde aan de rechterkant van de <b>is</b> op in de gespecificeerde variabele naam| var_name = 1 / var_name = 1 + 2 / var_name = var2|

bij alle operators is het mogelijk om deze te combineren, er wordt rekening gehouden met de rekenregels hieronder een lijst met de prioriteit van de operators. Daarnaast kunnen alle variabeles die aangemaakt zijn binnen het programma gebruikt worden op de plaats van var1/var2 in bovenstaande tabel. Tevens kunnen hier ook constantes staan.

<b>
1. macht 
 
2. delen/vermenigvuldigen  

3. plus/min  

4. gelijk_aan,groter_dan,kleiner_dan en assignment(wordt)  

</b>   

Een aantal voorbeelden voor het gebruik van operators.    

```c
var1 = 1            //var1 is 1
1 + 2               //1 plus 2
var2 = 1 + 2        //var2 is 1 plus 2
3 + pow(2,4)        //3 plus 2 power 4
3 * 5/4 + 10        //3 times 5 divide 4 plus 10
```
### Speciale uitzonderingen met operatoren

De plus operator kan als enige ook met strings werken en kan hiermee dus ook een string en een int/float aan elkaar plakken door deze te casten naaar een string.

De conditionele operatoren gebruiken de lengte van een string als hiermee wordt vergeleken.

### Keywords
|keyword|uitleg|C equivalent|
|:-:|-|:-:|
|<b>if</b>|een if statement die kijkt of de conditie waar* is, als dit zo is dan wordt de "body" van de if uitgevoerd anders wordt er gesprongen naar de bijbehorende endif. | if |
|<b>endif</b>|geeft het einde van een if statement aan| de afsluitende } van een if|
|<b>while</b>|een statement die de "body" uitvoert als de conditie waar is, anders wordt er gesprongen naar de bijbehorende endwhile | while |
|<b>endwhile</b>| geeft het einde van een while loop aan en springt terug naar de bijbehorende while en kijkt dan weer opnieuw of de loop uitgevoerd wordt of geskipt.|de afsluitende } van een while|
|<b>show</b>| print de variabele of uitkomst van een expressie die achter de show staat, het is alleen mogelijk om 1 variabele of 1 uitkomst tegelijk te printen bijvoobeeld show var1,var2 is niet mogelijk op dit moment. daarnaast kunnen strings geprint worden, dit kan door een sting tussen "" achter de show te zetten. | printf()|




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







