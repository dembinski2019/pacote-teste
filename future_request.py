import requests
from requests.models import Response
from concurrent import futures


class FuturesRequest2:
    MAX_WORKERS = 20
    def __init__(self, *args, **kwargs) -> None:
        
        self.workers = self.MAX_WORKERS
        
    
    def __call__(self, method, url, on_success,**kwds:dict) -> Response:

        with futures.ThreadPoolExecutor(self.workers) as executor:
            res = [executor.submit(
                requests.request, method, url, **kwds
                )
            ]
            for future in futures.as_completed(res):
                on_success(future.result())