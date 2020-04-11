import random

# Variables

intentos_fallidos=0
acertados=0
preguntas = [['la capital de Buenos Aires es La Plata', 'si'],
            ['la capital de Catamarca es San Fernando del Valle de Catamarca', 'si'],
            ['la capital de Chaco es Resistencia', 'si'],
            ['la capital de Chubut es Rawson', 'si'],
            ['la capital de Córdoba es Córdoba', 'si'],
            ['la capital de Corrientes es Paraná', 'no'],
            ['la capital de Entre Ríos es Paraná', 'si'],
            ['la capital de Formosa es Formosa', 'si'],
            ['la capital de Jujuy es San Salvador de Jujuy', 'si'],
            ['la capital de La Pampa es General Acha', 'no'],
            ['la capital de La Rioja es La Rioja', 'si'],
            ['la capital de Mendoza es Mendoza', 'si'],
            ['la capital de Misiones es Posadas', 'si'],
            ['la capital de Neuquén es Neuquén', 'si'],
            ['la capital de Río Negro es Villalonga', 'no'],
            ['la capital de Salta es Santa Rosa de Tastil', 'no'],
            ['la capital de San Juan es San Juan', 'si'],
            ['la capital de San Luis es San Luis', 'si'],
            ['la capital de Santa Cruz es Río Gallegos', 'si'],
            ['la capital de Santa Fe es Santa Fe de la Vera Cruz', 'si'],
            ['la capital de Santiago del Estero es Santiago del Estero', 'si'],
            ['la capital de Tierra del Fuego es Rio Gallegos', 'no'],
            ['la capital de Tucumán es San Miguel de Tucumán', 'si']]

# Modulos

def seleccion (preguntas):
    seleccion_random = random.choice(preguntas)
    return(seleccion_random)
   
def pregunta (seleccion_random):
    print('Es correcto que ', seleccion_random[0])
    respuesta = input()
    respuesta_minuscula= respuesta.lower()
    return(respuesta_minuscula)
    
def evaluacion (preguntas, seleccion_random, respuesta_minuscula) :
    global intentos_fallidos
    global acertados
    if respuesta_minuscula == seleccion_random[1] :
        print('Correcto!')
        acertados = acertados + 1
        print()
        a = preguntas.index(seleccion_random)
        del(preguntas[a])
        print('Has acertado ', acertados, ' provincias,te quedan ', len(preguntas))
    else:
        print('Incorrecto')
        print('probemos con otra...')
        print()
        intentos_fallidos = intentos_fallidos + 1

    return(preguntas,intentos_fallidos)
        
#Programa principal

while  intentos_fallidos <3:
    variable_seleccion= seleccion(preguntas)
    variable_pregunta= pregunta(variable_seleccion)
    evaluacion(preguntas,variable_seleccion,variable_pregunta)

print('Has gastado tus 3 intentos. Estudia mejor y proba de nuevo')

