import os

import boto3
from dotenv import load_dotenv

load_dotenv()

client = boto3.client(
    "bedrock-runtime",
    region_name=os.environ["AWS_DEFAULT_REGION"],
)

response = client.converse(
    modelId=os.environ["BEDROCK_MODEL_ID"],
    messages=[
        {
            "role": "user",
            "content": [
                {"text": "Explica en català què és un AMFE."}
            ],
        }
    ],
    inferenceConfig={
        "maxTokens": int(os.getenv("BEDROCK_MAX_TOKENS", "500")),
        "temperature": float(os.getenv("BEDROCK_TEMPERATURE", "0.1")),
    },
)

print(response["output"]["message"]["content"][0]["text"])

print("\nUsage:", response["usage"])
print("Metrics:", response["metrics"])