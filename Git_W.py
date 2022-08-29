import subprocess
from enum import Enum

class GitCommand(Enum):
    ADD = 0
    COMMIT = "git commit -m \"{}\""
    ORIGIN = "https://github.com/IshchukI/Lesson20DZSubprocess.git"


class RusultCode(Enum):
    OK = 0
    ERROR = 1


def git_init():
    init = subprocess.run("git init",
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding="utf-8")
    print(init.stdout)

def git_add_origin():
    add_origin = subprocess.run("git remote set-url origin {}".format(GitCommand.ORIGIN.value),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding="utf-8")

    check_origin = subprocess.run("git remote -v",
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding="utf-8")
    print(check_origin.stdout)


def git_create_branch():
    branch = subprocess.run("git branch -M main",
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding="utf-8")



def git_status():
    status = subprocess.run("git status",
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding="utf-8")
    return status

def git_add():
    add = subprocess.run("git add .",
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding="utf-8")
    return add


def git_commit(message):
    commit_result = subprocess.run(GitCommand.COMMIT.value.format(message),
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   encoding="utf-8")
    return commit_result

def git_push():
    commit_result = subprocess.run("git push origin main",
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   encoding="utf-8")
    # return git_push()


status = git_status()
if ("fatal: not a git repository" in status.stdout):
    print("--->git is still uninitialized")
    print("--->git  uninitializing")
    git_init()
    git_add_origin()
    git_create_branch()
    status = git_status()

if ("Untracked files" in status.stdout or "Changes not staged for commit:" in status.stdout or "Changes to be committed:" in status.stdout):
    add = git_add()
    print("add ok")
    commit_result = git_commit("first try")
    print("commit ok")
    git_push()
    print("push ok")
else:
    print("no changes in files")








