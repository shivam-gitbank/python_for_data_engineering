import requests # request lib
import json # json lib
import boto3
from datetime import datetime, timezone

#-----------------------------------------------------
# Config
#-----------------------------------------------------

API_URL = ""
S3_BUCKET = ""
SOURCE_NAME = ""

#----------------------------------------------------
# Calling API
#----------------------------------------------------
response = requests.get(API_URL, timeout = 30)
response.raise_for_status()
api_data = response.json()