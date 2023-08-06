# JsonRpc Flask Ext Dispatcher

## Instalación

```bash
    pip install bws-jsonrpc
```

## Modo de uso

```python

from flask import Flask
from bws_jsonrpc import rpc


@rpc.method
def ping() -> Result:
    '''return pong'''
    return rpc.Success("pong")


@rpc.method
def think(object, verb) -> Result:
    return rpc.Success([verb, object])


g = rpc.group("actions")
@g.method(name="drink")
def _drink_(object, verb="drink") -> Result:
    return rpc.Success([verb, object])


@rpc.expose_class(name="person")
class Person(object):
    
    @rpc.expose_method    
    def greet(self, name=None):
        '''
            return Hi + name
        '''
        return rpc.Success("Hi {}".format(name or ""))



if __name__ == "__main__":

    app = Flask(__name__)
    
    app.register_blueprint(rpc.as_blueprint())

    app.run(debug=True)
```