ESTADO_FINAL = "Caracter Aceptado"
ESTADO_TRAMPA = "Caracter No Valido"
ESTADO_NO_FINAL = "NO FINAL"


lista= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
listanum = ["0","1","2","3","4","5","6","7","8","9"]

def afd_id(cadena):
    estado_actual = 0
    estados_finales = [1]
    for caracter in cadena:
        if estado_actual == 0 and caracter in lista:
            estado_actual = 1
        elif estado_actual == 1 and caracter in lista+listanum:
            estado_actual = 1
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL


def afd_num(cadena):
    estado_actual = 0
    estados_finales = [1]
    for caracter in cadena:
        if estado_actual == 0 and caracter in listanum:
            estado_actual = 1
        elif estado_actual == 0 and caracter == "-":
            estado_actual = 2
        elif estado_actual == 1 and caracter in listanum:
            estado_actual = 1
        elif estado_actual == 2 and caracter in listanum:
            estado_actual = 1
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
    
def afd_equal(cadena):
    if cadena == "=":
        return ESTADO_FINAL
    else:
        return ESTADO_TRAMPA

def afd_walrus(cadena):
    if cadena == ":=":
        return ESTADO_FINAL
    else:
        return ESTADO_TRAMPA

def afd_parenizq(cadena):
    if cadena == "(":
        return ESTADO_FINAL
    else:
        return ESTADO_TRAMPA
        
def afd_parender(cadena):
    if cadena == ")":
        return ESTADO_FINAL
    else:
        return ESTADO_TRAMPA

def afd_coma(cadena):
    if cadena == ",":
        return ESTADO_FINAL
    else:
        return ESTADO_TRAMPA

def afd_puntoycoma(cadena):
    if cadena == ";":
        return ESTADO_FINAL
    else:
        return ESTADO_TRAMPA
        
def afd_sumoperator(cadena):
    if cadena in ["-","+"]:
        return ESTADO_FINAL
    else:
        return ESTADO_TRAMPA   
    
def afd_multoperator(cadena):
    if cadena in ["*", "/"]:
     return ESTADO_FINAL
    else:
     return ESTADO_TRAMPA

def afd_relation(cadena):
    if cadena in [">","<","=",">=","<=","<>"]:
      return ESTADO_FINAL
    else:
        return ESTADO_TRAMPA

# PALABRAS RESERVADAS

def afd_if(cadena):
    estado_actual = 0
    estados_finales = [2]
    for caracter in cadena:
        if estado_actual == 0 and caracter =="i":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "f":
            estado_actual = 2
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
       return ESTADO_FINAL
    elif estado_actual == -1:
       return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL

def afd_then(cadena):
    estado_actual = 0
    estados_finales = [4]
    for caracter in cadena:
        if estado_actual == 0 and caracter == "t":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "h":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "e":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "n":
            estado_actual = 4
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
     return ESTADO_TRAMPA
    else:
      return ESTADO_NO_FINAL

def afd_call(cadena):
    estado_actual = 0
    estados_finales = [4]
    for caracter in cadena:
        if estado_actual == 0 and caracter == "c":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "a":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "l":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "l":
            estado_actual = 4
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
       return ESTADO_FINAL
    elif estado_actual == -1:
      return ESTADO_TRAMPA
    else:
      return  ESTADO_NO_FINAL

def afd_begin(cadena):
    estado_actual = 0
    estados_finales = [5]
    for caracter in cadena:
        if estado_actual == 0 and caracter == "b":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "e":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "g":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "i":
            estado_actual = 4
        elif estado_actual == 4 and caracter == "n":
            estado_actual = 5
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
       return ESTADO_TRAMPA
    else:
       return ESTADO_NO_FINAL

def afd_end(cadena):
    estado_actual = 0
    estados_finales = [3]
    for caracter in cadena:
        if estado_actual == 0 and caracter == "e":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "n":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "d":
            estado_actual = 3
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
       return ESTADO_FINAL
    elif estado_actual == -1:
       return ESTADO_TRAMPA
    else:
       return ESTADO_NO_FINAL

