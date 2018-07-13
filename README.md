Test command: `wrk -d20s -t10 -c200 http://localhost:8080`

*Cyclone (Python 2):*
Requests/sec:   3697.12
Transfer/sec:    711.26KB

*Tornado (Python 2):*
Requests/sec:   2254.80
Transfer/sec:    473.42KB

*Tornado (Python 3):*
Requests/sec:   2278.23

*Tornado (Python 3, asyncio):*
Requests/sec:   1846.11
Transfer/sec:    387.61KB

*Tornado (Python 3, asyncio-uvloop):*
Requests/sec:   2163.40
Transfer/sec:    428.88KB

*Sanic:*
Requests/sec:  20364.16
Transfer/sec:      2.47MB