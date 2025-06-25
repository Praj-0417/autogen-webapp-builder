import subprocess
import os
import sys
from datetime import datetime

def run_command_with_logging(command: str, cwd: str = None) -> None:
    """Run command and log all output including compilation errors"""
    errors = []
    current_error_block = []
    
    try:
        print(f"Running command: {command}")
        process = subprocess.Popen(
            command,
            shell=True,
            cwd=cwd or os.getcwd(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        while True:
            output = process.stdout.readline()
            if output:
                line = output.strip()
                print(line)
                
                # Detect compilation failures and TypeScript errors
                if any(trigger in line for trigger in [
                    "Failed to compile",
                    "ERROR in",
                    "TS",
                    "error",
                    "Error:"
                ]):
                    current_error_block.append(line)
                # If we were collecting an error block and hit an empty line, save it
                elif not line and current_error_block:
                    errors.extend(current_error_block)
                    current_error_block = []
                # Keep collecting lines if we're in an error block
                elif current_error_block:
                    current_error_block.append(line)
            
            err = process.stderr.readline()
            if err:
                line = err.strip()
                print(f"Error: {line}", file=sys.stderr)
                errors.append(line)
            
            if output == '' and err == '' and process.poll() is not None:
                # Don't forget any remaining error block
                if current_error_block:
                    errors.extend(current_error_block)
                break
        
        # Write errors to log file if any were found
        if errors and cwd:
            with open(os.path.join(cwd, 'error_log.txt'), 'w') as f:
                f.write('\n'.join(errors))
            print(f"\nErrors have been logged to: {os.path.join(cwd, 'error_log.txt')}")
            
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, command)
            
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")
        if errors:  # Make sure we write errors even if the command failed
            with open(os.path.join(cwd, 'error_log.txt'), 'w') as f:
                f.write('\n'.join(errors))
        raise

# Usage
if __name__ == "__main__":
    NAME = 'abnhihorha_f828ad'
    PATH = f'/home/arka/Desktop/Hackathons/KrackHack25/myCodes/user_generated/{NAME}/'
    run_command_with_logging("npm run build", cwd=PATH)
