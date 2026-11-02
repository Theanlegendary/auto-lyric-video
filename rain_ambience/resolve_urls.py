import urllib.request
import re

urls = [
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGDZAFO2nzneFGMVX-u_gE5lrVhsDf192aTmPOuzMk_3tAhlxfvpDkkhoLM30rtY6Dt7AKbEBqO9klmASDXGjgHcF5RIlPMAR9k7OZloHTa868yncB5qDL9Wh4p-S5YHCjR3ynKv55_4VPJI2GKcl8NXo1dVD8JqelJiiMGO95fE1Ds264A3gJ",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxxR38J_SWvRGw92-H2qr09IPQYrLtwPIhFcfCkRwBaHgahK6Hl0bRrKSwXuZHYh0z57INepKNeB-0b-pR-CUCYSHMZOyEQkop1CTBLgIKwqA8FeuP366746GmfIhyA7Kulg5zPCwt7Lfod9yTkyALjm9fKh3RBR3EqbkMabp1J_l7ryQ=",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO0wD15-3JNMgnWJXS_KrW7Uhwbbt-G1t9ekbhZoHuhiDYQbFLmauUAkim5Ry7hfDgownNSehd7dsLpfZ0fPwXUCgN9sqijx_pZeoljRpIsSv-4xrzHqfni7_1gVDAy5Cgry6MFpslttoCCTISBFmT6AspSroH9moWB-vuI2U8Aw=="
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            print("Redirects to:", resp.geturl())
    except Exception as e:
        print("Error resolving:", e)
