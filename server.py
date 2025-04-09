# server.py
from mcp.server.fastmcp import FastMCP
import random
import uuid

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


# Add a UUID generation tool
@mcp.tool()
def generate_uuid(version: int = 4) -> str:
    """Generate a random UUID"""
    if version == 4:
        return str(uuid.uuid4())
    elif version == 1:
        return str(uuid.uuid1())
    else:
        raise ValueError(f"UUID version {version} not supported")


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
