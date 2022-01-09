arr=[1,2,3,0,'ronk']

# for i in arr:
# 	try:
# 		print(10/i)
# 	except Exception as e:
# 		print("GOT Exception as: ",e.__class__)

for i in arr:
	try:
		print(10/i)
		print(ar)
	except ValueError:
		print("value error occured!")
	except (TypeError, ZeroDivisionError) as e:
		print(e.__class__)
	except Exception as e:
		print("Some error occured!",e.__class__)
	finally:
		print("finally block is executing!")