# Docker

```sh
docker compose down             --> Eliminar los contenedores
docker compose up -d --build    --> Levantar los contenedores


docker compose down --volumes --remove-orphans
docker compose build --no-cache
docker compose up
```


# Entrar al contenedor

```sh
docker exec -it generator_app bash
docker exec -it generator_scheduler bash
```