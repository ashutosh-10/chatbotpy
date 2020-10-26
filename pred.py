def adder(nums):

	return sum(nums)



def predict(msg):
	resp=  f"invalid"

	msg = msg.split(' ')
	if len(msg)>=2:
		nums = list(map(int,msg[1:]))
	if msg[0] =='add':
		
		resp = f"the addition is : {adder(nums)}"
	return resp



if __name__ == "__main__":
	print(predict("ok"))