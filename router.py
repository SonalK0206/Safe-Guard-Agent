from agents.classifier import classify_disaster
from agents.flood_agent import flood_response
from agents.earthquake_agent import earthquake_response
from agents.fire_agent import fire_response
from agents.emergency_agent import emergency_plan


def route_query(query):

    category = classify_disaster(query)

    valid_categories = [
        "Flood",
        "Earthquake",
        "Fire",
        "Cyclone",
        "Heatwave",
        "Emergency Plan",
        "Out of Scope"
    ]

    if category not in valid_categories:
        category = "Out of Scope"

    print("Detected Category:", category)

    if category == "Flood":
        return flood_response(query)

    elif category == "Earthquake":
        return earthquake_response(query)

    elif category == "Fire":
        return fire_response(query)

    elif category == "Emergency Plan":
        return emergency_plan(query)

    elif category == "Out of Scope":
        return """
        🚨 SafeGuard AI specializes in disaster preparedness and emergency planning.

        Please ask questions related to:
        • Floods
        • Earthquakes
        • Fires
        • Emergency Preparedness
        """

    else:
        return "Unable to classify the query."