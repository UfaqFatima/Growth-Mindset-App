import streamlit as st
import random

st.title("🌟 Growth Mindset App")
st.write("Short steps of a report")

# Steps of report
steps = [
    "Choose a Topic: Pick a clear and specific topic for your report.",
    "Know the Purpose: Understand why you're writing the report (to inform, analyze, or suggest).",
    "Research Information: Gather facts, data, or details from reliable sources.",
    "Make an Outline: Plan the structure: introduction, body, and conclusion.",
    "Write the Introduction: Start with a short intro explaining the topic and purpose.",
    "Write the Body: Add details, facts, or analysis in short paragraphs.",
    "Write the Conclusion: Summarize the main points or give suggestions.",
    "Add Headings and Subheadings: Use headings to keep things clear and organized.",
    "Check Grammar and Spelling: Read again and fix any mistakes.",
    "Add References: List the sources you used at the end.",
]

# Button and display logic
if st.button("Get Start!"):
    random_step = random.choice(steps)
    st.markdown(f"💬 **{random_step}**")

    st.subheader("Four Short Steps")
    st.write("📌 Pick a clear topic to write about")
    st.write("📌 Find good information or facts about your topic")
    st.write("📌 Start with an introduction about your topic")
    st.write("📌 End with a short conclusion or suggestion")

    st.markdown("---")

# Footer
st.markdown(
    "<div style='text-align: center; padding: 10px; color: #FF0000;'>Made with love by Ufaq Fatima🚀</div>",
    unsafe_allow_html=True
)
