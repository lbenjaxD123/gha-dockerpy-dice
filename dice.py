import os
import random

def set_github_action_output(output_name, output_value):
    with open(os.path.abspath(os.environ["GITHUB_OUTPUT"]),"a") as output:
        print(f'{output_name}={output_value}', file=output)

def run():
    dice_numbers = os.getenv("INPUT_DADOS",default=2)
    set_github_action_output("dado1",random.randint(1,6))
    if dice_numbers == 2:
        set_github_action_output("dado2",random.randint(1,6))
        

if __name__ == "__main__":
    run()