import math
import os
import re
import sys

from flask import Flask, Response, request

sys.set_int_max_str_digits(0)

app = Flask(__name__)
NUM = re.compile(r"[0-9]+")


def parse(value):
    if value is None or not NUM.fullmatch(value):
        return None
    return int(value)


@app.get("/toxtamurodovagulshodaa_gmail_com")
def lcm():
    x = parse(request.args.get("x"))
    y = parse(request.args.get("y"))
    if x is None or y is None:
        body = "NaN"
    else:
        body = str(math.lcm(x, y))
    return Response(body, mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
