# server.py
from mcp.server.fastmcp import FastMCP
import random

# Create an MCP server
mcp = FastMCP("diceroll")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dice roll tool
@mcp.tool()
def roll_dice(faces: int = 6, rolls: int = 1) -> str:
    """Roll a dice"""
    result = []
    for i in range(rolls):
        result.append(random.randint(1, faces))

    total = sum(result)

    if rolls == 1:
        return str(total)

    expr = " + ".join(str(r) for r in result)
    return f"{expr} = {total}"


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
