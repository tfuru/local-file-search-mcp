import asyncio
from mcp import ClientSession

from mcp.client.stdio import stdio_client, StdioServerParameters
# transport を sse に変更する場合は、以下のようにインポートを変更
from mcp.client.sse import sse_client

# stdio クライアントを使用する場合のメイン
async def main_stdio():
    # サーバスクリプトを起動
    # fastmcp run server.py --transport stdio
    params = StdioServerParameters(command="fastmcp", args=["run","server.py","--transport","stdio"])

    # async with を使って stdio_client を起動・管理
    async with stdio_client(params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # ツール呼び出し: hello_world
            # result = await session.call_tool("hello_world", {"name": "MCP"})
            # print("Tool result:", result.content)
            # ツール呼び出し: search
            search_term = "$.onStart"
            search_results = await session.call_tool("search", {"term": search_term})
            print(f"Search results for '{search_term}':", search_results.content)

# sse クライアントを使用する場合のメイン
async def main_sse():
    # サーバスクリプトを起動
    # fastmcp run server.py --transport sse
    params = "http://127.0.0.1:8000/sse"

    # async with を使って sse_client を起動・管理
    async with sse_client(params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # ツール呼び出し: hello_world
            result = await session.call_tool("hello_world", {"name": "MCP"})
            print("Tool result:", result.content)
            # ツール呼び出し: search
            search_term = "onStart"
            search_results = await session.call_tool("search", {"term": search_term})
            print(f"Search results for '{search_term}':", search_results.content)

if __name__ == "__main__":
    asyncio.run(main_sse())
    # asyncio.run(main_stdio())