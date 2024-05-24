# Airflow
Configuración de Apache Airflow con Docker

**Archivos del proyecto**  

*1. docker-compose.yml*  

Este archivo contiene la configuración para Docker Compose, incluyendo la imagen de Airflow, el puerto de acceso y la carpeta de DAGs.    
```bash

## Archivos del proyecto

### 1. `docker-compose.yml`

Este archivo contiene la configuración para Docker Compose, incluyendo la imagen de Airflow, el puerto de acceso y la carpeta de DAGs.

```yaml
version: '3.7'
services:
  postgres:
    image: postgres:13
    environment:
      - POSTGRES_USER=airflow
      - POSTGRES_PASSWORD=airflow
      - POSTGRES_DB=airflow
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U airflow"]
      interval: 10s
      retries: 5
      start_period: 30s

  webserver:
    image: apache/airflow:2.3.0
    depends_on:
      - postgres
    environment:
      - AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
    volumes:
      - ./dags:/opt/airflow/dags
    ports:
      - "8080:8080"
    command: webserver

  scheduler:
    image: apache/airflow:2.3.0
    depends_on:
      - postgres
    environment:
      - AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
    volumes:
      - ./dags:/opt/airflow/dags
    command: scheduler
```

*2. Dockerfile*  

Este archivo define cómo construir la imagen personalizada de Airflow, incluyendo la copia de los DAGs.    

![image](https://github.com/mohaelmes/airflow/assets/158450254/f320a32a-df48-4c58-b3d7-ce6b0e0e62c6)



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
