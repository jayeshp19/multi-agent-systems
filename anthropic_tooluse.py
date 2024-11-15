import anthropic
from anthropic.types import TextBlock

client = anthropic.Client(api_key = "api_key")

tools = [
    {
        "name": "get_weather",
        "description": "",
        "input_schema": {
            "type": "object",
            "location": {
                "required": True,
                "description": "The location to get the weather for",
                "type": "string",
            },
        },
    }
]

message = [
    {"role": "user", "content": [{"type": "text", "text": "(empty)"}]},
    {
        "role": "assistant",
        "content": [
            TextBlock(
                text=" Hello from the weather station. Would you like to know the weather? If so, tell me your location.",
                type="text",
            )
        ],
    },
    {"role": "user", "content": [TextBlock(text="London and Delhi.", type="text")]},
]


with client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    system= "You are a weather assistant. You will provide weather information for a given location, you can use multiple tool calls at once",
    messages=message,
    tools=tools,
    stream=True,
) as stream:
  for text in stream:
      print(text)
