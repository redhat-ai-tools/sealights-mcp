# sealights-mcp

MCP server for SeaLights

## Running with Podman or Docker

You can run the sealights-mcp server in a container using Podman or Docker:

Example configuration for running with Podman:

```json
{
  "mcpServers": {
    "sealights": {
      "command": "podman",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "SEALIGHTS_DOMAIN",
        "-e", "SEALIGHTS_API_TOKEN",
        "-e", "SEALIGHTS_AGENT_TOKEN",
        "quay.io/maorfr/sealights-mcp"
      ],
      "env": {
        "SEALIGHTS_DOMAIN": "https://your-domain.sealights.co",
        "SEALIGHTS_API_TOKEN": "REDACTED",
        "SEALIGHTS_AGENT_TOKEN": "REDACTED"
      }
    }
  }
}
```

## Running with non-stdio transport

To run the server with a non-stdio transport (such as SSE), set the `MCP_TRANSPORT` environment variable to a value other than `stdio` (e.g., `sse`).

Example configuration to connect to a non-stdio MCP server:

```json
{
  "mcpServers": {
    "slack": {
      "url": "https://sealights-mcp.example.com/sse",
      "headers": {
        "X-Sealights-Api-Token": "REDACTED",
        "X-Sealights-Agent-Token": "REDACTED"
      }
    }
  }
}
```

Replace `REDACTED` with your API token according to https://api-doc.sealights.io/#authorization.

## Available Tools

- `get_apps()`: Get list of applications.
- `get_audit_log_actions()`: Get a list of all actions recorded in the audit log.
- `get_branches(app_name, visibility="visible")`: Get list of branches for a specific application.
- `get_build_coverage(bsid)`: Get coverage data for a specific build by Build Session ID (bsid).
- `get_build_metadata(bsid)`: Get detailed metadata for a specific build by Build Session ID (bsid).
- `get_builds(app_name="", branch_name="")`: Get list of builds for a specific application and/or branch.
- `get_live_agents()`: Get all live agents.
