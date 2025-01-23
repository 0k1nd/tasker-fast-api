# Docker
## Развёртка проекта в докере:

### Создать файл с окружением:

```
cp example.env .env
```

### Открыть и заполнить .env

```
nano .env
```

## Запуск проекта в докере:
```
docker compose up --build
```

## Остановка:
```
docker compose down
```

## Уронить докер вместе с бд:
```
docler compose down -v
```

# Fast-API

