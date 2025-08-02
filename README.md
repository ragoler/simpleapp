
# Simple FastAPI App

This is a simple FastAPI application that returns a random number and displays it on a web page.

## Running Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Open your browser** and navigate to `http://127.0.0.1:8000`.

## Deploying to Google Cloud Run

1. **Build the Docker image:**
   ```bash
   docker build -t simpleapp .
   ```

2. **Push the image to Google Container Registry (GCR):**
   ```bash
   docker push gcr.io/your-gcp-project-id/simpleapp
   ```

3. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy --image gcr.io/your-gcp-project-id/simpleapp --platform managed
   ```
