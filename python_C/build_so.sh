#!/bin/bash

set -ex

g++ -fPIC -shared test.cpp -o pytest.so
