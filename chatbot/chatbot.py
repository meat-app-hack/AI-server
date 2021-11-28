import openai
import os

def manage_sensitive(name):
    v1 = os.getenv(name)
    
    secret_fpath = f'/run/secrets/{name}'
    existence = os.path.exists(secret_fpath)
    
    if v1 is not None:
        return v1
    
    if existence:
        v2 = open(secret_fpath).read().rstrip('\n')
        return v2
    
    if all([v1 is None, not existence]):
        return KeyError(f'{name}')

openai.api_key = manage_sensitive(name='api_key')

print(openai.api_key)

completion = openai.Completion()

start_chat_log = '''Human: Hello, who are you?
AI: I am doing great. How can I help you today?
'''

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'


