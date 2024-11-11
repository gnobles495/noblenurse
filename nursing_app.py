import streamlit as st

st.title("Nursing Decision-Making App")
st.write("Welcome to your guided clinical decision-making practice!")

# Add a sample question
st.subheader("Case Scenario")
st.write("A 60-year-old patient is experiencing shortness of breath and chest pain. What would be your first priority?")

# Create options for students to choose
choice = st.radio("Choose an action:", ("Assess vital signs", "Administer oxygen", "Notify the doctor", "Provide reassurance"))

# Provide feedback based on the choice
if choice == "Assess vital signs":
    st.write("Good choice! Assessing vital signs helps determine the patient's current status.")
elif choice == "Administer oxygen":
    st.write("Administering oxygen is important, but assessing vitals should come first to determine the appropriate oxygen need.")
elif choice == "Notify the doctor":
    st.write("Notifying the doctor might be necessary later, but let's first assess the patient's condition with vital signs.")
elif choice == "Provide reassurance":
    st.write("Providing reassurance is helpful, but it’s essential to assess vital signs first.")

