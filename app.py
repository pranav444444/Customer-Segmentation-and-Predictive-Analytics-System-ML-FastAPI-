from fastapi import FastAPI, Request, Form
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from uvicorn import run as app_run
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.pipeline.prediction_pipeline import PredictionPipeline
from src.pipeline.train_pipeline import TrainPipeline
from src.constant.application import *

import warnings
warnings.filterwarnings('ignore')

app = FastAPI()

# Templates for rendering HTML
templates = Jinja2Templates(directory='templates')

# Set up CORS middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# ---------------------- ROUTES ----------------------

@app.get("/train")
async def trainRouteClient():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.get("/")
async def predictGetRouteClient(request: Request):
    try:
        return templates.TemplateResponse(
            "customer.html",
            {"request": request, "context": "Rendering", "recommendation": ""}
        )
    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/")
async def predictRouteClient(
    request: Request,
    Age: int = Form(...),
    Education: int = Form(...),
    Marital_Status: int = Form(...),
    Parental_Status: int = Form(...),
    Children: int = Form(...),
    Income: float = Form(...),
    Total_Spending: float = Form(...),
    Days_as_Customer: int = Form(...),
    Recency: int = Form(...),
    Wines: int = Form(...),
    Fruits: int = Form(...),
    Meat: int = Form(...),
    Fish: int = Form(...),
    Sweets: int = Form(...),
    Gold: int = Form(...),
    Web: int = Form(...),
    Catalog: int = Form(...),
    Store: int = Form(...),
    Discount_Purchases: int = Form(...),
    Total_Promo: int = Form(...),
    NumWebVisitsMonth: int = Form(...)
):

    try:

        input_data = [
            Age, Education, Marital_Status, Parental_Status, Children,
            Income, Total_Spending, Days_as_Customer, Recency,
            Wines, Fruits, Meat, Fish, Sweets, Gold,
            Web, Catalog, Store, Discount_Purchases,
            Total_Promo, NumWebVisitsMonth
        ]

        prediction_pipeline = PredictionPipeline()
        predicted_cluster = prediction_pipeline.run_pipeline(input_data=input_data)

        # LOGIC (Cluster Interpretation)
        cluster = int(predicted_cluster)

        if cluster == 0:
            label = "High Value Customer"
            recommendation = "Provide loyalty rewards and premium services"

        elif cluster == 1:
            label = "Low Value Customer"
            recommendation = "Offer discounts and increase engagement"

        else:
            label = "Medium Value Customer"
            recommendation = "Upsell products and targeted promotions"
            
        #pls note if you want to test backend in swagger uncomment this line
        # return {"predicted_cluster": int(predicted_cluster[0])}

        return templates.TemplateResponse(
            "customer.html",
            {
                "request": request,
                "context": label,
                "recommendation": recommendation,
                "cluster_id":cluster
            }
        )

    except Exception as e:
        return {"status": False, "error": str(e)}


# Run the app
if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)
    
    
    
    

'''
To run the app firsy acrivate environement by typing this command in CMD in terminal: conda activate D:\Customer_Segmentation_ML_project\Customer-Categorizer-main\venv 

and then run commnad -> python app.py

'''