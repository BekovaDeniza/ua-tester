# User-Agent Tester for Web Parsers

Этот проект предназначен для массового тестирования различных `User-Agent` заголовков и браузерных имитаций через библиотеку `curl_cffi`. Он помогает определить, какие конфигурации успешно проходят проверку на целевом веб-сайте.

## 🔧 Возможности

- Асинхронный HTTP-клиент
- Поддержка до 200 одновременных запросов
- Тестирование с прокси
- Имитация различных браузеров (`impersonate`)
- Логирование результатов

## 📦 Установка

```bash
git clone https://github.com/your-repo/ua-tester.git
cd ua-tester
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

## 🚀 Запуск

1. Подготовьте файл `proxylist.txt` в формате:

   ```
   ip:port:username:password
   ```

2. Запустите скрипт:

```bash
python -m ua_tester.main
```

## 📄 Результаты

Результаты сохраняются в `result.txt` в виде:

```
<status_code> | <impersonate> | <proxy> | <headers>
<first 1000 symbols of response>
------------------------------------------------------------
```

