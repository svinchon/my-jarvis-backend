from fastmcp import Client

async def get_next_train_time(
    origin: str,
    destination: str
):
    client = Client("http://localhost:8000/mcp")
    async with client:
        result = await client.call_tool(
            "get_next_train_time",
            {
                "origin": origin,
                "destination": destination
            }
        )
        return result
