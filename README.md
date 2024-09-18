# App Backend Samy - Carrito de Compras.

Este es un sistema de gestión de carritos de compras con funcionalidades para crear, actualizar, eliminar elementos y generar facturas.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Arquitectura](#arquitectura)
- [Uso](#uso)
- [Rutas de la API](#rutas-de-la-api)
- [Configuración](#configuración)
- [Pruebas](#pruebas)

## Descripción

Este proyecto es una Api que permite gestionar un carrito de compras desde la creación de productos o eventos, agregar items al carrito, gestionar el stock de los mismos, hasta generar una factura.


## Arquitectura

El proyecto está diseñado utilizando una arquitectura hexagonal (también conocida como arquitectura de puertos y adaptadores), lo que asegura una separación clara entre la lógica de negocio y las dependencias externas. Esta arquitectura promueve la modularidad y facilita el mantenimiento y las pruebas del sistema.

Se tuvo en cuenta el concpto de arquitecturas limpias: POO(Pramación orientada a objetos), Pratones de dinseño y principios solid.

Además se implementó la metodología TDD(Test-Driven Development) es una metodología de desarrollo de software en la que las pruebas se escriben antes de escribir el código que implementa la funcionalidad,
esto mejora la calidad del código, facilita el diseño, detecta errores y documentan el código.


FYI: Este tipo de arquitecturas es recomendada para proyectos grandes que evolucionan en el tiempo, pero en esta prueba técnica fue implementado para demostrar mis habilidades con estos conceptos modernos de programación.

## Ejemplo de Arquitectura

Componentes Principales
- Dominio (domain):
Entidades: Representan los conceptos fundamentales del negocio. En este proyecto, las entidades pueden incluir Cart, Item, etc.
Descripción: Contiene la lógica de negocio esencial y las entidades que reflejan el modelo del dominio.

- Casos de Uso (use_cases):
Descripción: Define las operaciones o acciones que la aplicación puede realizar. Los casos de uso están organizados en módulos según el dominio, como eventos, productos y carrito de compras.
Ejemplos: create_event_use_case.py, add_item_to_cart_case_use.py.

- Puertos (ports):
Descripción: Interfaces que definen cómo el núcleo de la aplicación interactúa con servicios externos. Se dividen en puertos de entrada (para casos de uso) y puertos de salida (para repositorios).
Repositorios: Incluyen interfaces para acceder a datos, como cart_repository.py, event_repository.py.

- Adaptadores (adapters):
Descripción: Implementan los puertos para conectar la aplicación con el mundo exterior. Los adaptadores de entrada podrían ser controladores de API, mientras que los adaptadores de salida podrían ser repositorios concretos que interactúan con la base de datos.
Ejemplos: Repositorios para MongoDB (mongodb_repository.py), manejo de excepciones (exceptions.py).

- Drivers (drivers):
Descripción: Facilitan la interacción con la aplicación desde el usuario o sistemas externos. En este proyecto, los drivers son las interfaces REST que permiten a los clientes realizar solicitudes a la API.
Ejemplos: main.py, routers/product.py.

- Servicios (services):
Descripción: Componentes que proporcionan funcionalidades específicas, como la generación de PDF en pdf_service.py.

- Tests (tests):
Descripción: Contienen pruebas unitarias e integración para validar el funcionamiento de la lógica de negocio y los adaptadores. Las pruebas se organizan en pruebas unitarias y de integración.
Ejemplos: create_event_use_case_test.py, mongodb_product_repository_test.py.

```plaintext
├── app
│   ├── adapters
│   ├── domain
│   ├── drivers
│   ├── ports
│   ├── services
│   └── tests
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md
└── requirements.txt
```

### Requisitos

- **Python 3.12 o superior**: Asegúrate de tener instalada una versión compatible de Python.
- **FastAPI**: La API está construida utilizando el framework FastAPI.
- **MongoDB en Docker**: La base de datos MongoDB está gestionada a través de contenedores Docker.
- **Dockerizado**: El proyecto está completamente dockerizado para facilitar su despliegue y ejecución.


## Pasos para la Instalación

### 1. Clonar el Repositorio

Clona el repositorio desde GitHub utilizando el siguiente comando:

    ```bash
    git clone git@github.com:JhonSoto99/shopping_cart_fast_api_clean_architecture.git
    cd shopping_cart
    ```

### 2. Construir Levantar Contenedores

Para construir e iniciar los contenedores Docker necesarios, ejecuta:

    ```bash
    docker-compose build

    docker-compose up -d
    ```

Este comando levantará los contenedores para el backend y las instancias de MongoDB definidas en el archivo `docker-compose.yml`.

### 4. Ejecutar la Aplicación

Una vez que los contenedores estén en funcionamiento, la aplicación estará disponible en `http://localhost:8080` (o el puerto especificado en tu configuración).

### 5. Ejecutar Pruebas

Para ejecutar las pruebas unitarias del proyecto, utiliza el siguiente comando:

    ```bash
    pytest
    ```

Asegúrate de tener `pytest` instalado en tu entorno para ejecutar las pruebas.

### 6. Documentación de la API

La documentación interactiva de la API estará disponible en:

- [Swagger UI](http://localhost:8080/docs)
- [ReDoc](http://localhost:8080/redoc)

## Notas Adicionales

- **MongoDB**: Verifica que los contenedores de MongoDB estén corriendo correctamente. Puedes usar `docker ps` para comprobar el estado de los contenedores.
- **Configuraciones Especiales**: Consulta el archivo `docker-compose.yml` y los archivos de configuración dentro de la carpeta `app` si necesitas realizar configuraciones adicionales.

Para cualquier problema o duda, consulta la documentación del proyecto o abre un issue en el repositorio.


##  Documentación del Proceso y Mejoras

- **Inicialización del Proyecto**:
Se comenzó creando un proyecto con FastAPI, seleccionando una arquitectura hexagonal para mantener una separación clara entre la lógica de negocio y las dependencias externas. Esta elección permitió una estructura modular y fácil de mantener.

- **Configuración del Entorno**:
Se configuraron los contenedores Docker para el backend y MongoDB, y se preparó un archivo docker-compose.yml para facilitar el despliegue y la ejecución del proyecto.

- **Implementación de Funcionalidades**:
Gestión de Productos y Eventos: Implementación de casos de uso para crear, actualizar y eliminar productos y eventos.
Carrito de Compras: Funcionalidades para agregar, eliminar y actualizar ítems en el carrito.
Generación de Facturas: Generación de facturas a partir de los ítems del carrito.

- **Pruebas y Validación**:
Se utilizaron pruebas unitarias y de integración para asegurar el correcto funcionamiento de la lógica de negocio y los adaptadores.

- **Manejo de Errores**:
Se hixzo uso del intermediario de errores que proporciona FastApi para globalizar la gestion de errores de la Api.

- **Documentación de la API**:
Se integró Swagger UI y ReDoc para proporcionar documentación interactiva de la API, facilitando la comprensión y prueba de los endpoints.

## Puntos Flacos y Problemas Encontrados

Realmente el desarrollo del proyecto no tuvo problemas complejos, pero si tiene puntos de mejora:

- Completar pruebas unitarias y de integración, las pruebas quedaron en un 70% faltó el otro 30% 
no se completaron por temas de tiempos, pero resalto que las pruebas son un infaltable para terminar el desarollo.

- Para el manejo de errores identifiqué que faltó unificar algunas excpeciones compartidas, entre eventos, productos y el carrito
manejar un nombre genérico para usarlas en alguno de los 3 casos. No se hizo por temas de tiempo.

- Faltó implementar la lógica para guardar una imagen del producto o evento, actualmente se guarda un str.  No se termino por temas de tiempo. 

## Nuevas Funcionalidades

- Agregar un sistema de autorizacón y autenticación a la Api.
- Asociar un carrito de compras a  un usuario
- Gestion de pago y envío de los items
- Persistr el carrito de compras en base de datos(Actualmente solo se persiste en tiempo de ejecución)
- Y muchas otras mejoras más.