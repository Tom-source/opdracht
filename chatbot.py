import os
import chainlit as cl
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint

# Ensure the Hugging Face API key is set in the environment
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

# Initialize the Hugging Face model endpoint
llm = HuggingFaceEndpoint(
    repo_id="TomW9/fine_tuned_gpt2",  #My own trained model based on AI act data
)

# Define the prompt template
prompt_template = PromptTemplate(
    input_variables=['user_input'],
    template="You are an expert in the AI act. Answer the following question: {user_input}"
)

# Initialize the LLMChain
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

@cl.on_message
def main(user_message: str):
    # Generate response from the model
    response_message = llm_chain.run(user_input=user_message)
    cl.Message(content=response_message).send()

#to run this script
# chainlit run chatbot.py -w in the terminal