def afd_hasta(cadena):
    estado_actual = 0
    estados_finales = [5]
    for caracter in cadena:
        if estado_actual == 0 and caracter == "h":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "a":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "s":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "t":
            estado_actual = 4
        elif estado_actual == 4 and caracter == "a":
            estado_actual = 5
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
       return ESTADO_TRAMPA
    else:
       return ESTADO_NO_FINAL

def afd_leer(cadena):
    estado_actual = 0
    estados_finales = [4]
    for caracter in cadena:
        if estado_actual == 0 and caracter == "l":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "e":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "e":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "r":
            estado_actual = 4
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
       return ESTADO_FINAL
    elif estado_actual == -1:
       return ESTADO_TRAMPA
    else:
       return ESTADO_NO_FINAL

def afd_mostrar(cadena):
    estado_actual = 0
    estados_finales = [7]
    for caracter in cadena:
        if estado_actual == 0 and caracter == "m":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "o":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "s":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "t":
            estado_actual = 4
        elif estado_actual == 4 and caracter == "r":
            estado_actual = 5 
        elif estado_actual == 5 and caracter == "a":
            estado_actual = 6
        elif estado_actual == 6 and caracter == "r":
            estado_actual = 7
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
       return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL

def afd_func(cadena):
    estado_actual = 0
    estados_finales = [4]
    for caracter in cadena:
        if estado_actual == 0 and caracter == "f":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "u":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "n":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "c":
            estado_actual = 4
        else:
            estado_actual = -1
            break
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL

def afd_finfunc(cadena):
    estado_actual = 0
    estados_finales = [7]
    for caracter in cadena:
        if estado_actual == 0 and caracter == "f":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "i":
            estado_actual = 2
        elif estado_actual == 2 and caracter == "n":
            estado_actual = 3
        elif estado_actual == 3 and caracter == "f":
            estado_actual = 4
        elif estado_actual == 4 and caracter == "u":
            estado_actual = 5
        elif estado_actual == 5 and caracter == "n":
            estado_actual = 6
        elif estado_actual == 6 and caracter == "c":
            estado_actual = 7
        else:
            estado_actual = -1
            break 
    if estado_actual in estados_finales:
        return ESTADO_FINAL
    elif estado_actual == -1:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
    

tokens_posibles = [ ("if",afd_if), ("then",afd_then), ("call",afd_call), ("begin",afd_begin), ("repetir",afd_repetir), ("hasta",afd_hasta), 
 ("leer",afd_leer), ("mostrar",afd_mostrar), ("func",afd_func), ("finfunc",afd_finfunc), ("id",afd_id),("num",afd_num), ("equal",afd_equal), ("walrus", afd_walrus), ("coma", afd_coma),
 (";",afd_puntoycoma), ("(",afd_parenizq), (")",afd_parender), ("multoperator",afd_multoperator), ("sumoperator",afd_sumoperator), ("relation",afd_relation) ] 

def lexer(codigofuente):
    tokens = [] 
    posicion_actual = 0  
    while posicion_actual < len(codigofuente):
        while codigofuente[posicion_actual].isspace():
              posicion_actual = posicion_actual+1

        comienzo_lexema = posicion_actual 
        posibles_tokens = [] 
        posibles_tokens_con_un_caracter_mas = [] 
        lexema = "" 
        var_aux_todos_en_estado_trampa = False
        
        while not var_aux_todos_en_estado_trampa and posicion_actual <= len(codigofuente):
            var_aux_todos_en_estado_trampa = True 
            lexema = codigofuente[comienzo_lexema:posicion_actual +1]
            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []
            
            for (tipo_token, afd) in tokens_posibles:
                simulacion_afd = afd(lexema) 
                if simulacion_afd == ESTADO_FINAL:
                    posibles_tokens_con_un_caracter_mas.append(tipo_token)
                    var_aux_todos_en_estado_trampa = False
                elif simulacion_afd == ESTADO_NO_FINAL:
                    var_aux_todos_en_estado_trampa = False
            
            posicion_actual = posicion_actual + 1 

        if len(posibles_tokens) == 0:
            print ("error : token desconocido "+ lexema)
        else:
            posicion_actual = posicion_actual - 1
            tipo_token = posibles_tokens[0]
            token = (tipo_token, codigofuente[comienzo_lexema:posicion_actual])
            tokens.append(token)

    
    return tokens
