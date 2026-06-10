from groq_client import client

def fire_response(user_query):

    prompt = f"""
    You are a Fire Safety Expert.

    User Query:
    {user_query}

    Provide:
    - Fire prevention
    - Emergency response
    - Evacuation guidance
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role":"user",
            "content":prompt
        }]
    )

    return response.choices[0].message.content