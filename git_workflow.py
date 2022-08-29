import subprocess
from enum import Enum


class RusultCode(Enum):
    OK = 0
    ERROR = 1


class GitCommand(Enum):
    ADD = 0
    COMMIT = "git commit -m {}"


print(GitCommand.COMMIT.value.format('my message'))

def git_commit(message):
    status = subprocess.run("git status",
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding="utf-8")
    if status.returncode == 1:
        print('Something wrong')
    else:
        if 'Changes to be committed:' in status.stdout:
            add_result = subprocess.call("git add .")
            if status.returncode == RusultCode.ERROR:
                print('Something wrong')
            else:
                commit_result = subprocess.run(GitCommand.COMMIT.value.format(message),
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            encoding="utf-8")

        else:
            print("Nothing to commit")



        # git add .