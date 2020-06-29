# Visual Studio Code

When you start Visual Studio Code in a folder, that folder becomes your workspace. You can have workspace-specific settings that override your user settings. However, if you only use Visual Studio Code to edit a file, then only your user settings are in effect.

## Features

### IntelliSense

IntelliSense refers to the broad category of features that Visual Studio Code provides to make code editing both easier and more effective for developers. An example of one such feature is smart completion suggestions. Instead of suggesting completions based on the strings that exist in the current file (which is how Vim's native completion suggestion system works), Intellisense suggests completions based on variable types and knowledge of the symbols defined in imported modulesa among other things. These kinds of suggestions are far more comprehensive and useful, which makes the development experience delightful.

IntelliSense is natively supported for JavaScript, TypeScript, JSON, HTML, CSS, SCSS, and Less. One possible reason why IntelliSense is so tightly coupled with web technologies is because Visual Studio Code itself is built using web technologies. In particular, it is based on the Electron framework, which allows the development of desktop GUI applications using web technologies and is the basis of Atom, GitHub Desktop, and WordPress Desktop. You can get IntelliSense for other languages through Extensions.

### Shortcuts

- ⇧⌘P: Show All Commands
- ⇧⌘E: View: Show Explorer
- ⇧⌘F: View: Show Search
- ⌃⌘G: View: Show SCM
- ⇧⌘D: View: Show Run and Debug
- ⇧⌘X: View: Show Extensions
- ⌘K⌘S: Preferences: Open Keyboard Shortcuts
- ⌘P: Go To File ...
- ⇧⌘O: Go To Symbol in Editor ...
- ⌘T: Go To Symbol in Workspace ...

### Debugging

- There are 6 things you can do: Continue, Step Over, Step Into, Step Out, Restart, and Stop.
- There is a Debug Console available in the Panel (where the Integrated Terminal is also found) that allows you to evaluate expressions where your program currently is in execution.
- Visual Studio Code supports Log Points which are an alternative to print statements that show up in the Debug Console instead of the Terminal. The advantage of this is that it does not require making modifications to your code (which you have to remember to revert) and it decouples your debugging messages from your regular program output.
- Instead of always logging something when you reach a particular point in your program, you can hav conditional Log Points based on expression evaluation of hit count. These can be dynamically modified during a debugging session.
- Both Break Points and Log Points in Visual Studio Code persist even after you restart the application.

### Commands

To show all the commands, use the keyboard shortcut ⇧⌘P. Here are some examples:

- Git: Stash
- Git: Commit
- File: New File
- File: New Folder
- View: Toggle Minimap
- View: Toggle Wordwrap
- Debug: Open launch.json
- Debug: Start Debugging
- Markdown: Open Preview
- Markdown: Open Preview to the Side
- Preferences: Open Workspace Settings
- Preferences: Open Workspace Settings (JSON)

## Configuration

- Visual Studio Code uses JSON for all configuration purposes.
- There are two main categories of settings: User and Workspace.
- User the keyboard shortcut ⌘, to access both User and Workspace settings.
- Workplace settings are stored in the file `.vscode/settings.json`.
- Debug settings are stored in the file `.vscode/launch.json`.

## Languages

### Python

- IntelliSense works for standard modules as well as ones you've installed into the environment of the selected Python interpreter; just make sure that you've selected the correct Python interepreter for your workspace.
- Here are some commands the Python extension added to the command palette:
    - Python: Select Interpreter
    - Python: Start REPL
    - Python: Run Python File in Terminal
    - Python: Select Linter
    - Python: Format Document
    - Python: Configure Tests
    - Python: Run All Tests
    - Python Refactor: Sort Imports
- A **linter** is a program that detects both stylistic as well as syntactic errors.
    - The default linter for Python in Visual Studio Code is PyLint, but you can choose a variety of other linters including Bandit, Flake8, and MyPy.
    - By default, linting is enabled (the `python.linting.enabled` setting is `true`), linting is triggered on saving a file (the `python.lintOnSave` setting is `true`), and the maximum number of linting messages is 100 (the `python.linting.maxNumberOfProblems` setting is `100`).
- A **formatter** is a program that only changes how your program looks.
    - The default linter for Python in Visual Studio Code is Autopep8, but you can choose other linters like Black or Yapf.

### C

### C++

### Rust
