#Funciones de todas las operaciones de los conjuntos
#Función de la intersección
def intersection(conj1, conj2):
    #Lista que se devolvera al usuario
    intersection = []
    for a in conj1:
        #Revisa que los valores del primer conjunto esten en el segundo
        if a in conj2:
            intersection.append(a)
    return (intersection, '.')

#Función de la union
def union(conj1, conj2):
    #Lista que se devolvera al usuario
    union = []
    #Añade los elementos del primer conjunto
    for a in conj1:
        union.append(a)
    #Añade los elementos del segundo conjunto que no se encontraban en el primero
    for b in conj2:
        if b not in union:
            union.append(b)
    return (union,'.')

#Función de la diferencia
def difference(conj1, conj2):
  #Lista que se devolvera al usuario
  difference = []
  #Añade los elementos que si esten en el primer conjunto pero no en el segundo.
  for a in conj1:
      if a not in conj2:
          difference.append(a)
  return (difference,'.')

#Función de la diferencia para la función simetrica
def difference2(conj1, conj2):
  #Lista que se devolvera al usuario
  difference = []
  for a in conj1:
      if a not in conj2:
          difference.append(a)
  for b in conj2:
      if b not in conj1:
          difference.append(b) 
  return (difference)

#Función de la simetrica
def symmetric_difference(conj1, conj2):
    #Lista que se devolvera al usuario
    symmetric_difference = []
    symmetric_difference.append(difference2(conj1, conj2))
    return (symmetric_difference)

#Función del complemento
def complement(conj1):
    #Lista que se devolvera al usuario
    complement = []
    #Añade los elementos que no esten en el conjunto seleccionado pero sí en el universo
    for i in range(1, 101):
      if i not in conj1:
        complement.append(i)
    return(complement,'.')

#Función del producto cartesiano
def ProductoCartesiano(conj1, conj2):
  #Lista que se devolvera al usuario
  cartesiano = []
  #Combina cada valor del primer conjunto que escogio el usuario y lo combina con el segundo
  for a in conj1:
    for b in conj2:
      cartesiano.append((a, b))
  return (cartesiano, ",")

#Función de la potencia
def potencia(conj1):
  if len(conj1) == 0:
      return [[]]
  r = potencia(conj1[:-1])
  #Operación para sacar cada combinación del conjunto
  return (r + [s + [conj1[-1]] for s in r])

#Función de la cardinalidad
def Cardinalidad(conj1):
  #Comando len devuelve el número de elementos en el conjunto seleccionado
  cardinalidad = len(conj1)
  return (cardinalidad)

#Función de la Contencion
def Contencion(conj1, conj2):
  #Revisa que los valores del primer conjunto esten en el segundo
  for i in range (len(conj1)):
    if conj1[i] in conj2:
      t = "Verdadero"
    else:
      return "Falso"
    
  #Checa que el conjunto A y el conjunto B no sean iguales
  if t=="Verdadero":
      if len(conj1)==len(conj2):
          return "Falso"
      else:
          return "Verdadero"
