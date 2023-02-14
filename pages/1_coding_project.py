"""
This is a streamlit script for a small webapp that creates a ChatGPT coding project prompt.
"""

import streamlit as st


st.title("Coding project prompt")


usecase = ["school","college","portfolio","work","fun"]

languages = ["python","javascript","java","C","lua","ruby","C++","C#","Visual Basic","Pascal","HTML","CSS"]


topics = ["loops","if/else","object oriented programming","input/output(text based)","functions","reading/writing files","language specific magic", "strings", "integers","float","arrays","binary trees","search trees"]




class prompt_builder:
    def __init__(self, language, usecase, topics, min_size, max_size, include_topics, exclude_topics):
        self.min_size = min_size
        self.max_size = max_size
        self.language = language
        self.usecase = usecase
        self.topics = topics
        self.__include_topics = include_topics
        self.__exclude_topics = exclude_topics


    def build_prompt(self):
        """
        this method generates the final prompt
        """

        project_size = f"The project should also be about {self.min_size} - {self.max_size} lines of code (this is important!)"


        if self.topics:
            include = "The project should use these technologies: " + ", ".join(self.__include_topics)
            exclude = "The project should not use these technologies: " + ", ".join(self.__exclude_topics)
        else:
            include = ""
            exclude = ""
        technologies = include + exclude



        

        prompt = f"Create a coding project for {self.usecase} in the {self.language} programming language. The project should be creative and fun or useful (possible a game or some useful application). {project_size} {technologies} Add comments in the code to explain what is happening and give me only the code as well as a title for the project and a short description of what it does."
        return prompt









with st.form("Prompt Generator",clear_on_submit=False):
    usecase = st.selectbox("REQUIRED: Select what the project is for",options=usecase)

    language = st.selectbox("REQUIRED: Select the programming language",options=languages)

    language2 = st.text_input("OPTIONAL: Insert alternative programming language / technology here, leave empty if a language was selected")

    include = st.multiselect("OPTIONAL: Select topics that should be included in the project",options=topics)
    exclude = st.multiselect("OPTIONAL: Select topics that should be excluded in the project", options=topics)

    lines = st.slider("OPTIONAL: project size(lines of code)", 0, 1000, (50, 100))


    submitted =  st.form_submit_button("Generate prompt")
    if submitted:

        with st.spinner("Please wait ..."):
            if language2 != "":
                language = language2



            if include == [] or exclude == []:
                topics = False
            else:
                topics = True

            prompt_generate = prompt_builder(language, usecase, topics, lines[0], lines[1], include, exclude)

            prompt = prompt_generate.build_prompt()

            st.markdown("Copy your prompt below:")
            st.code(prompt)









