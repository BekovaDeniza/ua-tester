# 🕵️‍♂️ UA Tester

Инструмент для асинхронного тестирования того, как веб-страница реагирует на различные комбинации **User-Agent**, **impersonate**-режимов и **прокси**.

Используется библиотека [`curl_cffi`](https://github.com/yifeikong/curl_cffi) с поддержкой `impersonate`, а также `asyncio` для высокой параллельности запросов.

---

## 🚀 Возможности

- Асинхронные запросы с поддержкой до 200 одновременных соединений
- Поддержка `impersonate` (на базе Chrome, Safari, Edge и др.)
- Ротация `User-Agent` заголовков и `proxy`
- Поддержка форматов прокси: `ip:port:user:pass` и `http(s)://user:pass@ip:port`
- Запись логов в отдельный файл `logs.txt`
- Гибкое управление через аргументы CLI


## 🛠 Установка

1. Клонируй репозиторий:

```bash
git clone https://github.com/BekovaDeniza/ua-tester.git
cd ua-tester
````

2. Создай виртуальное окружения и установи зависимости:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📄 Пример `proxylist.txt`

```txt
127.0.0.1:8080:user:pass
http://user:pass@10.10.10.10:3128
# Комментарии и пустые строки игнорируются
```

---

## 🧪 Пример использования

### Базовый запуск:

```bash
python -m ua_tester.main --url "https://example.com"
```

### С конкретными impersonate:

```bash
python -m ua_tester.main --url "https://example.com" --impersonate-only chrome,safari15_3
```

### Без прокси:

```bash
python -m ua_tester.main --url "https://example.com" --no-proxy
```

### С выводом в другой файл:

```bash
python -m ua_tester.main --url "https://example.com" --output results.txt
```

---

## ⚙️ Аргументы командной строки

| Аргумент                    | Назначение                                                                   |
| --------------------------- | ---------------------------------------------------------------------------- |
| `--url` / `-u`              | *(обязательный)* URL для тестирования                                        |
| `--no-proxy` / `-n`         | Отключить использование прокси                                               |
| `--output` / `-o`           | Указать имя файла для вывода результатов (по умолчанию: `result.txt`)        |
| `--impersonate-only` / `-i` | Указать конкретные impersonate (через запятую) — пример: `chrome,safari15_3` |

