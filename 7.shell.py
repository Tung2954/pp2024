import subprocess
import shlex

def execute_command(command):
    try:
        command_list = shlex.split(command)

        result = subprocess.run(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Output:")
        print(result.stdout)

        if result.stderr:
            print("Errors:")
            print(result.stderr)

    except Exception as e:
        print(f"Error: {e}")
    
def main():
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        if '<' in user_input:
            input_file = user_input.split('<')[1].strip()
            with open(input_file, 'r') as file:
                user_input = file.read()

        if '>' in user_input:
            output_file = user_input.split('>')[1].strip()
            with open(output_file, 'w') as file:
                file.write("Output: \n")
        execute_command(user_input)

if __name__ == "__main__":
    main()