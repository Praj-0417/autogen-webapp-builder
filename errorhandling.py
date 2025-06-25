from typing import Dict
import json
from sendToAgent import callAgentAPI
import subprocess
import os


def debug_build_error(error_message: str, files: Dict[str, str], path) -> Dict[str, str]:

    prompt = {
        "error_message": error_message,
        "files": files
    }    
    print(f"Sending files to debugger-agent with Error Message: {error_message}")
    response = callAgentAPI('debugger-agent', prompt)['response']

    json.dump(response, open(f'{path}/debugger_output.json', 'w'))
    
    # Parse response and update files
    fixes = response["fixes"]
    updated_files = {}
    
    for fix in fixes:
        print(f"To fix: {fix['file_path']}")
        updated_files[fix["file_path"]] = fix["updated_code"]
    
    return updated_files
