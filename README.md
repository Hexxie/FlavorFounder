# Flavor founder

Application which demonstrate you how many molecules of flavour your favoiurite products consists of. 

git clone

Build the frontend part

docker build -t flavor-founder-app .

docker run -p 3000:3000 flavor-founder-app

Build python part:

cd python

Create venv

for Windows
python -m venv venv
venv\Scripts\activate

for Linux or Mac
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python flavor.py
