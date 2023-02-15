import streamlit as st




st.title("ChatGPT prompts")
st.sidebar.success("Select prompt generator")

st.sidebar.write("Find the source code on [Github](https://github.com/fabischw/prompt-generator)")
st.sidebar.write("Made by [fabischw](https://github.com/fabischw)")


st.subheader("This app generates ChatGPT prompts for specific usecases")
st.caption("The different prompt generators can be accessed via the sidebar")



st.markdown("### Current prompt generators include:")
st.markdown("- coding project - generate a prompt for coding projects")
st.markdown("- travel guide - generate a prompt for compiling a plan what to do at your destination")