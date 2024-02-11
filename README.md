# Python GUI Devcontainer

This devcontainer setup has been tested in Visual Studio Code on Windows 11 Pro.

It is based on the latest Python 3 image (`mcr.microsoft.com/devcontainers/python:3`).

`tk` is installed by `post-create.sh`.

The following line in the `devcontainer.json` allows us to run a Python Tkinter GUI application on Windows 11 Pro from inside a VS Code devcontainer installation.

```jsonc
    "runArgs": ["-e DISPLAY=$DISPLAY"]
```
