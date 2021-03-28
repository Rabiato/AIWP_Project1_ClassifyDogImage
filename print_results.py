#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: Johannes SB
# DATE CREATED:
# REVISED DATE: 24.03.2021

def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and
                            0 = pet Image 'is-NOT-a' dog.
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image
                            'as-a' dog and 0 = Classifier classifies image
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value
      model - Indicates which CNN model architecture will be used by the
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and
                             False doesn't print anything(default) (bool)
      print_incorrect_breed - True prints incorrectly classified dog breeds and
                              False doesn't print anything(default) (bool)
    Returns:
           None - simply printing results.
    """
    # getting file names from dictionary
    filenames = list(results_dic.keys())

    # print statement that indicates which of the three CNN model architectures
    print('CNN model architectures used is: {} \n'.format(model))

    # print Number of Images, Number of Dog Images, Number of "Not-a" Dog Images
    print('The Number of Images is: {} \n'.format(len(filenames)))
    print('The Number of Number of Dog Images is: {} \n'.format(results_stats_dic['n_dogs_img']))
    print('The Number of Number of \"Not-a\" Dog Images is: {} \n'.format(results_stats_dic['n_notdogs_img']))

    # print
    # % Correct Dogs
    # % Correct Breed
    # % Correct "Not-a" Dog
    # % Match (optional - this includes both dogs and not-a dog)
    for key in results_stats_dic.keys():
        if key[0:3] == 'pct':
            print('Statistic: {} Value: {} \n'.format(key, results_stats_dic[key]))

    # if print_incorrect_dogs = True prints incorrectly classified dog images and
    # False doesn't print anything(default) (bool)
    if print_incorrect_dogs == True:
        # Some dogs were misclassified:
        if results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] !=\
        results_stats_dic['n_images']:
            for idx in range (0, len(filenames), 1):
                if sum(results_dic[filenames[idx]][3:]) == 1:
                    print('misclassified dog: pet image label is {} and classifier label is {} \n'\
                          .format(results_dic[filenames[idx]][0],results_dic[filenames[idx]][1]))

    # print_incorrect_breed - True prints incorrectly classified dog breeds and
    # False doesn't print anything(default) (bool)
    if print_incorrect_breed == True:
        if results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
            # print the pet image and classifier labels for misclassified breeds
            for idx in range (0, len(filenames), 1):
                if sum(results_dic[filenames[idx]][3:]) == 2:
                    if results_dic[filenames[idx]][2] == 0:
                        print('misclassified breed: pet image label is {} and classifier label is {}\n'\
                              .format(results_dic[filenames[idx]][0],results_dic[filenames[idx]][1]))
