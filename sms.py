from twilio.rest import Client
#x=input("Number:")
#print(x)
sid="ACe597d7973d3cbde58d2d0ba349e6e8df"
token="db9cc22118465912dc1d10baafc6bbb9"
client=Client(sid,token)
msg="YOUR PRODUCT IS DISPATCHED"
#client.messages.create(to=x,from_="+15109451751",body=msg)
client.messages.create(to="+919967100111",from_="+15109451751",body=msg)
