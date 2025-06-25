
# Autogen-WebApp-Builder

## Introduction

Autogen-WebApp-Builder is an autonomous system that takes a simple user prompt and builds a complete React-based web application from scratch. It intelligently orchestrates different AI agents to design, develop, debug, and deploy the app — all without human intervention.

The final result is a live, working website hosted via GitHub Pages.

---

## Agent-Based Architecture

This project uses a multi-agent framework where each agent has a specific responsibility:

- **Orchestrator Agent**: Interprets the user prompt, decides folder structure and tech stack, and delegates tasks.
- **Designer Agent**: Generates frontend UI components based on structure and design intent.
- **Developer Agent**: Writes functional frontend/backend logic (primarily frontend).
- **Debugger Agent**: Iteratively analyzes build errors and fixes them.
- **Deployment Agent**: Automates the GitHub deployment process (build, push, configure GitHub Pages).

---

## Features

- Supports React.js with TypeScript
- Autonomous debugging loop with error resolution
- Automated deployment using GitHub Actions
- Outputs a live deployment URL after successful build

---

## Tech Stack

- Python
- React (TypeScript)
- GitHub CLI
- Agent.ai API
- GitHub Actions

---

## Project Structure

```
autogen-webapp-builder/
├── templates/               # HTML templates
├── app.py                   # Core application interface
├── app_build_script.py      # Scripts to run builds
├── catch_error.py           # Build error catcher
├── deploy_script.py         # Deployment logic
├── deploy.yml               # GitHub Actions workflow
├── divideWork.py            # Handles agent-wise task division
├── errorhandling.py         # Debugger agent logic
├── main.py                  # Entry script (user prompt, loop)
├── sendToAgent.py           # API handler for Agent.ai
├── .env.example             # Template for environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### Environment Variables

Create a `.env` file in your root directory and add the following:

```
TOKEN=your_github_pat
GITHUB_USERNAME=your_github_username
AGENT_API_KEY=your_agent_ai_key
```

Make sure your GitHub token has `repo`, `workflow`, and write permissions.

---

### Prerequisites

Ensure the following are installed:

- Python 3.8+
- pip
- npm and npx
- GitHub CLI (`gh`)

---

### GitHub CLI Setup

```
gh auth login
```

---

### Node.js Check

```
npm -v
npx -v
```

If not installed:

```
winget install OpenJS.NodeJS
```

---

## How To Use

1. Clone the Repository

```
git clone https://github.com/Praj-0417/autogen-webapp-builder.git
cd autogen-webapp-builder
```

2. Create Virtual Environment (optional)

```
python -m venv venv
venv\Scripts\activate       # On Windows
# or
source venv/bin/activate    # On macOS/Linux
```

3. Install Python Requirements

```
pip install -r requirements.txt
```

4. Run the Application

```
python main.py
```

Then follow the prompts:

- Enter your project name
- Enter your prompt (e.g., "Create a portfolio website")

The system will:

- Scaffold the project
- Call agents
- Retry builds if needed
- Deploy automatically

5. After Success

A deployment URL is printed — your live site hosted via GitHub Pages.

---

## Deployment Flow

- Auto-deploys via `gh-pages` branch
- `deploy.yml` GitHub Actions workflow triggers on push
- Deployment is pushed to:
  https://<your-username>.github.io/<repo-name>/

---

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 Pranav Raj

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

---

## Contributions

Pull requests and issues are welcome. If you improve the logic, agent workflows, or error handling, feel free to fork and contribute back.
