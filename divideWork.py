from sendToAgent import callAgentAPI

def saveToFile(file_path, content):
    import os
    directory = os.path.dirname(file_path)  
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    lines = content.splitlines()
    if len(lines) > 1:
        content = "\n".join(lines[1:-1])  # Keep only the middle lines
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def code_strip(code):
    lines = code.splitlines()
    if len(lines) > 1:
        return "\n".join(lines[1:-1])  # Keep only the middle lines
    return code

def run_designer(response, _path):
    designer_tasks = response['agent_tasks']['designer_agent']
    frontend_structure = response['file_structure']['frontend']
    paths = []

    for idx, task in enumerate(designer_tasks):
        # designer_tasks[idx]['frontend_general_structure'] = frontend_structure
        print(f"Calling designer-agent on: {task['component_path']}")
        # log_progress(f"Calling designer-agent on: {task['component_path']}", _path)

        code = callAgentAPI('design-tech', task)['response']
        path = task['component_path']
        paths.append(path)
        saveToFile(_path+path, code)

    return paths


def run_developer(response, _path):
    developer_tasks = response['agent_tasks']['developer_agent']
    backend_structure = response['file_structure']['backend']
    paths = []

    for idx, task in enumerate(developer_tasks):
        # developer_tasks[idx]['backend_general_structure'] = backend_structure
        if "App.tsx" in task['file_path']:
            continue


        path = task['file_path']
        paths.append(path)

        # check if path (file) already exists
        import os.path
        if os.path.exists(_path+path):
            with open(_path+path) as file:
                task['existing_code'] = file.read()

        print(f"Calling developer-agent on: {task['file_path']}")   
        # log_progress(f"Calling developer-agent on: {task['file_path']}", _path) 
        code = callAgentAPI('develop-tech', task)['response']

        saveToFile(_path+path, code)

    return paths

def get_App_js(response, _path):
    code = callAgentAPI('app-tsx', response)['response']
    path = '/src/App.tsx'
    # log_progress(f"Calling app-tsx agent on: {path}", _path)
    saveToFile(_path+path, code)

    return [path]
