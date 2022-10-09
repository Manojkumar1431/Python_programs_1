houses = int(input())
percentile = (2/houses)*100
"""if percentile=2/3*100=66.6 will be output
so we want nearest whole number i.e 67 thats why we add 0.4 to answer i.e 66.6+0.4=67"""

print(int(percentile+0.4))