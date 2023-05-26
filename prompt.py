from sys import argv, exit as abort
from os import getenv as ENV
import openai

openai.api_key = ENV("OPENAI_KEY")


def get_file_content(file_name: str) -> str:
    with open(f"{file_name}", "r") as file: return file.read()


def prompt_with(tests:str) -> list[dict]: 
    return [
        {"role": "system", "content": "You are a programmer using TDD"},
        {"role": "user", "content": "Which language do you use?"},
        {"role": "assistant", "content": "I use python"},
        {"role": "user", "content": "Which test framework do you use?"},
        {"role": "assistant", "content": "I use pytest"},
        {
        "role": "user", 
         "content": f"""
         Implement the code tested in the tests provided so that all pass.
         Include nothing else in your reply, as it will be written 
         directly to a single source code file.

         The tests are as follows:
         ```
         {tests}
         ```

         """
        }
    ]


def generate_code(
    tests: str,
    model: str = "gpt-3.5-turbo",
) -> str:
    messages = prompt_with(tests)
    response = openai.ChatCompletion.create(
            model=model, 
            messages=messages
    )['choices'][0]['message']['content']

    return response.replace('```python', '').replace('```', '')


def write_file_content(file_name: str, content: str = "") -> None:
    try:
        with open(f"{file_name}", "w") as file: 
            file.write(content)
    except:
        print("Something has gone wrong... have a look anyways:")
        print(content)


def main():
    dir_name: str
    try:
        dir_name = argv[1] 
    except:
        print("You should specify a directory...")
        abort()
    tests = get_file_content(f"{dir_name}/test.py")
    code = generate_code(tests)
    print(code)
    write_file_content(f"{dir_name}/src.py", code)
    print("...And done!")


__name__ == "__main__" and main()

