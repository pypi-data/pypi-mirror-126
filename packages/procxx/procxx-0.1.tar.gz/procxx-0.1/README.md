# procxx
## Simple C++ builder tools

### **About**
procxx is a c++ builder tools for building c++ project.

If you want something with more features, you can use CMake.

procxx target is to make building c++ easier.

### **Supported Compilers**
- gcc (g++)
- clang (clang++)
- other compilers that support gcc and clang flags

### **Example**
```py
from procxx import CXXProject

myproject = CXXProject("g++") # you can remove the g++ if you want it auto-detect compiler

myproject.add_include("include") # add include path

myproject.add_raw("src/*.cpp") # add raw argument. Usually for adding source file

myproject.autorun("main.cpp") # you can also use run method but autorun will automatically run the compiled executeable
```

### **License**
MIT