"""
This is a streamlit script for a small webapp that creates a ChatGPT coding project prompt.
"""

import streamlit as st


st.title("Coding project prompt")


usecase = ["school","college","portfolio","other"]

languages = ["python","javascript","java","C","lua","ruby","C++","C#","Visual Basic","Pascal"]


topics = ["loops","if/else","object oriented programming","input/output(text based)","functions","reading/writing files","language specific magic", "strings", "integers","float","arrays","binary trees","search trees"]



#with st.expander("advanced settings"):






class prompt_builder:
    def __init__(self, set_size, language, usecase, file_number, topics, min_size=0, max_size=100, include_topics=[], exclude_topics=[]):
        self.set_size = set_size
        self.__min_size = min_size
        self.__max_size = max_size
        self.language = language
        self.usecase = usecase
        self.file_number = file_number
        self.topics = topics
        self.__include_topics = include_topics
        self.__exclude_topics = exclude_topics

    def set_min_size(self,min_size):
        self.__min_size = min_size

    def set_max_size(self,max_size):
        self.__max_size = max_size

    def set_include_topics(self, include_topics):
        self.__include_topics = include_topics

    def set_exclude_topics(self, exclude_topics):
        self.__exclude_topics = exclude_topics

    def build_prompt(self):
        """
        this method generates the final prompt
        """
        if self.set_size:
            project_size = f"The project should also be about {self.__min_size} - {self.__max_size} lines of code (this is important!)"
        else:
            project_size = ""

        if self.topics:
            include = "The project should use these technologies: " + ", ".join(self.__include_topics)
            exclude = "The project should not use these technologies: " + ", ".join(self.__exclude_topics)
        else:
            include = ""
            exclude = ""
        technologies = include + exclude



        

        prompt = f"Create a coding project for {self.usecase} in the {self.language} programming language. The project should consist of {self.file_number} files . The project should be creative and fun or useful (possible a game or some useful application). {project_size} {technologies} Add comments in the code to explain what is happening and give me only the code as well as a title for the project and a short description of what it does."
        return prompt



