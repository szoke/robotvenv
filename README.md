# Robot Framework with Virtual Environments and Visual Studio Code

This repository is a quick proof of concepts about how Robot Framework, virtual environments and Visual Studio Code can be used together smoothly.

The goal is to be able to navigate between Robot libraries, resources and test cases and run tests in Visual Studio Code.

## Setup

Let's see how to set your development environment to be able to do so.

- Clone the Repository
- Navigate to the repository root folder
- Create a new virtual environment and activate it (It is important to create it in the repository root or else VS Code seems to not find it)

```
python3 -m venv venv
echo "*" > ./venv/.gitignore
source ./venv/bin/activate
```

- Install the dependencies into the virtual environment

```
pip install -r requirements.txt
```

## Working with Visual Studio Code

- Start Visual Studio
- A pop up will be shown asking if you want to use the newly created virtual environment for the workspace
- Click 'Yes'
- (Alternatively, you can select the interpreter manually)
- If not installed, install the Python extension from Microsoft
- If not installed, install the Robot Framework Language Server extension from Robocorp

The Robot Framework Language Server will need extra configuration of the Python module search path in order to see the dependencies and be able to navigate between Robot keywords.

The paths to external packages and internal packages and modules must be added to the `robot.pythonpath` setting in the `.vscode/settings.json` file.

```
{
    "robot.pythonpath": [
        "${workspaceFolder}",
        "${workspaceFolder}/aszokepackage",
        "${workspaceFolder}/venv/lib/python3.10/site-packages"
    ]
}
```

## Running Tests in Terminal

To run Robot tests in a terminal, you have to add the paths to internal packages and modules to the `PYTHONPATH` environment variable. (The `.vscode/settings.json` file has no effect in this case.)

```
export PYTHONPATH=./aszokepackage:$PYTHONPATH
```
Then run the test like this

```
robot test.robot
```