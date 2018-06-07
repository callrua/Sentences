# Sentences
Sentence validator and a simple GUI implementing it.

validator.py contains functions for validating a sentence against predefined test cases, it can accept a text file as input and will run the tests against every line in the file, alternatively, if no file is given it will prompt user for a sentence to validate.
gui.py makes use of the python tkinter module to display a simple GUI making use of the functions in validator.py

### Prerequisites

+ python 3.5
+ tkinter python module

```
sudo apt-get install python3
sudo apt-get install python3-tk
```

## Getting Started

Running the GUI;

```
python3.5 gui.py
```

Running validator.py with a text file;

```
python3.5 validator.py /path/to/file
```

Running validator.py with no text file;

```
python3.5 validator.py
```



