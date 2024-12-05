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

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=history,
            temperature=0.1,
            top_p=1
        )
        print(f'\n\n<Answer>\n{response.choices[0].message.content}\n\n')
        history.append({"role": "assistant", "content": response.choices[0].message.content})
