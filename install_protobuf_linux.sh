#!/bin/bash

# This script will install the protobuf compiler and output the version on linux

# 1. Install pre-compiled binaries
PB_REL="https://github.com/protocolbuffers/protobuf/releases"
curl -LO $PB_REL/download/v32.1/protoc-32.1-linux-x86_64.zip

# 2. Inzip the file
unzip protoc-32.1-linux-x86_64.zip -d /usr/local/

# 3. Remove the zip file
rm protoc-32.1-linux-x86_64.zip

# 4. Print to protobuf compiler version
/usr/local/bin/protoc --version