"""
from model import pipe

def foo(user_message):

    question = user_message

    messages = [
        {"role": "user", "content": question},
    ]

    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    outputs = pipe(prompt, max_new_tokens=100)[0]  
    generated_text = outputs["generated_text"]
    return generated_text

"""