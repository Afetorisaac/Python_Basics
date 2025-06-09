# Welcome to coding with python
#! /usr/bin/python3

#A simple program to make some tricky decisions

print("What is your name?")
name= input()

print("How old are you?")
age = input()

print(name)

if name == "TTM" :
	print("Hello TTM")
	elif int(age) > 50:
		print("You are too young to be a hacker, so you are a script kiddie.")
	elif int(age) > 100:
		print("You are an intermediate hacker")
	elif int(age) > 150:
		print("You are a professional hacker")
	else :
		print("Age cannot be a string or negative integer")
