
from universal_mcp.servers.server import SingleMCPServer

from universal_mcp_zenquotes.app import ZenquotesApp

app_instance = ZenquotesApp()

mcp = SingleMCPServer(
    app_instance=app_instance
)

if __name__ == "__main__":
    print(f"Starting {mcp.name}...")
    mcp.run()


