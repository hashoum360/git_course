from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.middleware.cors import  CORSMiddleware

class BmiOutput(BaseModel):
    bmi: float
    message: str | None = None


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/calculate_bmi", response_model=BmiOutput)
def calculate_bmi(
    weight: float = Query(..., gt=20, lt=200, description="Weight in kg"),
    height: float = Query(..., gt=1, lt=3, description="Height in meters"),
):
    return BmiOutput(bmi=weight / (height * height), message="BMI calculated successfully")
@app.get("/v1/models")
def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "hello-model",
                "object": "model",
                "created": 0,
                "owned_by": "local",
            }
        ],
    }
