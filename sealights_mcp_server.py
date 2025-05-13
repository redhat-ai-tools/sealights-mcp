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


async def make_request(
    url: str, token_type: TokenType, params: dict[str, Any] = None
) -> dict[str, Any] | None:
    token = os.environ[token_type.value]
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url, headers=headers, params=params, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(e)
            return None


@mcp.tool()
async def get_apps():
    """Get list of applications."""
    url = f"{SEALIGHTS_API_BASE}/apps"
    return await make_request(url, TokenType.API)


@mcp.tool()
async def get_branches(app_name: str, visibility: str = "visible"):
    """Get list of branches for a specific application."""
    url = f"{SEALIGHTS_API_BASE}/apps/{app_name}/branches"
    params = {}
    if visibility:
        params["visibility"] = visibility
    return await make_request(url, TokenType.API, params)


@mcp.tool()
async def get_builds(app_name: str | None = None, branch_name: str | None = None):
    """Get list of builds. The resulting SlimBuild object only has some metadata. For extended build metadata, see Get Build Metadata."""
    url = f"{SEALIGHTS_API_BASE}/slim-builds"
    params = {}
    if app_name:
        params["appName"] = app_name
    if branch_name:
        params["branchName"] = branch_name
    return await make_request(url, TokenType.API, params)


@mcp.tool()
async def get_build_metadata(bsid: str):
    """Get detailed metadata description for a specific build by Build Session ID (bsid)."""
    url = f"{SEALIGHTS_API_BASE}/builds/{bsid}"
    return await make_request(url, TokenType.API)


@mcp.tool()
async def get_build_coverage(bsid: str):
    """Get coverage data for a specific build by Build Session ID (bsid)."""
    url = f"{SEALIGHTS_API_BASE}/builds/{bsid}/coverage"
    return await make_request(url, TokenType.API)


if __name__ == "__main__":
    mcp.run(transport="stdio")
