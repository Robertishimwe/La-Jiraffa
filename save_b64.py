import base64
import os

b64_str = ""

try:
    with open(r"C:\Users\TestSolutions\Documents\La-Jiraffa\images\onSite\getQuotation\planning_new.jpg", "wb") as f:
        f.write(base64.b64decode(b64_str))
    print("Success")
except Exception as e:
    print(e)
