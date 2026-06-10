from groq_client import client

def classify_disaster(query):

    prompt = f"""
    You are a disaster query classifier.

    Classify the user query into ONLY one of these categories:

    - Flood
    - Earthquake
    - Fire
    - Cyclone
    - Heatwave
    - Emergency Plan
    - Out of Scope

    Examples:

    Query: What should I do during a flood?
    Category: Flood

    Query: Earthquake safety tips
    Category: Earthquake

    Query: How can I prevent house fires?
    Category: Fire

    Query: Create a family emergency plan
    Category: Emergency Plan

    Query: Who won the IPL?
    Category: Out of Scope

    Query: Write a Python program
    Category: Out of Scope

    Query: What is machine learning?
    Category: Out of Scope

    User Query:
    {query}

    Return ONLY the category name.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()