# Steganography

## Introduction
Steganography is a mechanism for hiding pieces of data within image files. As we know images are arrays of bytes that represent a color in binary, cause 1 byte equals 8 bytes, so each entry represent an 8-digit number. Thus, each pixel follows the RGB format. Red, green and blue are the main colors and by putting values from 0 to 255, we can make different combinations, because of this we get a binary number of each color. As technology grew, people realized 8 bit color were short, because of this decided working in a new image representation, so 32-bit color borned. It allow us to put 2 bytes in each row, and for that we'll get 16 bits and $2^{16}$ colors.

With steganography we modify the pixel values, doing this we are changing the RGB binary source (red, blue and green intensities), for this we use LSB technique. Least Significant Bit (LSB) gives a way to modify last bit of every pixel, replacing with a bit of our message, for that we must convert string to binary, we doesn't want to modify MSB (Most Significant Bit) cause image will change approx 99%.

[![bit changes - javatpoint](https://static.javatpoint.com/python/images/image-steganography-using-python3.png)](https://www.javatpoint.com/image-steganography-using-python)