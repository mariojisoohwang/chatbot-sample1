from dto import ChatbotRequest
from samples import simple_text_sample
import aiohttp
import time
import logging
import json

logger = logging.getLogger("Callback")

async def callback_handler(request: ChatbotRequest) -> dict:

    time.sleep(1.0)
    
    url = request.userRequest.callbackUrl
    payload = simple_text_sample

    if url:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, json=payload) as resp:
                result = await resp.json()
                logger.info("result=" + str(result))
    else:
        logger.info("empty url")
