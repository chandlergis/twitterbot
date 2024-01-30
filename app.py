from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from twitter import main  # Make sure to replace 'your_script' with the actual name of your Python script file

app = FastAPI()

class TweetRequest(BaseModel):
    ids: List[str] = Field(..., example=["1234567890"])

class MediaInfo(BaseModel):
    media_url_https: Optional[List[str]]
    media_type: Optional[List[str]]

class TweetResponse(BaseModel):
    # Include all the fields you expect in your tweet_data
    # For simplicity, I'm only adding a few fields here
    id: str
    text: str
    media_info: MediaInfo

@app.post("/tweets/", response_model=List[TweetResponse])
def get_tweets(request: TweetRequest):
    try:
        tweet_data = main(request.ids)
        # You might need to transform tweet_data to match the TweetResponse model
        return tweet_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
