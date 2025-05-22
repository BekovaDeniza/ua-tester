import asyncio
import logging
from random import choice

import aiofiles
from curl_cffi.requests import AsyncSession

write_lock = asyncio.Lock()
semaphore = asyncio.Semaphore(200)

async def write_result(msg: str, file_name: str = 'result.txt'):
    async with write_lock:
        async with aiofiles.open(file_name, 'a', encoding='utf-8') as f:
            await f.write(msg)


async def fetch_url(url: str, headers: dict, proxy: str | None, impersonate: str | None, cookies: dict, output_file: str):
    async with semaphore:
        async with AsyncSession() as session:
            try:
                kwargs = {
                    "headers": headers,
                    "impersonate": impersonate,
                    "cookies": cookies,
                    "timeout": 30
                }

                if proxy:
                    kwargs["proxy"] = proxy

                response = await session.get(url, **kwargs)
                status = response.status_code
                text = response.text[:1000]

            except Exception as e:
                status = 'ERR'
                text = str(e)

            msg = f'{status} | {impersonate} | {proxy} | {headers}\n{text}\n{"-"*60}\n'
            await write_result(msg, output_file)
            logging.info(f'{status} | {impersonate} | {headers}')
