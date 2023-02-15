"""
This is a streamlit script for a small webapp that creates a ChatGPT travel guide prompt.
"""

import streamlit as st


st.title("Coding project prompt")
st.sidebar.success("Select prompt generator")



class prompt_builder:
    def __init__(self, destination:str, day_count:int, museum:bool, nature:bool ,multiple_days:bool):
        self.destination = destination
        self.day_count = day_count
        self.museum = museum
        self.nature = nature
        self.multiple_days = multiple_days



    def build_prompt(self):
        """
        this method generates the final prompt
        """

        if not self.museum:
            museum = "do not"
        else:
            museum = "do"

        museum = f"I {museum} want to visit a museum "

        if self.multiple_days:
            multiple_days = f"You may also use multiple days for one activity if required."
        else:
            multiple_days = "Don't do activities that take longer than a day."
        

        prompt = f"I want you to act as my travel guide. My Destination is {self.destination}. I will spend {self.day_count} at the destination. I want you to suggest me things to do at my destination. {museum} Please compile a complete plan for my holidays in {self.destination}. Give me a list with a different idea for each day. {multiple_days}"

        return prompt



with st.form("Prompt Generator",clear_on_submit=False):
    destination = st.text_input("Insert your destination")

    day_count = st.slider("Days you spend at the destination",min_value=0,max_value=60, step=1)

    museum = st.checkbox("Visit Museums")
    nature = st.checkbox("Spend time in nature")
    multiple_days = st.checkbox("Multi-day activities")



    submitted =  st.form_submit_button("Generate prompt")
    if submitted:

        with st.spinner("Please wait ..."):

            prompt_generate = prompt_builder(destination, day_count, museum, nature, multiple_days)

            prompt = prompt_generate.build_prompt()

            st.markdown("Copy your prompt below:")
            st.code(prompt)