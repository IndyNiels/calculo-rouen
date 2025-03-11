import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(
    page_title="Comparador de Bicicletas",
    page_icon="🚲",
    layout="wide"
)

# Título y descripción de la aplicación
st.title("Comparador de Bicicletas")
st.markdown("¡Utiliza los controles deslizantes para personalizar tu bicicleta perfecta!")

# Crear barra lateral para entradas
st.sidebar.header("Elige los parámetros de tu bicicleta")

# Configuración de la primera bicicleta
st.sidebar.subheader("Nuestra Bicicleta")

# Control deslizante de precio para bicicleta 1
price_range_1 = st.sidebar.slider(
    "Rango de Precio (€) - Nuestra Bicicleta",
    min_value=500,
    max_value=5000,
    value=1500,
    step=100,
    help="Selecciona tu presupuesto para nuestra bicicleta"
)

# Control deslizante de batería para bicicleta 1
battery_capacity_1 = st.sidebar.slider(
    "Capacidad de Batería (Wh) - Nuestra Bicicleta",
    min_value=250,
    max_value=1000,
    value=500,
    step=50,
    help="Mayor capacidad significa mayor autonomía"
)

# Control deslizante de potencia del motor para bicicleta 1
motor_power_1 = st.sidebar.slider(
    "Potencia del Motor (Nm) - Nuestra Bicicleta",
    min_value=50,
    max_value=100,
    value=70,
    step=5,
    help="Mayor par motor significa mejor aceleración y capacidad para subir pendientes"
)

# Control deslizante de Cadre ENVSO para bicicleta 1 (cambiado a porcentaje)
frame_size_1 = st.sidebar.slider(
    "Cadre ENVSO (%) - Nuestra Bicicleta",
    min_value=50,
    max_value=100,
    value=75,
    step=5,
    help="Porcentaje de Cadre ENVSO - un valor más alto indica mejor calidad"
)

# Añadir un separador
st.sidebar.markdown("---")

# Configuración de la segunda bicicleta
st.sidebar.subheader("Bicicleta Competidor")

# Control deslizante de precio para bicicleta 2
price_range_2 = st.sidebar.slider(
    "Rango de Precio (€) - Bicicleta Competidor",
    min_value=500,
    max_value=5000,
    value=2500,
    step=100,
    help="Selecciona el presupuesto para la bicicleta competidora"
)

# Control deslizante de batería para bicicleta 2
battery_capacity_2 = st.sidebar.slider(
    "Capacidad de Batería (Wh) - Bicicleta Competidor",
    min_value=250,
    max_value=1000,
    value=750,
    step=50,
    help="Mayor capacidad significa mayor autonomía"
)

# Control deslizante de potencia del motor para bicicleta 2
motor_power_2 = st.sidebar.slider(
    "Potencia del Motor (Nm) - Bicicleta Competidor",
    min_value=50,
    max_value=100,
    value=85,
    step=5,
    help="Mayor par motor significa mejor aceleración y capacidad para subir pendientes"
)

# Control deslizante de Cadre ENVSO para bicicleta 2 (cambiado a porcentaje)
frame_size_2 = st.sidebar.slider(
    "Cadre ENVSO (%) - Bicicleta Competidor",
    min_value=50,
    max_value=100,
    value=65,
    step=5,
    help="Porcentaje de Cadre ENVSO - un valor más alto indica mejor calidad"
)

# Mostrar configuraciones seleccionadas
st.header("Configuraciones de Bicicletas")

# Crear columnas para mejor diseño
col1, col2 = st.columns(2)

# Mostrar configuración de bicicleta 1
with col1:
    st.subheader("Configuración de Nuestra Bicicleta")
    st.write(f"**Rango de Precio:** {price_range_1}€")
    st.write(f"**Capacidad de Batería:** {battery_capacity_1} Wh")
    st.write(f"**Potencia del Motor:** {motor_power_1} Nm")
    st.write(f"**Cadre ENVSO:** {frame_size_1}%")

# Mostrar configuración de bicicleta 2
with col2:
    st.subheader("Configuración de Bicicleta Competidor")
    st.write(f"**Rango de Precio:** {price_range_2}€")
    st.write(f"**Capacidad de Batería:** {battery_capacity_2} Wh")
    st.write(f"**Potencia del Motor:** {motor_power_2} Nm")
    st.write(f"**Cadre ENVSO:** {frame_size_2}%")

