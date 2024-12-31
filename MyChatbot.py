from openai import OpenAI

def is_api_key_valid(client):
    try:
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": 'U r a helpful assistant.'}],
            temperature=0.1,
            top_p=1
        )
        return True
    except Exception as e:
        return False


base_url = ''
api_key = ''
if not base_url:
    print('\nPlease input your api base: ')
    base_url = input().strip()
if not api_key:
    print('\nPlease input your api key: ')
    api_key = input().strip()

client = OpenAI(api_key=api_key,
                base_url=base_url
                )

validation = is_api_key_valid(client)
if validation:
    print('Welcome!\n')
    history = [{
        "role": "system",
        "content": 'U r a helpful assistant.'
    }]
else:
    print('Invalid api base or key. Please retry.')

while validation:
    print(f'<Question>')
    question = input()
    if question.strip() == 'quit' or question.strip() == 'exit':
        print('\n----------------------- Thank you for your use -----------------------\n')
        break
    elif question.strip() == 'clear':
        history = [history[0]]
        print('\nHistory Cleared\n')
    elif question.strip() == 'history':
        print(f'\n<History>\n{history}\n\n')
    else:
        history.append({"role": "user", "content": question})
        print('\n\n<Answer>')
        response = client.chat.completions.create(
            messages=history,
            model='gpt-4o-mini',
            temperature=0.1,
            stream=True
        )
        stream_messages = ""
        for chunk in response:
            delta = chunk.choices[0].delta
            if delta.content:
                stream_message = delta.content
                stream_messages += stream_message
                print(stream_message, end='')
        print('\n\n')
        history.append({"role": "assistant", "content": stream_messages})
