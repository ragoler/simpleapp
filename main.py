from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import random

app = FastAPI()

@app.get("/favicon.svg", response_class=FileResponse)
def favicon():
    return "favicon.svg"


@app.get("/api/random")
def get_random_number():
    return {"number": random.randint(1, 100)}

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Simple App</title>
            <link rel="icon" href="/favicon.svg" type="image/svg+xml">
        </head>
        <body>
            <h1>Hello World, the random number is: <span id="random-number"></span></h1>
            include Favicon
            <script>
                fetch('/api/random')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('random-number').innerText = data.number;
                    });
            </script>
        </body>
    </html>
    """
