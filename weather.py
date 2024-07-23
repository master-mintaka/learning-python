temperature = int(input("What's the temprature: "))

if temperature > 80:
    print("It's to hot.")
    print("Better stay inside")
elif temperature < 60:
    print("Very cold to stay outside")
else:
    print("Enjoy the out door")

#Simple version
if temperature > 80 or temperature < 60:
    print("Please stay inside")
else:
    print("Go out and take the world!!!")

