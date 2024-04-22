while True:
	print("stone,paper,scissors game with ALEX AI")
	print("1.stone")
	print("2.paper")
	print("3.scissors")
	import random as rd
	mylist=["stone","paper","scissors"]
	aa=(rd.choice(mylist))
	cc=str(input("choice and write Correct word="))
	if (cc==aa):
		print("//////draw/////")
	elif(aa=="paper" and cc=="stone"):
		print("alex = paper")
		print("you = stone")
		print("**********alex win**********")
	elif(aa=="paper" and cc=="scissors"):
		print("alex = paper")
		print("you = scissors")
		print("**********you win**********")
	elif(aa=="stone" and cc=="paper"):
		print("alex = stone")
		print("you = paper")
		print("**********you win**********")
	elif(aa=="stone" and cc=="scissors"):
		print("alex = stone")
		print("you = scissors")
		print("***********alex win***********")
	elif(aa=="scissors" and cc=="stone"):
		print("alex = scissors")
		print("you = stone")
		print("**********you  win***********")
	elif(aa=="scissors" and cc=="paper"):
		print("alex = scissors")
		print("you = paper")
		print("*************alex  win**********");
	qq=str(input("you want more play yes/no"))
	if(qq=="no" or qq=="NO"):
		break
	
	
	

	
		
    
     
    
	

	