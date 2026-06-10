from groq_client import client

def emergency_plan(user_query):

    prompt = f"""
    Generate a Family Emergency Plan.

    Information:
    {user_query}

    Include:
    - Emergency contacts
    - Meeting points
    - Essential supplies
    - Communication plan
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role":"user",
            "content":prompt
        }]
    )

    return response.choices[0].message.content