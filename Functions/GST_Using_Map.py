prices=[100,250,400,1200,50]
gst=0.18
prices_with_gst = list(map(lambda x: x + x*gst, prices))
print("Original prices:", prices)
print("Prices with GST:", prices_with_gst)