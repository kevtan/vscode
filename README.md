# Visual Studio Code

When you start Visual Studio Code in a folder, that folder becomes your workspace. You can have workspace-specific settings that override your user settings. However, if you only use Visual Studio Code to edit a file, then only your user settings are in effect.

## Features

### IntelliSense

IntelliSense refers to the broad category of features that Visual Studio Code provides to make code editing both easier and more effective for developers. An example of one such feature is smart completion suggestions. Instead of suggesting completions based on the strings that exist in the current file (which is how Vim's native completion suggestion system works), Intellisense suggests completions based on variable types and knowledge of the symbols defined in imported modules among other things. These kinds of suggestions are far more comprehensive and useful, which makes the development experience delightful.

IntelliSense is natively supported for JavaScript, TypeScript, JSON, HTML, CSS, SCSS, and Less. One possible reason why IntelliSense is so tightly coupled with web technologies is because Visual Studio Code itself is built using web technologies. In particular, it is based on the Electron framework, which allows the development of desktop GUI applications using web technologies and is the basis of Atom, GitHub Desktop, and WordPress Desktop. You can get IntelliSense for other languages through Extensions.

### Shortcuts

- ⇧⌘P: Show All Commands
- ⇧⌘E: View: Show Explorer
- ⇧⌘F: View: Show Search
- ⇧⌘G: View: Show SCM (I have overridden this for consistency)
- ⇧⌘D: View: Show Run and Debug
- ⇧⌘X: View: Show Extensions
- ⇧⌘T: View: Toggle Integrated Terminal (I have overridden this for consistency)
- ⌥⌘←: View: Open Previous Editor
- ⌥⌘→: View: Open Next Editor
- ⌘K⌘S: Preferences: Open Keyboard Shortcuts
- ⌘P: Go To File ...
- ⇧⌘O: Go To Symbol in Editor ...
- ⌘T: Go To Symbol in Workspace ...
- ⌥-: Go Back
- ⌥⇧-: Go Forward

### Debugging

- There are **6** things you can do: Continue, Step Over, Step Into, Step Out, Restart, and Stop.
- There is a Debug Console available in the Panel (where the Integrated Terminal is also found) that allows you to evaluate expressions where your program currently is in execution.
- Visual Studio Code supports _Log Points_ which are an alternative to print statements that show up in the Debug Console instead of the Terminal. The advantage of this is that it does not require making modifications to your code (which you have to remember to revert) and it decouples your debugging messages from your regular program output.
- Instead of always logging something when you reach a particular point in your program, you can have conditional _Log Points_ based on expression evaluation of hit count. These can be dynamically modified during a debugging session.
- Both _Break Points_ and _Log Points_ in Visual Studio Code persist even after you restart the application.

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

- Visual Studio Code uses JSON files for all configuration purposes.
- There are two main categories of settings: User and Workspace.
  - User settings are stored in the file `~/Library/ApplicationSupport/Code/User/settings.json`
  - Workspace settings are stored in the file `.vscode/settings.json`.
- Use the keyboard shortcut ⌘, to access both User and Workspace settings.
- Debug settings are stored in the file `.vscode/launch.json`.

## Navigation

- Go to Definition (⌥F): Jump to the definition of a symbol.
- Go to Declaration:

## Languages

### Python

- IntelliSense works for standard modules as well as ones you've installed into the environment of the selected Python interpreter; just make sure that you've selected the correct Python interpreter for your workspace.
- Here are some commands the Python extension added to the command palette:
  - Python: Select Interpreter (usually a good choice is `.venv/bin/python`)
  - Python: Start REPL
  - Python: Run Python File in Terminal
  - Python: Select Linter
  - Python: Format Document
  - Python: Configure Tests
  - Python: Run All Tests
  - Python Refactor: Sort Imports

#### Formatting

A **formatter** is a program that detects only stylistic errors. Here are the different formatters that you can choose when working with Python in Visual Studio Code:

- autopep8 (default)
- black
- yapf

Formatting commands:

- Format Document With...
- Format Document
- Format Selection

Formatting settings:

- `python.formatting.provider`: which formatter you are using (the possible values are `"autopep8"`, `"black"`, or `"yapf"`, or `"none"`).

TODO: Can you enable more than one formatter? What are the repercussions of doing so?

#### Linting

A **linter** is a program that detects both stylistic and syntactic errors. Here are the different linters that you can choose when working with Python in Visual Studio Code:

- bandit
- flake8
- mypy
- prospector
- pycodestyle
- pydocstyle
- pylama
- pylint (default)

Linting commands:

- Python: Enable Linting (This command allows you to quickly toggle the `python.linting.enabled` setting between `true` and `false`. If the setting did not exist before, then it is added to `settings.json`.)
- Python: Select Linter (This command sets the `python.linting.<linter>Enabled` setting to be `true` for whatever linter you select and simultaneously sets the corresponding setting for all the other linters to be `false`. The only way you can enable multiple linters is for you to manually edit the `settings.json` file.)
- Python: Run Linting (This command forcibly triggers the linter to run. You shouldn't really need to use it though, because linting is automatically run every time you hit save.)

Linting settings:

- By default, linting is enabled (the `python.linting.enabled` setting is `true`), linting is triggered on saving a file (the `python.lintOnSave` setting is `true`), and the maximum number of linting messages is 100 (the `python.linting.maxNumberOfProblems` setting is `100`).
- Different linters will be able to catch different kinds of errors. Because of this, it may be advantageous to enable more than one linter. This is not only possible but also easy to do. The only catch is that this is not something you can do from the command palette. You must manually change some settings in `.vscode/settings.json`. For instance, if you wanted to enable both PyLint and MyPy, then you would set both `python.linting.mypyEnabled` and `python.linting.pylintEnabled` to be true.

PyRight: https://github.com/Microsoft/pyright
PyLance: https://devblogs.microsoft.com/python/announcing-pylance-fast-feature-rich-language-support-for-python-in-visual-studio-code/

#### Testing

The Python extension allows you to both run tests written with the `unittest`, `pytest`, or `nose` quickly and examine the results of those tests in an intuitive manner. You simply need to run the "Python: Configure Tests" command, select the testing framework you used to write your tests, the directory that contains your tests, and the regular expression used to determine which files contain tests. In terms of personal conventions, I use the `unittest` framework, put tests in the `tests/` folder, and give files containing tests names that match the `test_*` regular expression. Here are some notes about writing tests using the `unittest` framework:

- The fundamental unit of abstraction is the **test case**.
- Test cases are entirely self contained. They can be run in complete isolation or arbitrary sequence with other test cases.
- Test cases consist of **test methods**. You can tell which methods are test methods because the names of test methods start with `test`.
- Most test cases subclass `unittest.TestCase`, which implements assertion methods that allow you to check many different kinds of assertions for code correctness. Examples of such methods include: `self.assertEqual()`, `self.assertTrue()`, and `self.assertFalse()`.
- If you define the `setUp()` and `tearDown()` methods, they are automatically executed before and after each test method in a test case. This promotes code reuse.
- A test case should be entirely self-contained; they can be run in isolation or arbitrary sequence.
- You can only enable one test framework at a time. Writing tests with one framework would be a good idea anyway for consistency.

Something you can do to write more realistic tests is create **mock objects**. These are artificially created objects that are designed to imitate real ones. Their value is in the fact that mock objects offer further control and stability of your tests. Instead of making an actual HTTP request and retrieving an HTTP response object in your code, you can create a fake HTTP response object instead. You can also create mock HTTP response objects that correspond to different failure modes!

- Mock objects create attributes on the fly as you try to access them. This is the ultimate form of duck typing—mock objects can be used anywhere!
- Mock objects keep track of how you use them.
- A fantastic package for mocking tests that depend on the date is `freezegun`. Check it out!

```
from unittest import mock

# create a mock object
thing = mock.Mock()

# perform assertions I
thing.method.assert_not_called()

# use the mock object
thing.method("Kevin")

# perform assertions II
thing.method.assert_called()
thing.method.assert_called_once()
thing.method.assert_called_with("Kevin")        # only applies to most recent call
thing.method.assert_called_once_with("Kevin")   # only applies to most recent call

# use the mock object some more
thing.method("Kelly")

# perform assertions III
thing.method.assert_called_once()
thing.method.assert_called_with()

# perform more analysis
thing.method_calls
thing.method.call_count
thing.method.call_args      # only applies to most recent call
thing.method.call_args_list
```

#### The `site` Module

In order to test your code, you need to be able to import the modules that contain your code. This may require you to tinker with `sys.path`, which is a list of strings telling Python where to look for modules. Modifying this variable is done through the `site` module.

Before we dive into the usage of the `site` module, we need to know a few things about the `sys` module.

- `sys.executable`: The absolute path of the Python interpreter.
- `sys.prefix`: The site-specific directory where the platform independent Python files are installed. What this means is the main collection of Python library modules will be installed at `prefix/lib/pythonX.Y`.
- `sys.exec_prefix`: ...

> It looks like the solution was to add the project directory to the PYTHONPATH environment variable. This causes the project directory to get added to `sys.path` and makes the modules defined in it importable.

#### Language Servers

If you open the settings, you can choose the Python language server to use. Your two options are _Jedi_ and _Microsoft_. Here are some considerations to take into account when making the decision of which language server you are going to use:

- One
- Two
- Three

### C

### C++

### Rust

## TODO

This is a list of unresolved questions.

- When you install a new module with pip, VSCode Intellisense does not seem to pick it up until you quit the application and restart (there is an "Analyzing in Background" notification in the status line). Is there a way to automatically or manually trigger this to happen without restarting the application?
- Linting is a super important past of a pleasing development environment so it deserves some more careful exposition. There are a lot of other Python linters that have not been discussed. For instance, `pycodestyle` and `pydocstyle`. What do these things have to offer? What are some other important linting-related settings that can be configured in `.vscode/settings.json`? What should be the default configuration for my personal linting purposes? Which linters should be installed and enabled?
