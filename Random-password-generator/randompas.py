#!/usr/bin/env python3
import random
import time
def generate_password():
	return "".join(str(random.randint(0,9))for _ in range(6))

print("Password generator is start generating password.....  Press ctrl+c to stop.")

try:
	while True:
		password = generate_password()
		print("Generated Password: ",password)
		time.sleep(2)

except KeyboardInterrupt:
	print("\nGenerator stopped successfully.")
