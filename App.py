import streamlit as st
import joblib
import pandas as pd

# Cargar el modelo de predicción
modelo = joblib.load('mejor_modelo_random_forest.bin')

# Título de la página
st.title('Predicción de Tipo de Delito')

# Descripción de la aplicación
st.write("""
Esta aplicación predice el tipo de delito basado en la información proporcionada.
Seleccione las opciones en el panel izquierdo para obtener una predicción.
""")

# Crear el formulario de entrada para los usuarios
st.sidebar.header('Parámetros de entrada')

# Selector para el sexo
sexo = st.sidebar.selectbox('Sexo', ('MASCULINO', 'FEMENINO'))

# Selector para el nombre de la comuna
comuna = st.sidebar.selectbox('Nombre de la Comuna', ['SUR', 'PROVENZA', 'LA CIUDADELA', 'LA CONCORDIA', 'CENTRO',
       'CABECERA DEL LLANO', 'ORIENTAL', 'OCCIDENTAL', 'SAN FRANCISCO',
       'NORORIENTAL', 'NORTE', 'SUROCCIDENTE', 'GARCIA ROVIRA',
       'MORRORICO', 'LA PEDREGOSA', 'MUTIS', 'LAGOS DEL CACIQUE',
       'NO DISPONIBLE', 'CORREGIMIENTO 1', 'CORREGIMIENTO 3',
       'CORREGIMIENTO 2'])

# Selector para el rango de horario
rango_horario = st.sidebar.selectbox('Rango de Horario', ['Mañana', 'Tarde', 'Noche'])

# Selector para el día de la semana
dia_semana = st.sidebar.selectbox('Día de la Semana', ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])


# Crear un botón para ejecutar la predicción
if st.sidebar.button('Predecir Tipo de Delito'):
    
    # Crear un DataFrame con las entradas
    data = {
        'SEXO': [sexo],
        'COMUNA': [comuna],
        'RANGO_HORARIO': [rango_horario],
        'DIA_SEMANA': [dia_semana],

    }
    
    # Convertir las entradas en un DataFrame
    df = pd.DataFrame(data)
    
    # Asegúrate de que las columnas del DataFrame coincidan con las del modelo
    # Puedes aplicar cualquier codificación o transformación adicional que necesites
    
    # Realizar la predicción
    prediccion = modelo.predict(df)[0]
    
    # Mostrar la predicción
    st.subheader('Tipo de Delito Predicho:')
    st.write(prediccion)


