# colour-quantizing
This project performs colour quantization with a k-means clustering algorithm.

## Usage
Run this code in the commandline by calling```
$ python main.py IMAGE-PATH K-VALUE```
It will display the results of the algorithm in a popup window using the Pillow image processing library.

## What is Colour Quantization?
Colour quantization reduces the amount of colours in an image while maintaining its detail. It can be thought of as repainting a picture with a smaller palette of colours.

## What is K-Means Clustering?
K-Means Clustering is a process that finds the natural clusters inside data. In this case, we're using data in the form of RGB pixels in an image, so the algorithm finds a palette of `K-VALUE` distinct colours that roughly approximate the image.

## Additional Notes
Ordinarily K-Means doesn't go further than producing the clusters. However this project then performs colour quantization by recolouring each pixel to the nearest colour on the palette generated. There are some very effective domain-specific algorithms for colour quantization of images, such as [scolorq](https://people.eecs.berkeley.edu/~dcoetzee/downloads/scolorq/#sampleimages).
