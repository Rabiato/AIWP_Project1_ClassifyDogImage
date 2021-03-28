#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Johannes SB
# DATE CREATED:
# REVISED DATE: 21.03.21
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function

    filenames = listdir(image_dir)
    # alternative way to filter out file if starts with .
    # filenames = [f for f in listdir(image_dir) if not f.startswith('.')]
    # however, solved in if statement later
    results_dic = dict()

    # Creates empty pet list
    pet_labels = []

    # Determines number of items in dictionary
    items_in_dic = len(results_dic)

    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(filenames), 1):
        # Skips file if starts with . (like .DS_Store of Mac OSX) because it
        # isn't an pet image file
        if filenames[idx][0] != ".":

            # Sets pet_image variable to a filename
            pet_image = filenames[idx]

            # Sets string to lower case letters
            low_pet_image = pet_image.lower()

            # Splits lower case string by _ to break into words
            word_list_pet_image = low_pet_image.split("_")

            # Create pet_name starting as empty string
            pet_name = ""

            # Loops to check if word in pet name is only
            # alphabetic characters - if true append word
            # to pet_name separated by trailing space
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_name += word + " "

            # Strip off starting/trailing whitespace characters
            pet_name = pet_name.strip()
            pet_labels.append(pet_name)

            # Adds new key-value pairs to dictionary ONLY when
            # key doesn't already exist.
            # This dictionary's value is a List that contains only
            # one item - the pet image label
            if filenames[idx] not in results_dic:
                results_dic[filenames[idx]] = [pet_labels[idx]]

    return results_dic
