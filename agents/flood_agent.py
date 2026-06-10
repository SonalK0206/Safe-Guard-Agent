from groq_client import client

def flood_response(user_query):

    prompt = f"""
    You are a Flood Preparedness Expert.

    User Query:
    {user_query}

    Provide:
    1. Risk Assessment
    2. Preparedness Measures
    3. Emergency Actions
    4. Recovery Steps
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role":"user",
            "content":prompt
        }]
    )

    return response.choices[0].message.content