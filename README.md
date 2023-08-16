```
  _____                 _             _______              _            
 |  __ \               | |           |__   __|            (_)           
 | |__) | __ _   _  ___| |__   __ _     | | ___  ___ _ __  _  ___ __ _  
 |  ___/ '__| | | |/ _ \ '_ \ / _` |    | |/ _ \/ __| '_ \| |/ __/ _` | 
 | |   | |  | |_| |  __/ |_) | (_| |    | |  __/ (__| | | | | (_| (_| | 
 |_| _ |_|   \__,_|\___|_.__/ \__,_|    |_|\___|\___|_| |_|_|\___\__,_| 
    | \ | |                                                             
    |  \| | _____  _____  ___   _____      __                           
    | . ` |/ _ \ \/ / _ \/ __| / __\ \ /\ / /                           
    | |\  |  __/>  < (_) \__ \ \__ \\ V  V /                            
    |_| \_|\___/_/\_\___/|___/ |___/ \_/\_/      
```

# Misión

Se solicita desarrollar un sistema en el cual el usuario por medio de una archivo plano (.csv) cargue 
una plantilla de inventario aun DB PostgreSQL se debe tener en cuenta que el archivo deberá 
primero ser cargado a un BlobStorage de Azure y luego de su cargue se deberá crear o actualizar los 
datos en el modelo de la DB sea caso correspondiente para así tener un Log de carga y 
procesamiento del mismo.



# Variables de entorno

Debes definir las siguientes variables:

- DB_USER: Corresponde al usuario con el que se maneja la base de datos alojada en Azure.
- DB_PASSWORD: Corresponde a la constraseña de la base de datos alojada en Azure.
- DB_HOST: Corresponde al host en el que esta alojada la base de datos.
- DB_NAME:  Corresponde a un nombre especifico que se asignó la base de datos a la cual vamos a conectar la aplicación.
- STORAGE_ACCOUNT_CS: Corresponde a los valores necesarios para la conexión de un container específico.
- CONTAINER_NAME: nombre del contenedor al que se desea conectar.

# Correr aplicación con Docker-compose

1. Navegar hasta el directorio raiz de la aplicación.

2. Correr la aplicación y levantar contenedor para los andpoints:

```bash
docker-compose up --build -d
```

# Correr aplicación de manera local

1. Crear entorno virtual:

```bash
python3  -m venv env
```

2. Activar el entorno virual:

```bash
python -m env/Script/activate
```

3. Instalar las dependencias necesarias:

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
```

4. Correr la aplicación y levantar servidor para los andpoints:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 80
```


