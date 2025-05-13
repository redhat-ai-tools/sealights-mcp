# sealights-mcp

MCP server for SeaLights

## Running with Podman or Docker

You can run the ocm-mcp server in a container using Podman or Docker:

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
        "-e", "SL_DOMAIN",
        "-e", "SEALIGHTS_API_TOKEN",
        "-e", "SEALIGHTS_AGENT_TOKEN",
        "quay.io/maorfr/sealights-mcp"
      ],
      "env": {
        "SL_DOMAIN": "https://your-domain.sealights.co",
        "SEALIGHTS_API_TOKEN": "REDACTED",
        "SEALIGHTS_AGENT_TOKEN": "REDACTED"
      }
    }
  }
}
```

Replace `REDACTED` with the tokens according to https://api-doc.sealights.io/#authorization.
