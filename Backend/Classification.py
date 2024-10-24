from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from ChainOfThoughts import chian_of_thoughts_response_product_query

# Loaded all the secret keys
load_dotenv()


# created openai instance to interact with the openai models
LLM = ChatOpenAI(model="gpt-4o-mini")

string_parser = StrOutputParser()
json_parser = JsonOutputParser()


def service_classification(user_input):
    system_prompt = """ You wil be provided with customer service queries. The customer service queries will be delimited with {delimiter} charachters.
          Your task is to Classify each query into a primary category and a secondary category based on the provided catagories below.
                Primary categories: Billing, Technical Support,
                Account Management, or General Inquiry.

                Billing secondary categories:
                Unsubscribe or upgrade
                Add a payment method
                Explanation for charge
                Dispute a charge

                Technical Support secondary categories:
                General troubleshooting
                Device compatibility
                Software updates

                Account Management secondary categories:
                Password reset
                Update personal information
                Close account
                Account security

                General Inquiry secondary categories:
                Product information
                Pricing
                Feedback
                Speak to a human

                Finaly you should provide your output in json format with the
                keys: primary and secondary.
                """
    classification_prompt = ChatPromptTemplate.from_messages(
        [("system", f"{system_prompt}"),
         ("user", "{delimiter}{user_input}{delimiter}")])

    classification_chain = classification_prompt | LLM | json_parser

    final_response = classification_chain.invoke(
        {"user_input": user_input, "delimiter": "###"})

    if final_response["primary"] == "General Inquiry":
        return chian_of_thoughts_response_product_query(user_input, final_response)
    else:
        return final_response["primary"]
