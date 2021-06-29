#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/home/bright/Vscode_Project/python_Cpp/pybind11
g++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` test.cpp -o test`python3-config --extension-suffix`