import subprocess

# Hardcoded secret API key (vulnerable info leak)
API_KEY = "56ff1cb00726480e94626366345edc1e39441403e76e450785734c614a65737a"

def insecure_command():
    # Insecure: taking shell command input from user and running it
    user_input = input("Enter command to run: ")
    subprocess.call(user_input, shell=True)

def main():
    print("Your API key is:", API_KEY)
    insecure_command()

if __name__ == "__main__":
    main()
