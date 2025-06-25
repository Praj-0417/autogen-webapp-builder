from sendToAgent import callAgentAPI
from divideWork import run_developer, run_designer, get_App_js
import json
from app_build_script import run_command # log_progress
from errorhandling import debug_build_error
from app import update_build_script
from catch_error import run_command_with_logging
import os
from deploy_script import deploy_
from dotenv import load_dotenv
load_dotenv()


NAME = input("Enter the project name: ")
PATH = os.path.join(os.getcwd(), 'user_generated', NAME)
USERNAME = os.getenv("GITHUB_USERNAME")

prompt = input("Enter the prompt: ")
run_command(f"npx create-react-app {NAME} --template typescript", cwd=os.path.join(os.getcwd(), 'user_generated'))
update_build_script(os.path.join(PATH, "package.json"))
project_manager_agent = "orchestrate-tech"
agent1_op = callAgentAPI(project_manager_agent, prompt)['response']
# json.dump(agent1_op, open('agent_op/agent_output.json', 'w'))

des_files = run_designer(agent1_op, PATH)
dev_files = run_developer(agent1_op, PATH)
app_file = get_App_js(agent1_op, PATH)

flag = False
count = 0

while not flag and count < 10:
    try:
        if count >= 10:
            print("Build Failed. Exiting")
            # log_progress("Build Failed. Exiting", PATH)
            print("Final Error Log:")            
            with open(f"{PATH}/error_log.txt", 'r') as f:
                print(f.read())
            break

        run_command_with_logging(f"npm run build", cwd=PATH)
        print("Build Successful")
        # log_progress("Build Successful", PATH)
        flag = True

        print("Deploying the app...")
        # log_progress("Deploying the app...", PATH)
        deploy_(PATH, USERNAME, NAME)

    except Exception as e:
        count += 1
        print("Build Failed. Analyzing the error...")
        # log_progress("Build Failed. Analyzing the error...", PATH)

        with open(f"{PATH}/error_log.txt", 'r') as f:
            error_log = f.read()

        file_contents = {}
        all_files = list(set(des_files + dev_files + app_file))
        for file in all_files:
            with open(PATH+file, 'r') as f:
                file_contents[file] = f.read()
        
        updated_files = debug_build_error(error_log, file_contents)

        for file_path, content in updated_files.items():
            print(f"Updating: {file_path}")
            # log_progress(f"Updating: {file_path}", PATH)
            with open(PATH+file_path, 'w') as f:
                f.write(content)
