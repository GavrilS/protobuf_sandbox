#!/bin/bash

# This script will install the protobuf compiler and output the version on ubuntu

apt install -y protobuf-compiler
protoc --version