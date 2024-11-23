# web_dz_1

Docker Compose — это инструмент, который позволяет определять и запускать многоконтейнерные Docker-приложения

Запуск приложений

```
docker-compose up -d
```

Остановка приложений

```
docker-compose down
```

Перезапуск приложений

```
docker-compose logs -f
```

Выполнение команд внутри контейнера

```
docker-compose exec <service> bash
```

Масштабирование сервисов

```
docker-compose up --scale web=3
```
