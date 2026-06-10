import streamlit as st
import sqlite3
from risk_agent import location_risk
from router import route_query
from preparedness_score import calculate_score

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="SafeGuard AI",
    page_icon="🚨",
    layout="wide"
)

# ----------------------------------
# Header
# ----------------------------------

st.title("🚨 SafeGuard AI")
st.subheader("AI-Powered Disaster Preparedness Assistant")

st.markdown("""
Stay informed and prepared for disasters such as:

- 🌊 Floods
- 🌍 Earthquakes
- 🔥 Fires
- 📋 Emergency Planning

Ask any disaster-related question below.
""")

st.divider()

# ----------------------------------
# Disaster Assistant
# ----------------------------------

st.header("🤖 Disaster Assistant")

query = st.text_area(
    "Enter your question",
    placeholder="Example: What should I do during a flood?"
)

if st.button("Get Advice"):

    if query.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Analyzing situation..."):

            response = route_query(query)

        # Save chat history

        conn = sqlite3.connect("safeguard.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO chat_history
        (query, response)
        VALUES (?, ?)
        """, (query, response))

        conn.commit()
        conn.close()

        st.success("Response Generated")

        st.markdown(response)

st.divider()

# ----------------------------------
# Preparedness Assessment
# ----------------------------------

st.header("📊 Disaster Preparedness Assessment")

name = st.text_input("Enter Your Name")

location = st.text_input("Enter Your Location")

st.write("Answer the following questions:")

q1 = st.checkbox("Emergency Kit Available?")
q2 = st.checkbox("Power Backup Available?")
q3 = st.checkbox("Emergency Contacts Saved?")
q4 = st.checkbox("First Aid Kit Available?")
q5 = st.checkbox("Flashlight Available?")
q6 = st.checkbox("Emergency Food Supply Available?")
q7 = st.checkbox("Drinking Water Stored?")
q8 = st.checkbox("Battery Radio Available?")
q9 = st.checkbox("Emergency Medicines Available?")
q10 = st.checkbox("Family Emergency Meeting Point Planned?")

if st.button("Calculate Preparedness Score"):

    if not name.strip() or not location.strip():
        st.error("Please enter both Name and Location.")
        st.stop()

    answers = [
        int(q1),
        int(q2),
        int(q3),
        int(q4),
        int(q5),
        int(q6),
        int(q7),
        int(q8),
        int(q9),
        int(q10)
    ]

    score = calculate_score(answers)

    # Save to Database

    conn = sqlite3.connect("safeguard.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users (name, location, preparedness_score)
    VALUES (?, ?, ?)
    """, (name, location, score))

    conn.commit()
    conn.close()

    st.subheader(f"Preparedness Score: {score:.0f}%")

    # Show Risk Assessment

    risk_report = location_risk(location)

    st.markdown("### 📍 Area Risk Assessment")

    st.write(risk_report)

    # Preparedness Verdict
    if score >= 80:

        st.success("🟢 Excellent Preparedness")

        st.write("""
        You appear well prepared for emergencies.
        Continue updating your emergency supplies and plans regularly.
        """)

    elif score >= 50:

        st.warning("🟡 Moderate Preparedness")

        st.write("""
        You have basic preparedness measures in place.
        Consider improving your emergency readiness.
        """)

    else:

        st.error("🔴 High Risk")

        st.write("""
        Your preparedness level is low.
        Build an emergency kit and emergency plan as soon as possible.
        """)

st.divider()

# ----------------------------------
# View Saved Assessments
# ----------------------------------

st.header("📁 Previous Assessments")

if st.button("Show Assessment History"):

    conn = sqlite3.connect("safeguard.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name, location, preparedness_score
    FROM users
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    if rows:

        for row in rows:

            st.write(
                f"👤 {row[0]} | 📍 {row[1]} | 📊 {row[2]:.0f}%"
            )

    else:

        st.info("No assessments found.")

st.divider()
st.divider()

# ----------------------------------
# Chat History
# ----------------------------------

st.header("💬 Disaster Query History")

if st.button("Show Chat History"):

    conn = sqlite3.connect("safeguard.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT query, response, created_at
    FROM chat_history
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    if rows:

        for row in rows:

            st.markdown(f"### ❓ Query")
            st.write(row[0])

            st.markdown("### 🤖 Response")
            st.write(row[1])

            st.caption(f"🕒 {row[2]}")

            st.divider()

    else:

        st.info("No chat history found.")
# ----------------------------------
# Footer
# ----------------------------------

st.markdown("""
---
### About SafeGuard AI

SafeGuard AI helps individuals and families prepare for disasters through:

- Disaster Awareness
- Emergency Planning
- Preparedness Assessment
- Safety Guidance

""")