import openai
import os

OPENAI_API_KEY='OPENAI_API_KEY'

def main():
    openai.api_key = os.getenv(OPENAI_API_KEY)

    if openai.api_key == None:
        print("OPENAI_API_KEY")
        exit(-1)

    print("PyChat v0.1")
    query = input('Input: ')

    print("Query: {}".format(query))
    
    completion = openai.Completion.create(engine="text-davinci-003", prompt=query, max_tokens=4000)

    output = completion.choices[0].text

    print("Output: {}".format(output))

if __name__ == '__main__':
    main()