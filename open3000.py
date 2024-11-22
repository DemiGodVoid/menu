import subprocess
import os
import signal
import time

def kill(port):
    try:
        output = subprocess.check_output(["lsof", "-t", f"-i:{port}"])
        pids = output.decode('utf-8').strip().split()
        for pid in pids:
            os.kill(int(pid), signal.SIGKILL)
            print(f"Killed process ID {pid} using port {port}.")
            time.sleep(3)
    except subprocess.CalledProcessError:
        print(f"No process found using port {port}.")
        time.sleep(3)
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(3)

PORT = 3000
kill(PORT)
