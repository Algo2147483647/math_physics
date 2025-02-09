import asyncio
import subprocess
import os


def open_typora(path):
    # 使用 asyncio 创建子进程
    os.system(
        "C:\\Software\\Typora\\Typora.exe " + path
    )


async def open_typora_2(path):
    # 使用 asyncio 创建子进程
    process = await asyncio.create_subprocess_exec(
        "C:\\Software\\Typora\\Typora.exe", path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # 等待子进程结束
    stdout, stderr = await process.communicate()

    if process.returncode == 0:
        print("Typora opened successfully")
    else:
        print(f"Error: {stderr.decode()}")