# Calcular puntuaciones usando la fórmula: Puntuación = (Valor más bajo × 10) / Valor actual
st.header("Puntuación de Bicicletas")

# Crear una función para calcular la puntuación (mayor es mejor)
def calculate_score(value1, value2):
    min_value = min(value1, value2)
    score1 = (min_value * 10) / value1 if value1 > 0 else 0
    score2 = (min_value * 10) / value2 if value2 > 0 else 0
    return score1, score2

# Calcular puntuaciones para cada parámetro
price_score1, price_score2 = calculate_score(price_range_1, price_range_2)
# Para batería, motor, tamaño del cuadro - mayor es mejor, así que invertimos la fórmula
battery_score1, battery_score2 = calculate_score(1/battery_capacity_1, 1/battery_capacity_2)
motor_score1, motor_score2 = calculate_score(1/motor_power_1, 1/motor_power_2)
frame_score1, frame_score2 = calculate_score(1/frame_size_1, 1/frame_size_2)

# Aplicar ponderaciones: Precio 40%, otros 20% cada uno
weighted_price_score1 = price_score1 * 0.4
weighted_price_score2 = price_score2 * 0.4
weighted_battery_score1 = battery_score1 * 0.2
weighted_battery_score2 = battery_score2 * 0.2
weighted_motor_score1 = motor_score1 * 0.2
weighted_motor_score2 = motor_score2 * 0.2
weighted_frame_score1 = frame_score1 * 0.2
weighted_frame_score2 = frame_score2 * 0.2

# Calcular puntuaciones totales ponderadas (sobre 10)
total_score1 = weighted_price_score1 + weighted_battery_score1 + weighted_motor_score1 + weighted_frame_score1
total_score2 = weighted_price_score2 + weighted_battery_score2 + weighted_motor_score2 + weighted_frame_score2

# Crear un DataFrame para mostrar las puntuaciones
score_data = {
    "Parámetro": ["Precio (40%)", "Capacidad de Batería (20%)", "Potencia del Motor (20%)", "Cadre ENVSO (20%)", "Puntuación Total"],
    "Puntuación Nuestra Bicicleta": [
        f"{weighted_price_score1:.2f}/4.0 ({price_score1:.2f})", 
        f"{weighted_battery_score1:.2f}/2.0 ({battery_score1:.2f})", 
        f"{weighted_motor_score1:.2f}/2.0 ({motor_score1:.2f})", 
        f"{weighted_frame_score1:.2f}/2.0 ({frame_score1:.2f})",
        f"{total_score1:.2f}/10.0"
    ],
    "Puntuación Bicicleta Competidor": [
        f"{weighted_price_score2:.2f}/4.0 ({price_score2:.2f})", 
        f"{weighted_battery_score2:.2f}/2.0 ({battery_score2:.2f})", 
        f"{weighted_motor_score2:.2f}/2.0 ({motor_score2:.2f})", 
        f"{weighted_frame_score2:.2f}/2.0 ({frame_score2:.2f})",
        f"{total_score2:.2f}/10.0"
    ]
}

score_df = pd.DataFrame(score_data)

# Mostrar las puntuaciones
st.subheader("Puntuaciones de Bicicletas (Mayor es Mejor)")
st.write("Usando fórmula: Puntuación = (Valor más bajo × 10) / Valor actual")
st.write("Para batería, motor y tamaño del cuadro, la fórmula se invierte ya que valores más altos son mejores.")
st.write("El precio tiene un peso del 40% de la puntuación total, mientras que los otros parámetros son el 20% cada uno.")
st.table(score_df)

# Determinar el ganador
if total_score1 > total_score2:
    st.success(f"Nuestra Bicicleta tiene una mejor puntuación general: {total_score1:.2f}/10 vs {total_score2:.2f}/10")
elif total_score2 > total_score1:
    st.success(f"Bicicleta Competidor tiene una mejor puntuación general: {total_score2:.2f}/10 vs {total_score1:.2f}/10")
