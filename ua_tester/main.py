import argparse
import asyncio
import itertools
import os
from random import choice

from ua_tester.client import fetch_url
from ua_tester.config import impersonate_list as default_impersonate_list, headers_list
from ua_tester.proxy import load_proxies
from ua_tester.logger import setup_logger

setup_logger()

def parse_args():
    parser = argparse.ArgumentParser(description="User-Agent and impersonation tester")

    parser.add_argument(
        "--no-proxy", "-n",
        action="store_true",
        help="Запустить без использования прокси"
    )
    parser.add_argument(
        "--url", "-u",
        type=str,
        required=True,
        help="URL, к которому выполнять запросы"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="result.txt",
        help="Имя файла для вывода результатов (по умолчанию result.txt)"
    )
    parser.add_argument(
        "--impersonate-only", "-i",
        type=str,
        help="Список impersonate, разделённый запятыми (пример: chrome,safari15_3)"
    )

    return parser.parse_args()

async def main():
    args = parse_args()

    url = args.url
    output_file = args.output

    # Определение списка impersonate
    if args.impersonate_only:
        impersonate_list = [i.strip() for i in args.impersonate_only.split(',') if i.strip()]
    else:
        impersonate_list = default_impersonate_list

    cookies = {}

    if os.path.exists(output_file):
        os.remove(output_file)

    proxies = load_proxies('proxylist.txt') if not args.no_proxy else [None]

    tasks = []
    for impersonate, headers in itertools.product(impersonate_list, headers_list):
        proxy = choice(proxies)
        task = fetch_url(url, headers, proxy, impersonate, cookies, output_file)
        tasks.append(asyncio.create_task(task))

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
