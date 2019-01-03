#!/usr/bin/python3

import subprocess


def attempt(password):
	subprocess.getoutput("echo '"+password.replace("'", "'\"'\"'")+"' > test\n")
	out = subprocess.getoutput("udisksctl unlock -b /dev/sda3 --key-file test")

	if out.find("Failed to activate device") >= 0:
		return "badpass"
	else:
		print(out)
		return "unknown"
	

def create_possibilities():
	out = []
	return out
			

def main():
	pos = create_possibilities()

	for idx, x in enumerate(pos):
		print("Attempting #", 215 + idx)
		res = attempt(x)
		if res != "badpass":
			print("Password ", x, " has unknown response")
			break

if __name__ == "__main__":
	main()
