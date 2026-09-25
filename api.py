from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="NumInfo API")

# CSV Load
df = pd.read_csv("database.csv", dtype=str)

# Column names ko clean karna
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Phone clean
df["phone"] = df["phone"].astype(str).str.strip()

print("Database Loaded:", len(df))
print(df.columns.tolist())


@app.get("/")
def home():
    return {
        "developer": "@Oriss01",
        "api_by": "@Oriss01",

        "status": "online",
        "records": len(df),

        "credits": "Developer @Oriss01 | API by @Oriss01"
    }


@app.get("/lookup/{phone}")
def lookup(phone: str):
    phone = phone.strip()

    result = df[df["phone"] == phone]

    if result.empty:
        return {
            "developer": "@Oriss01",
            "api_by": "@Oriss01",

            "success": False,
            "message": "Number not found",

            "credits": "Developer @Oriss01 | API by @Oriss01"
        }

    row = result.iloc[0].fillna("")

    return {
        "developer": "@Oriss01",
        "api_by": "@Oriss01",

        "success": True,
        "data": {
            "first_name": row["first_name"],
            "last_name": row["last_name"],
            "address": row["address"],
            "city": row["city"],
            "county": row["county"],
            "state": row["state"],
            "zip": row["zip"],
            "phone": row["phone"],
            "carrier": row["carrier"],
            "gender": row["gender"],
            "ethnicity": row["ethnicity"],
            "ownrent": row["ownrent"],
            "latitude": row["latitude"],
            "longitude": row["longitude"]
        },

        "credits": "Developer @Oriss01 | API by @Oriss01"
    }