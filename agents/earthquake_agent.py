from groq_client import client

def earthquake_response(user_query):

    prompt = f"""
    You are an Earthquake Safety Expert.

    User Query:
    {user_query}

    Explain:
    - Before Earthquake
    - During Earthquake
    - After Earthquake
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role":"user",
            "content":prompt
        }]
    )

    return response.choices[0].message.content