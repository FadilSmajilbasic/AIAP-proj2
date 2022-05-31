## AI Applications miniproject 2

##### Fadil Smajilbasic & Fabian Freitag

## OpenCV

### What is it used for?

OpenCV stands for Open Computer Vision. It offers a very exhaustive framework for everything related to computer vision. OpenCV can be used for very basic tasks like opening an Image or a Video in a python project and editing these pictures. One option it offers, that will be used a lot is to greyscale an Image, since many of the other ressources provided with OpenCV require an image to be in greyscale. In our example we use OpenCV to detect a Face in an Image. This could be extended to use a Webcam and detect Faces in a livestream.

OpenCV includes a statistical machine learning library that contains:

- Boosting
- Decision tree learning
- Gradient boosting trees
- Expectation-maximization algorithm
- k-nearest neighbor algorithm
- Naive Bayes classifier
- Artificial neural networks
- Random forest
- Support vector machine (SVM)
- Deep neural networks (DNN)

### How do you use it

To use openCV you have to install it using: `pip install opencv-python`
And then import it in your python file using: `import cv2`

OpenCV can be used to display images, draw shapes over images (recangles, circles, lines, elippses, polygons, and text), apply filter to images (grayscale, color filter, blur,...)

Since videos are just a sequence of images, the same modifications can be done to videos as well.

### The Learning curve

The documentation of OpenCV, which can be found [here](https://docs.opencv.org/4.5.5/) for the latest version, is not very usefull. It contains all the classes methods, parameters and return values and in some cases there are even examples, but it is rather chaotic and browsing trough the documenteation you feel like your are in a maze and lost. While making the example project and doing our research we often found ourselves searching for explanations or solutions on online forums like stackoverflow or articles that describe the usage of some method better than the documentation itself, and we feel like that should not be the case with a well known library as OpenCV.

### Developer adoption

OpenCV is well known to developers in general. The project initially released in June 2000 has since gained a lot of traction and

### Closing statements

##### Sources:

- [Project idea](https://itsourcecode.com/free-projects/python-projects/handwritten-digit-recognition-in-python-with-source-code/)
- [Reference article](https://pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/)
