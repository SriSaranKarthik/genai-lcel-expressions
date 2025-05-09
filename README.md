## Design and Implementation of LangChain Expression Language (LCEL) Expressions

### AIM:
To design and implement a LangChain Expression Language (LCEL) expression that utilizes at least two prompt parameters and three key components (prompt, model, and output parser), and to evaluate its functionality by analyzing relevant examples of its application in real-world scenarios.

### PROBLEM STATEMENT:
Develop an LCEL-based application to process expressions with dynamic parameters, leveraging a prompt template for structured interaction, a language model to process the input, and an output parser for extracting meaningful results.

### DESIGN STEPS:

#### STEP 1:
Formulate a prompt structure with placeholders for at least two dynamic inputs.

#### STEP 2:
Utilize LangChain's language model to process the prompt and generate a response.

#### STEP 3:
Develop an output parser to retrieve structured data from the model’s response.

### PROGRAM:
```
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import ResponseSchema
from langchain.schema.output_parser import StrOutputParser

# Step 1: Define the PromptTemplate
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

# Step 2: Define the Output Parser
response_schemas = [
    ResponseSchema(name="dish", description="Recommended dish based on preferences"),
    ResponseSchema(name="cuisine", description="Cuisine category of the recommended dish"),
    ResponseSchema(name="diet", description="Dietary considerations for the dish"),
]
output_parser = StrOutputParser()

# Step 3: Initialize the Chat Model
llm = ChatOpenAI(model="gpt-4-0613", temperature=0)

# Step 4: Create the LangChain Expression (LLM Chain)
chain = LLMChain(llm=llm, prompt=prompt, output_parser=output_parser)

# Step 5: Test the Chain with Example Inputs
input_data = {"cuisine": "Italian", "diet": "vegetarian"}
result = chain.run(input_data)

# Step 6: Parse the Structured Output
parsed_result = output_parser.parse(result)

# Step 7: Display the Final Recommendation
print("Dish Recommendation:", parsed_result)

```
### OUTPUT:

![image](https://github.com/user-attachments/assets/585fe28a-e8f3-4cfb-8e65-075db758819b)

### RESULT:
Thus, the program to construct and execute a LangChain Expression Language (LCEL) expression using a minimum of two prompt parameters and three core components (prompt, model, and output parser) has been successfully implemented and tested.

