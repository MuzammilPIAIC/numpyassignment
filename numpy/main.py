{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from PIL import Image\n",
    "import os\n",
    "from resizeimage import resizeimage\n",
    "\n",
    "imageSize = (200, 200)\n",
    "picsDir = os.listdir('./photos')\n",
    "rootDir = './photos/'\n",
    "\n",
    "\n",
    "# THE FILES FINDER FUNCTION\n",
    "# It takes path of the Photos folder\n",
    "# it will return the number of pics in it and the list of all available pics.\n",
    "def filesfinder(directory):\n",
    "    files_list = []\n",
    "\n",
    "    for pic in directory:\n",
    "        im = Image.open(rootDir + pic)\n",
    "\n",
    "        files_list.append(im)\n",
    "\n",
    "    length_of_list = len(files_list)\n",
    "\n",
    "    return length_of_list, files_list\n",
    "\n",
    "\n",
    "# THE RESIZING FUNCTION\n",
    "# It takes the image size\n",
    "# It will return the list of resized images\n",
    "def resizing(image_size):\n",
    "    resized_images = []\n",
    "    for img in picsDir:\n",
    "        image = Image.open(rootDir + img)\n",
    "        image = resizeimage.resize_crop(image, image_size)\n",
    "        # image.thumbnail(image_size)\n",
    "        resized_images.append(image)\n",
    "\n",
    "    return resized_images\n",
    "\n",
    "\n",
    "# THE CONVERT TO NUMPY ARRAY FUNCTION\n",
    "# It takes list of resized images\n",
    "# It will return numpy array contain all 20 images\n",
    "def converttonumpyarray(list_of_resized_images):\n",
    "    for image in list_of_resized_images:\n",
    "        array1 = np.array(image).reshape(200, 200, 3)\n",
    "        for img in list_of_resized_images:\n",
    "            array2 = np.array(image).reshape(200, 200, 3)\n",
    "            array1 = np.concatenate((array1, array2))\n",
    "        break\n",
    "\n",
    "    return array1\n",
    "\n",
    "#THE MAIN FUNCTION\n",
    "#It runs all the local funtions\n",
    "#it returns the numpy array of shape(200,200,3) containing all the images\n",
    "def main():\n",
    "    # Finding files\n",
    "    num_of_files, list_of_pics = filesfinder(picsDir)\n",
    "    print('Number of files are : ', num_of_files)\n",
    "\n",
    "    # Resizing pictures\n",
    "    resized_images = resizing(imageSize)\n",
    "    print(\"Resized images are: \")\n",
    "    print(resized_images)\n",
    "\n",
    "    # Converting to numpy array\n",
    "    nparray = converttonumpyarray(resized_images)\n",
    "    print(\"Numpy array of 20 images are:\")\n",
    "    print(nparray)\n",
    "\n",
    "    return nparray\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
