import os
from enum import Enum
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sealights")

SL_DOMAIN = os.environ["SL_DOMAIN"]


class TokenType(Enum):
    API = "SEALIGHTS_API_TOKEN"
    AGENT = "SEALIGHTS_AGENT_TOKEN"


async def make_request(url: str, token_type: TokenType) -> dict[str, Any] | None:
    token = os.environ[token_type.value]
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(e)
            return None


if __name__ == "__main__":
    mcp.run(transport="stdio")
