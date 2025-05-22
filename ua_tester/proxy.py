import logging

def load_proxies(file_name: str) -> list[str]:
    proxies = []

    with open(file_name, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()

            if not line or line.startswith('#'):
                continue  # пропускаем пустые строки и комментарии

            if line.startswith("http://") or line.startswith("https://"):
                proxies.append(line)
                continue

            parts = line.split(':')
            if len(parts) == 4:
                ip, port, user, password = parts
                formatted = f"http://{user}:{password}@{ip}:{port}"
                proxies.append(formatted)
            else:
                logging.warning(f"Строка {line_num} в proxylist.txt имеет некорректный формат: '{line}'")

    if not proxies:
        raise ValueError("Файл прокси пустой или все строки имеют неправильный формат.")

    return proxies