else:
    st.info("¡Ambas bicicletas tienen puntuaciones iguales!")

# Crear un gráfico radar de comparación
st.header("Comparación de Bicicletas")

# Configurar los datos para el gráfico radar
labels = ['Precio', 'Batería', 'Motor', 'Cadre ENVSO']

# Normalizar valores para el gráfico
price_norm_1 = price_range_1 / 5000
battery_norm_1 = battery_capacity_1 / 1000
motor_norm_1 = motor_power_1 / 100
frame_norm_1 = frame_size_1 / 100  # Ahora normalizado de 0-1 directamente

price_norm_2 = price_range_2 / 5000
battery_norm_2 = battery_capacity_2 / 1000
motor_norm_2 = motor_power_2 / 100
frame_norm_2 = frame_size_2 / 100  # Ahora normalizado de 0-1 directamente

values_1 = [price_norm_1, battery_norm_1, motor_norm_1, frame_norm_1]
values_2 = [price_norm_2, battery_norm_2, motor_norm_2, frame_norm_2]

# Crear el gráfico radar de comparación
fig_comp, ax_comp = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

angles = [n / float(len(labels)) * 2 * 3.14159 for n in range(len(labels))]
angles += angles[:1]  # Cerrar el bucle

# Graficar Bicicleta 1
values_1 += values_1[:1]  # Cerrar el bucle
ax_comp.plot(angles, values_1, linewidth=1.5, linestyle='solid', color='blue', label='Nuestra Bicicleta')
ax_comp.fill(angles, values_1, alpha=0.25, color='blue')

# Graficar Bicicleta 2
values_2 += values_2[:1]  # Cerrar el bucle
ax_comp.plot(angles, values_2, linewidth=1.5, linestyle='solid', color='red', label='Bicicleta Competidor')
ax_comp.fill(angles, values_2, alpha=0.25, color='red')

# Establecer propiedades del gráfico
ax_comp.set_thetagrids([a * 180 / 3.14159 for a in angles[:-1]], labels, fontsize=8)
ax_comp.set_ylim(0, 1)
ax_comp.grid(True)
# Ajustar posición y tamaño de la leyenda
ax_comp.legend(loc='upper right', bbox_to_anchor=(1.1, 1.0), fontsize=8)
ax_comp.set_title("Comparación de Nuestra Bicicleta vs Bicicleta Competidor", size=12, pad=10)

# Hacer etiquetas de valor más pequeñas y ajustar posiciones
for i, label in enumerate(labels):
    angle = angles[i]
    # Añadir etiquetas de valor para Bicicleta 1
    ax_comp.text(angle, values_1[i] + 0.03, 
                f"NB: {round(values_1[i] * 100)}%", 
                horizontalalignment='center',
                color='blue',
                fontsize=7)
    # Añadir etiquetas de valor para Bicicleta 2
    ax_comp.text(angle, values_2[i] - 0.03, 
                f"BC: {round(values_2[i] * 100)}%", 
                horizontalalignment='center',
                color='red',
                fontsize=7)

# Ajustar diseño para asegurar que todo encaje
plt.tight_layout()

st.pyplot(fig_comp)

# Añadir una tabla comparando los valores reales
st.subheader("Comparación Numérica")
comparison_data = {
    "Métrica": ["Precio", "Capacidad de Batería", "Potencia del Motor", "Cadre ENVSO"],
    "Nuestra Bicicleta": [f"{price_range_1}€", f"{battery_capacity_1} Wh", f"{motor_power_1} Nm", f"{frame_size_1}%"],
    "Bicicleta Competidor": [f"{price_range_2}€", f"{battery_capacity_2} Wh", f"{motor_power_2} Nm", f"{frame_size_2}%"],
    "Diferencia": [
        f"{abs(price_range_1 - price_range_2)}€", 
        f"{abs(battery_capacity_1 - battery_capacity_2)} Wh", 
        f"{abs(motor_power_1 - motor_power_2)} Nm", 
        f"{abs(frame_size_1 - frame_size_2)}%"
    ]
}
comparison_df = pd.DataFrame(comparison_data)
st.table(comparison_df)

st.markdown("---")
st.markdown("© 2025 Comparador de Bicicletas | Magic Way Innovaciones SL") 