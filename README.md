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

Ordinarily this is where K-Means ends. However this project uses then recolours each pixel by finding the closest colour on the palette generated. There are some very effective algorithms for colour quantization of images, such as [scolorq](https://people.eecs.berkeley.edu/~dcoetzee/downloads/scolorq/#sampleimages).
