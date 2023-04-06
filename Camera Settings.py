LightCondition = {'snow':'1', 'sand':'1', 'sunny':'2', 'lightly cloudy':'3', 'overcast':'4', 'sunset':'5', 'shade':'5', 'dusk':'6', 'none':'7'}

Aperture = {'2': '8', '2.8': '7', '4': '6', '5.6': '5', '8': '4', '11': '3', '16': '2', '22': '1'}

Shutterspeed = {'30': '8', '60': '7', '125': '6', '250': '5', '500': '4', '1000': '3', '2000': '2', '4000': '1'}

ISO = {'6400': '8', '3200': '7', '1600': '6', '800': '5', '400': '4', '200': '3', '100': '2', '50': '1'}

Aperture2 = {'8': '2', '7': '2.8', '6': '4', '5': '5.6', '4': '8', '3': '11', '2': '16', '1': '22'}

Shutterspeed2 = {'8': '30', '7': '60', '6': '125', '5': '250', '4': '500', '3': '1000', '2': '2000', '1': '4000'}

ISO2 = {'8': '6400', '7': '3200', '6': '1600', '5': '800', '4': '400', '3': '200', '2': '100', '1': '50'}

while True:
  print('ヾ(⌐■_■)ノ♪')
  light = input('What is the light setting? Enter "list" for a list.')
  light = light.lower()
  if light == 'list':
    print("\n Snow\n Sand\n Sunny\n Lightly Cloudy\n Overcast\n Sunset\n Shade\n Dusk\n")
  elif light in LightCondition:
    print('You have chosen option:',light)
    X = int(LightCondition.get(light))
    break
  else:
    print('Invalid answer.')
while True:     
  recommendedsetting = input('Which setting would you like this program to recommend? Enter "list" for a list.')
  recommendedsetting = recommendedsetting.lower()
  if recommendedsetting == 'list':
    print("\n ISO\n Aperture\n Shutter-Speed\n")
  elif recommendedsetting == "aperture":
    f = '1'
    break
  elif recommendedsetting == "iso":
    f = '2'
    break
  elif recommendedsetting == 'shutter-speed':
    f = '3'
    break
  else: 
    print('Invalid answer.')
#aperturecode
if f == '1':
  print('You have chosen 📸Aperture📸')
  while True:
    C = input('What would you like to set your 📸ISO📸 to? Enter "list" for a list.')
    C = C.lower()
    if C == 'list':
      print("\n 6400\n 3200\n 1600\n 800\n 400\n 200\n 100\n 50")
    elif C in ISO:
      S = int(ISO.get(C))
      break
    else:
      print('Invalid answer.')
  while True:
    D = input('What would you like to set your 📸Shutter-speed📸 to? Enter "list" for a list.')
    D = D.lower()
    if D == 'list':
      print("\n 30\n 60\n 125\n 250\n 500\n 1000\n 2000\n 4000")
    elif D in Shutterspeed:
      G = int(Shutterspeed.get(D))
      break
    else:
      print('Invalid answer.')
  H = (16 - ((int(S) + int(G) + int(X))))
  if (int(H) < 1) or (int(H) > 15):
    print('Error. Your lighting is incorrect.')
  else:
    E = str(f)
    I = (Aperture2.get(E)) 
    print('You should set your aperture to', I)
    print('Thank you. You have finished this program.')

#ISOCode
elif f == '2':
  print('You have chosen 📸ISO📸')
  while True:
    C = input('What would you like to set your 📸Aperture📸 to? Enter "list" for a list.')
    C = C.lower()
    if C == 'list':
      print("\n 2\n 2.8\n 4\n 5.6\n 8\n 11\n 16\n 22")
    elif C in Aperture:
      S = int(Aperture.get(C))
      break
    else:
      print('Invalid answer.')
  while True:
    D = input('What would you like to set your 📸Shutter-speed📸 to? Enter "list" for a list.')
    D = D.lower()
    if D == 'list':
      print("\n 30\n 60\n 125\n 250\n 500\n 1000\n 2000\n 4000")
    elif D in Shutterspeed:
      G = int(Shutterspeed.get(D))
      break
    else:
      print('Invalid answer.')
  H = (16 - ((int(S) + int(G) + int(X))))
  if (int(H) < 1) or (int(H) > 15):
    print('Error. Your lighting is incorrect.')
  else:
    E = str(f)
    I = (ISO2.get(E)) 
    print('You should set your ISO to', I)
    print('Thank you. You have finished this program.')
#ShutterspeedCode
elif f == '3':
  print('You have chosen 📸Shutterspeed📸')
  while True:
    C = input('What would you like to set your 📸ISO📸 to? Enter "list" for a list.')
    C = C.lower()
    if C == 'list':
      print("\n 6400\n 3200\n 1600\n 800\n 400\n 200\n 100\n 50")
    elif C in ISO:
      S = int(ISO.get(C))
      break
    else:
      print('Invalid Answer')
  while True:
    D = input('What would you like to set your 📸Aperture📸 to? Enter "list" for a list.')
    D = D.lower()
    if D == 'list':
      print("\n 2\n 2.8\n 4\n 5.6\n 8\n 11\n 16\n 22")
    elif D in Aperture:
      G = int(Aperture.get(D))
      break
    else:
      print('Invalid answer.')
  H = (16 - ((int(S) + int(G) + int(X))))
  if (int(H) < 1) or (int(H) > 15):
    print('Error. Your lighting is incorrect.')
  else:
    E = str(f)
    I = (Shutterspeed2.get(E)) 
    print('You should set your 📸Shutter-speed📸 to', I)
    print('Thank you. You have finished this program.')