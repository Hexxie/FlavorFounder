# Flavor founder

Application which demonstrate you how many molecules of flavour your favoiurite products consists of.

## Build & Run

```
git clone https://github.com/Hexxie/FlavorFounder.git
```

### Build the frontend part

```
docker build -t flavor-founder-app .

docker run -p 3000:3000 flavor-founder-app
```

### Build python part:

```
cd python
```

#### Create venv

#### Windows
```
python -m venv venv
venv\Scripts\activate
```

#### Linux or Mac

```
python -m venv venv
source venv/bin/activate
```

#### Install dependencies

```
pip install -r requirements.txt
```

#### Run the app

```
python flavor.py
```

Now you can follow the http://localhost:3000/ to test the app
