#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#
# PROGRAMMER: Johannes SB
# DATE CREATED:
# REVISED DATE: 23.03.2021
##

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that
    the statistics calculated as the results are either percentages or counts.
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
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """
    # initialize result dictionary
    results_stats_dic = {}

    # getting file names from dictionary
    filenames = list(results_dic.keys())

    # initialize count values
    n_dogs_img = 0
    n_notdogs_img = 0
    n_match = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed  = 0

    # count numbers from input dictionary
    for idx in range (0, len(filenames), 1):
        # 2) n_dogs_img - number of dog images
        if results_dic[filenames[idx]][3] == 1:
            n_dogs_img += 1
        # 3) n_notdogs_img - number of NON-dog images
        if results_dic[filenames[idx]][3] == 0:
            n_notdogs_img += 1
        # 4) n_match - number of matches between pet & classifier labels
        if results_dic[filenames[idx]][2] == 1:
            n_match += 1
        # 5) n_correct_dogs - number of correctly classified dog images
        if results_dic[filenames[idx]][3] == 1 and results_dic[filenames[idx]][4] == 1:
            n_correct_dogs += 1
        # 6) n_correct_notdogs - number of correctly classified NON-dog images
        if results_dic[filenames[idx]][3] == 0 and results_dic[filenames[idx]][4] == 0:
            n_correct_notdogs += 1
        # 7) n_correct_breed - number of correctly classified dog breeds
        if results_dic[filenames[idx]][3] == 1 and results_dic[filenames[idx]][2] == 1:
            n_correct_breed += 1

    # update dictionary / fill dictionary with information
    # 1) n_images - number of images
    results_stats_dic.update({'n_images' : len(results_dic) })
    # 2) n_dogs_img - number of dog images
    results_stats_dic.update({'n_dogs_img' : n_dogs_img })
    # 3) n_notdogs_img - number of NON-dog images
    results_stats_dic.update({'n_notdogs_img' : n_notdogs_img})
    # 4) n_match - number of matches between pet & classifier labels
    results_stats_dic.update({'n_match' : n_match})
    # 5) n_correct_dogs - number of correctly classified dog images
    results_stats_dic.update({'n_correct_dogs' : n_correct_dogs})
    # 6) n_correct_notdogs - number of correctly classified NON-dog images
    results_stats_dic.update({'n_correct_notdogs' : n_correct_notdogs})
    # 7) n_correct_breed - number of correctly classified dog breeds
    results_stats_dic.update({'n_correct_breed' : n_correct_breed})
    # 8) pct_match - percentage of correct matches
    #     (Optional): Percentage Label Matches ( regardless if they're a dog)
    #     Y Number of label matches
    #     Z Number of images
    #     Percentage of correctly Matched Images ( regardless if they are a dog): Y/Z * 100
    if len(results_dic) > 0:
        pct_match = (n_match / len(results_dic)) * 100
        results_stats_dic.update({'pct_match' : pct_match})
    else:
        results_stats_dic.update({'pct_match' : 0})
    # 9) pct_correct_dogs - percentage of correctly classified dogs
    #    Objective _1_a: Percentage of Correctly Classified Dog Images
    #    A Correctly classified dog images.
    #    B Number of dog images
    #    Percentage of correctly classified "dog" images: A/B * 100
    if n_dogs_img > 0:
        pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100
        results_stats_dic.update({'pct_correct_dogs' : pct_correct_dogs})
    else:
        results_stats_dic.update({'pct_correct_dogs' : 0})
    # 10) pct_correct_breed - percentage of correctly classified dog breeds
    #     Objective _2_: Percentage of Correctly Classified Dog Breeds
    #     E Correctly classified as a particular breed of dog images.
    #     B Number of dog images
    #     Percentage of correctly classified Dog Breed images: E/B * 100
    if n_dogs_img > 0:
        pct_correct_breed = (n_correct_breed / n_dogs_img) * 100
        results_stats_dic.update({'pct_correct_breed' : pct_correct_breed})
    else:
        results_stats_dic.update({'pct_correct_breed' : 0})
    # 11) pct_correct_notdogs - percentage of correctly classified NON-dogs
    #     Objective _1_b: Percentage of Correctly Classified Non-Dog Images
    #     C Correctly classified NOT a dog images.
    #     D Number of NOT a dog images
    #     Percentage of correctly classified "Non-dog" images: C/D * 100
    if n_dogs_img > 0:
        pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100
        results_stats_dic.update({'pct_correct_notdogs' : pct_correct_notdogs})
    else:
        results_stats_dic.update({'pct_correct_notdogs' : 0})

    return results_stats_dic
