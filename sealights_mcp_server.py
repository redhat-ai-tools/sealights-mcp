import os
from enum import Enum
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sealights")

SEALIGHTS_API_BASE = f"{os.environ['SEALIGHTS_DOMAIN']}/sl-api/v1"


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


@mcp.tool()
async def get_builds():
    """Get list of builds. The resulting SlimBuild object only has some metadata. For extended build metadata, see Get Build Metadata."""
    url = f"{SEALIGHTS_API_BASE}/slim-builds"
    return await make_request(url, TokenType.API)


if __name__ == "__main__":
    mcp.run(transport="stdio")
