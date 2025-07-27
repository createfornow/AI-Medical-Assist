from typing import Iterable
import base64
import os
from groq import Groq
from groq.types.chat.chat_completion_message_param import ChatCompletionMessageParam
from dotenv import load_dotenv

load_dotenv()

#Step1: Convert image to required format (bytes to string)----------

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# image_path="acne.jpg"
# encoded_image=encode_image(image_path)
# image_file=open(image_path, "rb")
# encoded_image=base64.b64encode(image_file.read()).decode('utf-8')
# image_file.close()

# query="Is there something wrong with my face?"
# model="meta-llama/llama-4-maverick-17b-128e-instruct"
# model="meta-llama/llama-4-scout-17b-16e-instruct"

#Step2: Setup Multimodal LLM -----------------

def  analyze_image_with_query(query, model, encoded_image):
  
    client=Groq(api_key=os.environ.get("GROQ_API_KEY")) 
    messages:Iterable[ChatCompletionMessageParam]=[ 
        {
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text":query
                },
                {
                    "type":"image_url",
                    "image_url":{
                        "url":f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ] 

    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

