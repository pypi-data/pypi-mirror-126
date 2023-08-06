# djangoFeignClient

### install
```python
pip install djangoFeignClient
```

### example
```python
from feign_client.feignClient import FeignClient


class EurekaTest(unittest.TestCase):
    
    def test_eureka_user_login(self):
        data = {
            'username': 'admin',
            'password': '123456'
        }
        
        # eureka_server address
        host = '127.0.0.1:8081'
        
        # eureka app name
        app_name = 'test_app'
        
        # http request method
        method = 'POST'
        
        # request path
        path = '/user/login'

        res = FeignClient(eureka_server = host, method = method, path = path, app_name = app_name, data = dict(data)).result
        
        print(res)

```