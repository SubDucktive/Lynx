# Lynx
Hello! This is the official github repository for my programming language, Lynx. In this readme will have some basic information about Lynx and its development, as well as instructions on  how to build the project and navigate the repository.

# Project Vision & Motivation
In February 2025 (6 months ago), I wrote a simple programming language in Javascript, called Mercury. I was proud but it didn't have all of the features of a real language, plus, it was buggy and I didn't use too many good sources. The goal for Lynx is to be a deliberate, long-term project that may continue for months or years. Mercury had support for loops and conditional statements, but not more advanced, convenience features, such as the ternary operator. Mercury also didn't have objects or classes, and Lynx will have both, and many more features that modern languages have that make Lynx a feasible and usable language for scripting.
> **Note:** I do not plan for Lynx to be a language that will be useful to many people, due to some things like the speed and optimization of the language being horrible as it is written in Python.

# Project Layout
This is basically where you can find everything in the project if it isn't already self explanatory. I don't think this project will get too hard to navigate in the future.
## Source code
Source code will be stored in Lynx/src, different subdirectories to the source code directory might be necessary to organize code
## Tests folder
This is where tests and example programs will be stored (Lynx/tests). These may include tests for specific features, and might grow to a lot of files in the future.
## Documentation folder
Lynx/docs is where the Documentation will be stored. This is a tutorial/guide on how to use the language including every feature the language has, along with examples for most of the features explained.

# Installation and usage
In the future, there will be a script that does this automatically, but i guess you could just copy the source code to a folder in /usr/share

`sudo cp -r Lynx/src /usr/share/Lynx`

and then make a script that runs src/lynx.py

```
#!/bin/bash
python3 /usr/share/Lynx "$@"
```

then make it executable

`chmod +x lynx`

where lynx is the script, then copy it to /usr/bin/lynx

`sudo cp -r lynx /usr/bin/lynx`

then lynx can be used as a command:

```
lynx
lynx tests/print.lx
```

> **Note:** Do not copy code online if you dont trust it, also this isnt the most professional implementation of usage and i will improve upon this in the future