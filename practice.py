# n,m = map(int,input().split())
# print(n)
# print(m)

from datetime import datetime

t= datetime.today()
FORMAT = "%a %d %b %Y %H:%M:%S %z"
t=t.strftime(FORMAT)
print(t)