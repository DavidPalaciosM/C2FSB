#!/usr/bin/bash
sudo apt update
sudo apt upgrade
sudo apt install g++ libboost-all-dev libeigen3-dev
python3 -m venv pyvenv
source pyvenv/bin/activate
pip install -U -r requirements.txt
cd Cell2FireC/
make
cd ..
