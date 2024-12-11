# Flavor founder

Application which demonstrate you how many molecules of flavour your favorite products consists of.

## Main idea

The application queries FlavorDB to search for the requested product. FlavorDB lists molecules associated with certain flavors and tastes. In theory, we can predict the taste of a product by calculating how many molecules with specific taste profiles it contains.

We focus exclusively on taste molecules: sweet, bitter, sour, salty, and umami. You can refer to the image below to visualize how it works and understand the data we collect:

![taste demonstration](https://raw.githubusercontent.com/Hexxie/FlavorFounder/refs/heads/main/img/flavors.png)

## Architecture

Our frontend is built using Next.js and consists of two main components:

- `Component.tsx:` Handles the search functionality.
- `Product.tsx:` Displays the information about the product.
When the search button is clicked (or Enter is pressed), the frontend sends a GET request to our local Python server.

The Python server verifies if the product exists in the query and then fetches the relevant information from FlavorDB2. It calculates the number of molecules and returns other useful data (as shown in the image below) to present the requested product in a user-friendly format.


![app architecture](https://raw.githubusercontent.com/Hexxie/FlavorFounder/refs/heads/main/img/architecture.png)

[Figma board](https://www.figma.com/board/veUbS9ZOJop6SWFiuaXIIT/Python-Final-Project?node-id=0-1&t=pccYQwDygGRlDacG-1)

## Build & Run

```
git clone https://github.com/Hexxie/FlavorFounder.git
```

### Build the frontend part

Use Docker to build and run the application.

```
docker build -t flavor-founder-app .

docker run -p 3000:3000 flavor-founder-app
```

> **Note:** 
> If you prefer a native setup, you can use npm to install the dependencies. Refer to the commands in the Dockerfile to ensure all dependencies are installed correctly.

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
