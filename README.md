# MCP Think As

## Prerequisites

- python: e.g. `mise install python@3.13 && mise use python@3.13 -g`
- uv: e.g. `brew install uv`

## Configure

```
git clone https://github.com/ktrysmt/mcp-think-as
cd ./mcp-think-as
uv sync
```

and add `mcp.json` to your mcp config like this:

```
{
  "mcpServers": {
    "mcp-think-as": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-think-as",
        "run",
        "main.py"
      ]
    }
  }
}
```

## Reference

* <https://www.anthropic.com/engineering/claude-think-tool>
* <https://github.com/PhillipRt/think-mcp-server>
* <https://github.com/TechNavii/mcp_think>
