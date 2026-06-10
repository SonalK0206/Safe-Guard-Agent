from groq_client import client

def location_risk(location):

    prompt = f"""
    You are a disaster risk analyst.

    For the location {location},
    estimate:

    Flood Risk
    Earthquake Risk
    Fire Risk
    Cyclone Risk

    Return concise results.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content