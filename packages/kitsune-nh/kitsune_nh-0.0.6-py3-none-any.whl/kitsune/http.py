from collections.abc import Sequence
from typing import List, Dict, Any, Union

import re
import asyncio
import aiohttp

from kitsune.constants import TBR
from kitsune.routes import Route
from kitsune.query import Popularity

class HTTPHandler:

    __slots__ = ("loop", "lock", "session",)
   
    def __init__(self, loop: asyncio.AbstractEventLoop = None, session: aiohttp.ClientSession = None):                                                                                                                                                                                                                                              
        self.loop = loop or asyncio.get_running_loop()
        self.session = session 

        self.lock = asyncio.Lock()

    def ratelimit(async_func):
        async def wrapper(*args, **kwargs): 
            self = args[0]
            await self.lock.acquire()
            self.loop.call_later(TBR, self.lock.release)
            result = await async_func(*args, **kwargs)
            assert result is not None
            return result
        return wrapper 

    @ratelimit
    async def get(self, route: Route, **params) -> Union[Dict[str, Any], str, bytes, None]: 
        async with self.session.get(route.url, params = params) as response: 
            if 200 <= response.status < 300:    
                content_type = response.headers["Content-Type"]
                if content_type == "application/json": 
                    return await response.json()
                elif content_type[0:5] == "image": 
                    return await response.read()
                return await response.text()
            elif response.status == 429: 
                return await self.get(route) 
            else: 
                return None

    async def fetch_gallery_data(self, __id: int) -> Dict[str, Any]:  
        route = Route(f"/api/gallery/{__id}")
        payload = await self.get(route)

        return payload

    async def fetch_related_data(self, __id: int) -> List[int]: 
        route = Route(f"/g/{__id}")
        html = await self.get(route)

        ids = re.findall(r"/g/(\d+)/", html)
        
        filtered = [__id for __id in ids if ids.index(__id) != 0]

        return filtered

    async def fetch_homepage_data(self) -> List[int]: 
        route = Route()
        html = await self.get(route)

        ids = re.findall(r"/g/(\d+)/", html)

        return ids

    async def fetch_paginator_limit(self, query: str, popularity: Popularity) -> int: 
        route = Route(f"/api/galleries/search?query={query}")
        payload = await self.get(route, page = 1, popularity = popularity.value)

        limit = payload["num_pages"] if payload else 0

        return limit

    async def fetch_search_data(self, query: str, page: int, popularity: Popularity) -> Dict[str, Any]:
        route = Route(f"/api/galleries/search?query={query}")     
        payload = await self.get(route, page = page, popularity = popularity.value)

        return payload

    async def fetch_comment_data(self, __id: int) -> Dict[str, Any]:
        route = Route(f"/api/gallery/{__id}/comments")
        payload = await self.get(route)

        return payload

    async def fetch_media_bytes(self, media: Sequence[str]) -> List[bytes]: 
        routes = [Route(media) for media in media]
        bytes_l = await asyncio.gather(*(self.get(route) for route in routes))

        return bytes_l

        
