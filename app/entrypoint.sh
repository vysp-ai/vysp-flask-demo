#!/bin/bash
apt-get update
apt-get install -y python3-full python3-pip
cd /home/app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -U openai
flask run --host=0.0.0.0 --port=5001
