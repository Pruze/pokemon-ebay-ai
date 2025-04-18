from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI(title="Pokemon Card eBay AI")

@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint, returns basic API info."""
    return {"message": "Pokemon Card eBay AI API", "status": "operational"}

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}

# Will add more endpoints as we implement functionality