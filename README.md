Flask-QArgs
===========

Flask Query Arguments Parser, as your view decorators.

---

```shell
$ pip install flask-qargs
```

```python
from flask import Flask, g
import flask_qargs as qargs

app = Flask(__name__)


@app.route("/")
@qargs.init()
@qargs.argument('greeting', location='args', required=True)
@qargs.argument('name', location='args', required=True)
def hello():
    args = g.qargs
    return "{0} {1}!".format(args.greeting, args.name)


app.run(port=9998)
```

```shell
$ curl 'http://localhost:9998?greeting=Hi&name=Wonder'
Hi Wonder!
```
