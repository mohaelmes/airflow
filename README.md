# Airflow
Configuración de Apache Airflow con Docker

**Archivos del proyecto**  

*1. docker-compose.yml*  

Este archivo contiene la configuración para Docker Compose, incluyendo la imagen de Airflow, el puerto de acceso y la carpeta de DAGs.  

*2. Dockerfile*  

Este archivo define cómo construir la imagen personalizada de Airflow, incluyendo la copia de los DAGs.    

![image](https://github.com/mohaelmes/airflow/assets/158450254/7cc4a8a8-8e1a-4bcc-9c03-19f03ec8ac07)


*3. dags/prueba.py*  

Este archivo contiene un DAG de prueba que incluye una tarea dummy que no hace nada, solo sirve como prueba.  

![image](https://github.com/mohaelmes/airflow/assets/158450254/0b7a97e2-5787-4b65-bdb6-ce2b6cec9d59)


# Pasos para ejecutar el proyecto

**1. Crear la carpeta del proyecto:**

```bash
mkdir airflow-docker-project
cd airflow-docker-project
```

**2. Crear los archivos docker-compose.yml, Dockerfile y el DAG de prueba (archivos adjuntos)**

**3. Levantar los contenedores con Docker Compose:**

```bash
docker-compose up
```
**4. Acceder a la interfaz web de Airflow:**

Abre tu navegador y ve a http://localhost:8080 para acceder a la interfaz web de Airflow.

**5. Ejecutar el DAG de prueba:**

En la interfaz web de Airflow, activa y ejecuta el DAG prueba_dag.
