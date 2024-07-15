
from openai import OpenAI
import time
import random
#import tiktoken
import logging
import datetime

log = logging.getLogger("assistant")
logger = logging.getLogger(__name__)
logging.basicConfig(filename='assistant.log', level= logging.INFO, encoding='utf-8')

client = OpenAI()

# extract & return response text
def get_response_message(response):
    return response.choices[0].message.content

#extract & return the total number of tokens
def get_response_total_tokens(response):
    return response.usage.total_tokens  

#extract & return the total number of input tokens
def get_response_total_input_tokens(response):
    return response.usage.prompt_tokens

#extract & return the total number of output tokens
def get_response_total_output_tokens(response):
    return response.usage.completion_tokens

#encoding = tiktoken.encoding_for_model(model)
token_input_limit = 12289
total_token_count = 0
total_input_token_count = 0
total_output_token_count = 0

def process_run(thread_id, assistant_id):
    new_run = client.beta.threads.runs.create(
    thread_id = thread_id,
    assistant_id = assistant_id
    )
    
    phrases = ["Thinking", "Pondering", "Dotting the i's and crossing my t's", "Achieving world peace"]

    while True:
        time.sleep(2)
        print(random.choice(phrases) + "...")
        run_check = client.beta.threads.runs.retrieve(
            thread_id = thread_id,
            run_id = new_run.id
        )
        if run_check.status in ["cancelled","failed", "completed", "expired"]:
            return run_check
        
def log_run(run_status):
    if run_status in ["cancelled", "failed", "completed", "expired"]:
        log.error(str(datetime.datetime.now()) + " Run " + run_status + "\n")

# create the assistant
assistant = client.beta.assistants.create(
    name = "Study Buddy",
    model = "gpt-3.5-turbo",
    instructions = "You are a studdy partner for students who are new to technology. When you answer prompts use simple language that will help someone new to web development learn",
    tools=[]
)

thread = client.beta.threads.create()

user_input = " "

while True:
    if (user_input == ""):
        user_input = input("Chatbot: Hey there, I'm here to help. Type exit to end our chat. Otherwise, nice to meet you. What is your name? ")
    else:
        user_input = input("You: ")
    if user_input.lower() == "exit":
        print("\nAssistant: Goodbye, have a wonderful day!")
        log.info("\nDate: " + str(datetime.datetime.now()) + "\nTotal tokens: " + str(total_token_count) + "\nTotal Input tokens: " + str(total_input_token_count) + "\nTotal Output tokens: " + str(total_output_token_count) + "\n\n")
        exit()
        
    message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role = "user",
    content = user_input
    )
    
    run = process_run(thread.id, assistant.id)
    
    log_run(run.status)
    
    if run.status == "completed":
        thread_messages = client.beta.threads.messages.list(
            thread_id = thread.id
        )
        
        print("\nAssistant: " + thread_messages.data[0].content[0].text.value + "\n")
    
    if run.status in ["cancelled", "failed", "expired"]:
        print("\nAssistant: An error has occurred, please try again.\n")

"""thread_messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )
#message_for_user = thread_messages.data[0].content[0].text.value
#print("\nAssistant: " + message_for_user + "\n")"""