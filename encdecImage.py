#Reyniel Maglian
#CPSC 353 - Fall 2017
#Steganography Program
#Due: October 31, 2017
#----------------------------------------------------------------------------------------

#Import libraries needed
import sys
import binascii
from PIL import Image

#Encryption
#----------------------------------------------------------------------------------------
#If user wants to encrypt a jpeg image, go through this algorithm
if sys.argv[1] == '-enc':
	#Storing the inputted message into string variable
	textmsg = sys.argv[2]

	#Converting the inputted message from string to binary
	binarytext = ' '.join(format(ord(char), 'b') for char in textmsg)

	#Finding the length of the text and then converting it into binary
	lengthtext = len(binarytext)
	lengthtextbin = '{0:b}'.format(lengthtext)
	#Fill in the rest of the bits with 0s
	while (len(lengthtextbin) < 32):
		lengthtextbin = '0' + lengthtextbin

	#Importing the image that the user wants to use
	picture = Image.open(sys.argv[3])
	picvar = picture.load()
    
	#Finding the size of the jpg picture
	pictureWidth, pictureHeight = picture.size

	#Setting up the image size to work with encrypting the text
	counter = 0
	for i in range(pictureHeight-1, 0, -1):
		for g in range(pictureWidth-1, 0, -1):
			#Get RGB from each pixel
			R, G, B = picvar[g, pictureHeight-1]
		
			#Getting the R value in binary
			Rstr = str(R)
			Rvalbin = ''.join(format(ord(x), 'b').zfill(8) for x in Rstr)
			#Switching the LSB with the length bit
			Rvalbin = Rvalbin[:len(Rvalbin)-1] + lengthtextbin[counter]
			#Converting R binary value to ascii
			tempvar = int(Rvalbin, 2)
			R = tempvar.to_bytes((tempvar.bit_length() + 7) // 8, 'big').decode()
			counter = counter + 1

			#Getting the G value in binary
			Gstr = str(G)
			Gvalbin = ''.join(format(ord(x), 'b').zfill(8) for x in Gstr)
			#Switching the LSB with the length bit
			Gvalbin = Gvalbin[:len(Gvalbin)-1] + lengthtextbin[counter]
			#Converting G binary value to ascii
			tempvar = int(Gvalbin, 2)
			G = tempvar.to_bytes((tempvar.bit_length() + 7) // 8, 'big').decode()
			counter = counter + 1
			
			if counter != 32:
				#Getting the B value in binary
				Bstr = str(B)
				Bvalbin = ''.join(format(ord(x), 'b').zfill(8) for x in Bstr)
				#Switching the LSB with the length bit
				Bvalbin = Bvalbin[:len(Bvalbin)-1] + lengthtextbin[counter]
				#Converting B binary value to ascii
				tempvar = int(Bvalbin, 2)
				B = tempvar.to_bytes((tempvar.bit_length() + 7) // 8, 'big').decode()
				counter = counter + 1
			
			#Load updated RGB back into pixel
			picvar[g, i] = (int(R), int (G), int(B))
			
			#Breaking out of the width loop
			if counter == 32:
				break
		#Breaking out of the height loop
		if counter == 32:
			break

	#Encrypting text into the image
	#Initializing loop counters	
	loopCounter = 0
	lCounter2 = 0
	for h in range(pictureHeight-1, 0, -1):
		for l in range(pictureWidth-1, 0, -1):
			#Get RGB from each pixel
			R, G, B = picvar[l, h]

			#Encrypting for R pixel
			if loopCounter != lengthtext and lCounter2 >= 33:
				Rstr = str(R)
				Rvalbin = ' '.join(format(ord(x), 'b').zfill(8) for x in Rstr)
				#Switiching LSB with the length bit
				Rvalbin = Rvalbin[:len(Rvalbin)-1] + binarytext[loopCounter]
				#Putting R number into R pixel by converting from bin to text
				tempvar = int(Rvalbin, 2)
				R = tempvar.to_bytes((tempvar.bit_length() + 7) // 8, 'big').decode()
				loopCounter = loopCounter + 1
			lCounter = lCounter2 + 1
		
			#Encrypting for G pixel
			if loopCounter != lengthtext and lCounter2 >= 33:
				Gstr = str(G)
				Gvalbin = ' '.join(format(ord(x), 'b').zfill(8) for x in Gstr)
				#Switiching LSB with the length bit
				Gvalbin = Gvalbin[:len(Gvalbin)-1] + binarytext[loopCounter]
				#Putting G number into G pixel by converting from bin to text
				tempvar2 = int(Gvalbin, 2)
				G = tempvar2.to_bytes((tempvar2.bit_length() + 7) // 8, 'big').decode()
				loopCounter = loopCounter + 1
			lCounter2 = lCounter2 + 1
		
			#Encrypting for B pixel
			if loopCounter != lengthtext and lCounter2 >= 33:
				Bstr = str(B)
				Bvalbin = ' '.join(format(ord(x), 'b').zfill(8) for x in Bstr)
				#Switiching LSB with the length bit
				Bvalbin = Bvalbin[:len(Bvalbin)-1] + binarytext[loopCounter]
				#Putting B number into B pixel by converting from bin to text
				tempvar3 = int(Bvalbin, 2)
				B = tempvar3.to_bytes((tempvar3.bit_length() + 7) // 8, 'big').decode()
				loopCounter = loopCounter + 1
			lCounter = lCounter2 + 1
			
			#New RGB into pixel 
			picvar[l, h] = (int(R), int(G), int(B))
		
			#Break out of the width loop if no more text to encrypt
			if loopCounter == lengthtext:
				break
		#Break out of the height loop if no more text to encrypt
		if loopCounter == lengthtext:
			break
	#Saving the uploaded JPEG as a PNG after encrypting
	picture.save(sys.argv[4], 'PNG')
	
#Decryption
#----------------------------------------------------------------------------------------
#If user wants to decrypt an image, go through this algorithm
elif sys.argv[1] == '-dec':
	#Opening and loading the picture to decrypt
	picture = Image.open(sys.argv[2])
	picvar = picture.load()

	#Obtain the size of the image
	pictureWidth, pictureHeight = picture.size
  
	#Getting the length of the text 
	#Initializing counter and variable to store encrypted text length
	loopCounter = 0    
	enctextlength = ''
	for n in range(pictureHeight-1, 0, -1):
		for m in range(pictureWidth-1, 0, -1):
			#Get RGB from each pixel
			R, G, B = picvar[m,n]
	
			#Converting R value to binary
			Rstr = str(R)
			Rvalbin = ' '.join(format(ord(s), 'b').zfill(8) for s in Rstr)
			#Obtaining the LSB
			enctextlength = enctextlength + Rvalbin[len(Rvalbin)-1:]
			loopCounter = loopCounter + 1
	
			#Converting G value to binary
			Gstr = str(G)
			Gvalbin = ' '.join(format(ord(s), 'b').zfill(8) for s in Gstr)
			#Obtaining the LSB
			enctextlength = enctextlength + Gvalbin[len(Gvalbin)-1:]
			loopCounter = loopCounter + 1
			
			#If count reaches the end of the 32nd value bit, exit out of the loop
			if loopCounter == 32:
				break
			
			#Converting B value to binary
			Bstr = str(B)
			Bvalbin = ' '.join(format(ord(s), 'b').zfill(8) for s in Bstr)
			#Obtaining the LSB
			enctextlength = enctextlength + Bvalbin[len(Bvalbin)-1:]
			loopCounter = loopCounter + 1
		#Breaking the height loop	
		if loopCounter == 32:
			break
    
	#Converting the encrypted text length from binary to int
	enctextlength = int(enctextlength, 2)
    
	#Decrypting the text that was encrpyted in the image
	#Initializing the loop counters and variable to store encrpyted text
	enctext = ''
	loopCounter2 = 0
	jCount = 0
	#Decryptying the actual text that was encrypted
	for k in range(pictureHeight-1, 0, -1):
		for l in range(pictureWidth-1, 0, -1): 
			#Get RGB at each pixel
			R, G, B = picvar[l,k]
			
			#Decrypting the R pixel
			if loopCounter != enctextlength and jCount >= 33:
				#Converting from text to binary
				Rstr = str(R)
				Rvalbin = ' '.join(format(ord(s), 'b') for s in Rstr)
				#Obtain the LSB
				enctext = enctext + Rvalbin[len(Rvalbin)-1:]
				#Increment loop counter
				loopCounter2 = loopCounter2 + 1
			#Increment jcount counter			
			jCount = jCount + 1
	
			#Decrypting the G pixel
			if loopCounter != enctextlength and jCount >= 33:
				#Converting from text to binary
				Gstr = str(G)
				Gvalbin = ' '.join(format(ord(s), 'b') for s in Gstr)
				#Obtain the LSB
				enctext = enctext + Gvalbin[len(Gvalbin)-1:]
				#Increment loop counter
				loopCounter2 = loopCounter2 + 1
			#Increment jcount counter			
			jCount = jCount + 1

			#Decrypting the B pixel
			if loopCounter != enctextlength and jCount >= 33:
				#Converting from text to binary
				Bstr = str(B)
				Bvalbin = ' '.join(format(ord(s), 'b') for s in Bstr)
				#Obtain the LSB
				enctext = enctext + Bvalbin[len(Bvalbin)-1:]
				#Increment loop counter
				loopCounter2 = loopCounter2 + 1
			#Increment jcount counter			
			jCount = jCount + 1	
			
			#Break out of loop once finished
			if loopCounter2 == enctextlength:
				break
		if loopCounter2 == enctextlength:
			break
	
	#Decrypting the encrypted text from binary to ASCII
	tempvar = int(enctext, 2)
	dectxt = tempvar.to_bytes((tempvar.bit_length() + 7) // 8, 'big').decode()

	#Output what the encrypted text was and its length
	print("Message: ")
	print(dectxt)
	print("Message length: ")
	print(enctextlength)
