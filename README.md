# ChatterBot code with simple and edit with flask
#Ensure python 3.8.0 is installed on system
**In Linux**
python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install spacy==2.3.5
python -m spacy download en_core_web_sm
python -m spacy link en_core_web_sm en
mkdir -p venv/lib/python3.8/site-packages/chatterbot_corpus/data/custom
cp myown.yml venv/lib/python3.8/site-packages/chatterbot_corpus/data/custom/
cp M1.yml venv/lib/python3.8/site-packages/chatterbot_corpus/data/custom/
export FLASK_APP=main.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000
flask run
