# devcontainerPythonGUIWM - Visual Studio Code devcontainer for Python and tkinter

## Sample Dev Container file(s) for Python and tkinter  in VS Code Containerized Development

*assumptions*: Docker and VS Code installed as well as the Dev Containers extension for Visual Studio Code.

*usage*: clone the repo then open in Visual Studio Code.

*example*:  clone the repo; open a new VS Code window; open the directory containing this repo; when prompted, choose Reopen in Container. 

This devcontainer is based on the latest Python 3 image (`mcr.microsoft.com/devcontainers/python:3`).

`tk` is installed by `post-create.sh`.

The following line in the `devcontainer.json` allows us to run a Python Tkinter GUI application from inside a VS Code devcontainer installation.

```jsonc
    "runArgs": ["-e DISPLAY=$DISPLAY"]
```

## Run the Sample Code

In the `sample` directory, run this command:

```bash
python tk_test.py
```

### miscellany

`configit.sh` looks like this:

```bash
#!/bin/bash

git config --global user.email "yourEmail@mail.com"
git config --global user.name "yourGitUserName"
git config --global push.autoSetupRemote true

git config --global --add safe.directory $1
```
