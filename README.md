
## 🚀 Fase 1: Diseño del Proyecto

Estructura Base con Clean Architecture
Clean Architecture se basa en separar responsabilidades en capas bien definidas. 

### 🧠 Clean Architecture: Filosofía General
La Clean Architecture busca aislar las reglas del negocio del resto del sistema (frameworks, bases de datos, entradas/salidas). Así logramos:

* Escalabilidad.
* Bajo acoplamiento.
* Testeabilidad.
* Flexibilidad tecnológica (cambiar DB o framework sin afectar la lógica de negocio).

#### Clean Arquitecture + Screaming

Por " quien eres y tipo"

https://youtu.be/y3MWfPDmVqo?si=kBDOjrv8sA9P5eYn

✅ USUARIO FUNCIONALIDADES
1. Crear usuario
2. Resetear contraseña con código enviado por correo
3. Actualizar usuario
4. Desactivar usuario (activo/inactivo)


### TODO List

- [ ] Autenticacion y Autorizacion de usuarios
- [ ] FRONTEND REACT login usuarios.
- [ ] Crear Dockers and Postgres
- [ ] Crear Orquestador


### Component Test

docker-compose -f docker-compose-dev.yml exec web pytest --verbose tests/

### Docker commands

docker-compose -f docker-compose-dev.yml up -d --build

docker-compose -f docker-compose-dev.yml down -v


#### Develop to docker
Si estas desarrollando algo e instalaste librerias

[ ]  Freeze requirements

No esta refrescando los tests, porque estan fuera de app y docker lee desde app los cambios



### Curl

Registrar usuario
```
curl -X POST http://localhost:8080/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sebastián",
    "last_name": "Navarro",
    "email": "sebastian2@example.com",
    "password": "123456"
  }'
``` 

Authenticar
```
curl -X POST http://localhost:8080/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin3@example.com", "password": "Admin1234!"}'
```

Obtener datos del usuario logeado
```
curl -X GET http://localhost:8080/users/me \
  -H "Authorization: Bearer <TU_ACCESS_TOKEN>"
```

Cambiar role usuario
```
curl -X PATCH http://localhost:8080/users/user@example.com/role \
  -H "Authorization: Bearer <TU_TOKEN_JWT>" \
  -H "Content-Type: application/json" \
  -d '{
    "new_role": "admin"
  }'
```


Crear usuario admin directamente en postgres docker

psql -U postgres -d postgres 

```
INSERT INTO users (name, last_name, email, hashed_password, role, created_at, updated_at)
VALUES (
  'Admin', 
  'User', 
  'admin3@example.com', 
  '$2b$12$6Rhw26nKaZxtIQMtAU95SOlo1TD1S80muazV.jBqgy.L9FoiNf4Xa', 
  'admin', 
  NOW(), 
  NOW()
);
```

password: Admin1234!