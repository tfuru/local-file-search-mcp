import os
import sys
import asyncio
from pathlib import Path

from bs4 import BeautifulSoup
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# .nev を読み込んで PATH 環境変数を設定
load_dotenv()

# 環境変数から HTML_DATA_PATH を取得
html_data_path = os.getenv("HTML_DATA_PATH")

data_path = os.path.join(os.path.dirname(__file__), f'data/{html_data_path}')
soup = BeautifulSoup(open(data_path, encoding='utf-8'), 'html.parser')

# ここで ホスト 0.0.0.0 を指定して FastMCP サーバーを起動する必要がある
mcp = FastMCP("local-file-search-mcp", host="0.0.0.0", transport="sse")

# @mcp.tool(
#     name="hello_world",
#     description="Returns a greeting message with the provided name."
# )
# async def hello_world(name: str) -> str:
#     return f"Hello, {name}!"

# BeautifulSoup を使って HTML データを解析
@mcp.tool(
    name="search",
    description="Searches for a term in the HTML data and returns matching elements."
)
async def search(term: str) -> list:
    results = []
    for element in soup.find_all(string=lambda text: term.lower() in text.lower()):
        results.append(str(element))
    return results

if __name__ == "__main__":
    mcp.run()