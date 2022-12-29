import time 

hour =int(time.strftime('%H'))
# hour = 1
msg =""
if(hour>=4 and hour<=10):
  msg="Morning"
elif(hour>=11 and hour<=12):
  msg="Noon"
elif(hour>=13 and hour<=17):
  msg="Afternoon"
elif(hour>=18 and hour<=19):
  msg="Evening"
else:
  msg="Night"

print(time.strftime('%X'),"Good",msg,"Sir!")