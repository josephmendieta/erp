# ERP Project

Este proyecto es un sistema de gestión empresarial (ERP) desarrollado con Django que permite administrar ventas y analizar datos relacionados con las mismas.

## Funcionalidades básicas

- **Control de ventas:** Permite visualizar un resumen de las ventas realizadas, incluyendo detalles como la tienda, el barrio, el total de la venta, el dinero recibido, el cambio, la cantidad de artículos vendidos, la fecha de la venta y el nombre del vendedor.

- **Gráficas de ventas:** Ofrece gráficas interactivas que muestran información relevante sobre las ventas, como el número de productos vendidos por vendedor y la relación entre el dinero recibido y el cambio por vendedor.

- **Análisis por barrio y mes:** Proporciona gráficas que muestran la distribución de ventas por barrio y la evolución de las ventas mensuales.

## Instrucciones de ejecución

1. Clona el repositorio: `git clone https://github.com/tu_usuario/erp-project.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Realiza las migraciones de la base de datos: `python manage.py migrate`
4. Carga los datos iniciales (opcional): `python manage.py loaddata initial_data.json`
5. Ejecuta el servidor: `python manage.py runserver`
6. Accede a la aplicación en tu navegador: `http://localhost:8000/`

¡Listo! Ahora puedes explorar y utilizar el ERP project en tu entorno local.
