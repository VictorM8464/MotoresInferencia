
# Definicion de las premisas
premisa1 = {"llueve": True, "suelo_mojado": True}  # Si llueve, entonces el suelo estara mojado
premisa2 = {"llueve": True}  # Esta lloviendo

# Funcion para aplicar Modus Ponens
def modus_ponens(premisa_condicional, premisa_factual):
    if premisa_condicional[premisa_factual.keys()[0]] == premisa_factual.values()[0]:
        return True
    else:
        return False

# Aplicar Modus Ponens con las premisas definidas
conclusion = modus_ponens(premisa1, premisa2)

# Imprimir la conclusion
if conclusion:
    print("El suelo esta mojado.")
else:
    print("No se puede inferir si el suelo esta mojado o no.")
