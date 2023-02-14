import streamlit as st




st.title("ChatGPT prompts")
st.sidebar.success("Select prompt generator")


st.subheader("This app generates ChatGPT prompts for specific usecases")
st.caption("The different prompt generators can be accessed via the sidebar")
st.caption("If you have more ideas on what prompt generators to add feel free to submit a PR on github.")
st.caption("Project on github: https://github.com/fabischw/prompt-generator")


st.markdown("### Current prompt generators include:")
st.markdown("- coding project - generate a prompt for coding projects")
st.markdown("- travel guide - generate a prompt for compiling a plan what to do at your destination")