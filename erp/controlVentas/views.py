from django.shortcuts import render
from controlVentas.models import resumenVenta
import plotly.express as px
import pandas as pd 

def control(request): 
    ventas = resumenVenta.objects.all()
    contextControl = {
        "ventas": ventas,
    }
    return render(request, "controlVentas/indexControl.html", contextControl)

def graficaVenta(request):
    ventas = resumenVenta.objects.all()

    # Crear un DataFrame a partir de los objetos de ventas
    df_ventas = pd.DataFrame(list(ventas.values()))

    # Agregar el gráfico de barras
    grafico_barras = px.bar(df_ventas, x="nombreVendedor", y="articulosVendidos", 
                             title="Número de Productos Vendidos por Vendedor",
                             labels={"nombreVendedor": "Vendedor", "articulosVendidos": "Cantidad de Productos"},
                             color="nombreVendedor")

    # Agregar el gráfico de dispersión con recibido en el eje x y cambio en el eje y
    grafico_dispersion = px.scatter(df_ventas, x="recibido", y="cambio", 
                                    title="Relación entre Recibido y Cambio por Vendedor",
                                    labels={"recibido": "Recibido", "cambio": "Cambio"},
                                    color="nombreVendedor")

    # Convertir los gráficos a HTML
    html_grafico_barras = grafico_barras.to_html(full_html=False)
    html_grafico_dispersion = grafico_dispersion.to_html(full_html=False)

    contextGraficaV = {
        "grafico_barras": html_grafico_barras,
        "grafico_dispersion": html_grafico_dispersion
    }

    return render(request, "controlVentas/indexGraficasVentas.html", contextGraficaV)

def graficaBarrio(request):
    ventas = resumenVenta.objects.all()

    # Crear un DataFrame a partir de los objetos de ventas
    df_ventas = pd.DataFrame(list(ventas.values()))

    # Convertir la columna de fechaVenta a formato datetime
    df_ventas['fechaVenta'] = pd.to_datetime(df_ventas['fechaVenta'])

    # Agrupar por mes y sumar la cantidad de productos vendidos
    df_mes = df_ventas.groupby(df_ventas['fechaVenta'].dt.strftime('%B'))['articulosVendidos'].sum().reset_index()

    # Ordenar los meses de forma correcta
    meses_ordenados = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_mes['fechaVenta'] = pd.Categorical(df_mes['fechaVenta'], categories=meses_ordenados, ordered=True)
    df_mes = df_mes.sort_values('fechaVenta')

    # Agrupar por barrio y sumar la cantidad de productos vendidos
    df_barrio = df_ventas.groupby('barrioTienda')['articulosVendidos'].sum().reset_index()

    # Agregar el gráfico de pastel
    grafico_pastel = px.pie(df_barrio, values='articulosVendidos', names='barrioTienda', 
                            title='Distribución de Ventas por Barrio')

    # Agregar el gráfico de área apilada de ventas por mes
    grafico_area = px.area(df_mes, x='fechaVenta', y='articulosVendidos', 
                           title='Evolución de Ventas Mensuales', 
                           labels={'fechaVenta': 'Mes', 'articulosVendidos': 'Cantidad de Productos'},
                           color_discrete_sequence=px.colors.qualitative.Pastel)

    # Convertir los gráficos a HTML
    html_grafico_pastel = grafico_pastel.to_html(full_html=False)
    html_grafico_area = grafico_area.to_html(full_html=False)

    contextGraficas = {
        "grafico_pastel": html_grafico_pastel,
        "grafico_area": html_grafico_area
    }

    return render(request, "controlVentas/indexBarrioMes.html", contextGraficas)
