Name: Reyniel Maglian
Class: CPSC 353 - Fall 2017

This program takes a message that the user inputs that wants to be encrpyted and encrypts that message into the JPG image file. Next it manipulates the RGB pixels in the image in the LSB to store the message without showing any difference in the image. Lastly the program can also decrypt an image that has an encrpyted message hidding in it and shows the user what the encrpyted text is and how long that message is. 

To run this code:
-need Python 3+
-need Python Pillow

-----------------------------------------------------------------------------------------
****NOTE: I was not able to get the encryption part of the program to fully work. Got stuck with an error when storing the new updated pixels****

For encryption: 
In the terminal, you navigate to the file directory where encdecImage.py is saved with the image that you want to use for encryption. You then enter the following in the terminal.

For Linux terminal, make sure you have any version over Python 3 to run then enter the following:
$ python3 encdecImage.py -enc "(insert message)" (name of image file to encrypt).jpg (name of image file encrpyted).png 

For Python on Windows, as long as you have any version over Python 3 just enter the following:
python encdecImage.py -enc "(insert message)" (name of image file to encrypt).jpg (name of image file encrpyted).png

It will save the encrypted image in the same directory. 

-----------------------------------------------------------------------------------------

For decryption:
Save the encrypted .png file to the same file directory where the encdecImage.py is located.
In the terminal, navigate to the directory where the encdecImage.py is saved with the images. You then enter the following in the terminal:

For Linux terminal, make sure you have any version over Python 3 to run then enter the following:
$ python3 encdecImage.py -dec (name of encrpyted image).png

For Python on Windows, as long as you have any version over Python 3 just enter the following:
python encdecImage.py -dec (name of encrypted image).png

The terminal should then display what the encrypted text is and the length of that text that was encrypted.

-----------------------------------------------------------------------------------------

LICENSE:

Copyright 2017 Reyniel Maglian

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
