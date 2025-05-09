#!/usr/bin/env python
# coding: utf-8

# In[2]:


from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import ResponseSchema
from langchain.schema.output_parser import StrOutputParser


# In[3]:


prompt = PromptTemplate(
    template="""
You are a restaurant assistant. Based on the following inputs, recommend a dish:
- Cuisine preference: {cuisine}
- Dietary restriction: {diet}

Provide a response strictly in JSON format:
{{
    "dish": "<dish>",
    "cuisine": "<cuisine>",
    "diet": "<diet>"
}}
""",
    input_variables=["cuisine", "diet"],
)


# In[7]:


response_schemas = [
    ResponseSchema(name="dish", description="Recommended dish based on preferences"),
    ResponseSchema(name="cuisine", description="Cuisine category of the recommended dish"),
    ResponseSchema(name="diet", description="Dietary considerations for the dish"),
]
output_parser = StrOutputParser()


# In[8]:


llm = ChatOpenAI(model="gpt-4-0613", temperature=0)


# In[9]:


chain = LLMChain(llm=llm, prompt=prompt, output_parser=output_parser)


# In[10]:


input_data = {"cuisine": "Italian", "diet": "vegetarian"}
result = chain.run(input_data)


# In[11]:


parsed_result = output_parser.parse(result)


# In[12]:


print("Dish Recommendation:", parsed_result)

