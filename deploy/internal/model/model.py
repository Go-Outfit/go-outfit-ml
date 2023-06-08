RecommenderRequestBody = {
    "type": "object",
    "properties": {
        "gender": {
            "type": "string"
        },
        "weather": {
            "type": "string"
        },
        "situation": {
            "type": "string"
        },
        "fashion_style": {
            "type": "string"
        },
    },
    "required": ["gender", "weather", "situation", "fashion_style"]
}
