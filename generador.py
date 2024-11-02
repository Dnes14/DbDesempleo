import random
import csv
from datetime import datetime

# Configuración de datos
distritos = ['San Isidro', 'Miraflores', 'Surco', 'La Molina', 'San Borja', 'Barranco', 'San Miguel', 
             'Magdalena', 'Jesús María', 'Lince', 'Surquillo', 'La Victoria', 'Pueblo Libre']

sectores = ['Tecnología', 'Finanzas', 'Comercio', 'Industrial', 'Educación', 'Salud', 'Consultoría', 'Marketing']

niveles_educativos = ['Superior', 'Técnico', 'Postgrado']

# Rangos salariales por sector
rangos_salarios = {
    'Tecnología': (4000, 7000),
    'Finanzas': (4500, 8000),
    'Comercio': (2800, 4500),
    'Industrial': (3000, 5500),
    'Educación': (3000, 4500),
    'Salud': (3500, 6000),
    'Consultoría': (5000, 8000),
    'Marketing': (3500, 6000)
}

# Generar 800 registros
registros = []
for i in range(1, 801):
    edad = random.randint(22, 45)
    sexo = random.choice(['M', 'F'])
    nivel_educativo = random.choices(niveles_educativos, weights=[45, 35, 20])[0]
    ubicacion = random.choice(distritos)
    sector = random.choice(sectores)
    estado_empleo = random.choices(['Empleado', 'Desempleado'], weights=[70, 30])[0]
    
    # Calcular salario y años de experiencia
    if estado_empleo == 'Empleado':
        salario = random.randint(rangos_salarios[sector][0], rangos_salarios[sector][1])
        anos_experiencia = min(random.randint(1, 10), edad - 22)  # No más experiencia que edad - 22
    else:
        salario = 0
        anos_experiencia = random.randint(1, 10)
    
    registro = [
        i,  # ID_Persona
        edad,
        sexo,
        nivel_educativo,
        ubicacion,
        f'E{str(i).zfill(3)}',  # ID_Empleo
        sector,
        estado_empleo,
        salario,
        anos_experiencia
    ]
    registros.append(registro)

# Crear el CSV
header = ['ID_Persona', 'Edad', 'Sexo', 'Nivel_Educativo', 'Ubicacion_Geografica', 
          'ID_Empleo', 'Sector', 'Estado_Empleo', 'Salario_Mensual', 'Anos_Experiencia']

# Generar el contenido del CSV como string
csv_content = [','.join(header)]
for registro in registros:
    csv_content.append(','.join(str(x) for x in registro))

# Unir todo en un string
output = '\n'.join(csv_content)

# Crear un archivo CSV y escribir el contenido en él
with open('datos.csv', 'w') as csvfile:
    csvfile.write(output)

print("Archivo CSV creado con éxito!")