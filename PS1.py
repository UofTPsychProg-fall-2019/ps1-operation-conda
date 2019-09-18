#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1
@author: katherineduncan
"""

#%% Part 1: pass the error forward ____________________________________________
# this should be completed one at a time to get practice using GitHub


# there's an error in the definition of x below
# first group member (coder 1), your job is to first correct it 
# and make a new variable with an error for the next group member to fix
# after competign both steps, commit and push your changes to GitHub
coder1 = 'hello world! python line' + str(1) 
print(coder1)

# second group member's error to fix
# from Rebekah: this has a valid output as far as I can see? unless I'm misunderstanding the task shouldn't there be an issue with this?
#Juliana: my mistake! I was trying to be tricky and made '42.' a float, thinking you couldn't combine it with an integer...
#con't: while forgetting that those actually can be added! Updated with a new error
coder2_1 = 42. + 13
print(coder2_1)

# Rebekah: fixed
coder2_2 = str(42) + ' is the meaning of the universe'
print(coder2_2)

# now the second group member should define a variable with an error
# and then commit and push changes to GitHub
# Rebekah: added variable definition with an error
coder3 = this is a string

# etc. until all group members have fixed and made 1 error



#%%  Part 2  find and remove the invalid response______________________________

# Rebekah: added some answers here

# imagine these are a list of reaction times that you recorded 
rt = [400, 450, 500, 440, -1, 410, 570]

# the -1 indicates missing data. Your job is to remove it
# use the index method to find the missing value 
missing_rt = rt.index(-1)

# and then use missing_rt to remove the trial from rt
clean_rt = rt[0:missing_rt] + rt[missing_rt+1:]

# now you have data with more than one missing value
rt_trouble = [400, 450, 500, 440, -1, 410, 570, -1, 400]

# try the same procedure. Does it work? 
# use a comment to explain why or why not below in comments

# Rebekah: Attempting to use the index function only allows you to pick out 
# the first instance of -1 in the list. You would need to run it twice to create 
# a new value for missing_rt after removing the first faulty value, or use a 
# loop to go through the entire list and catch every single one individually.

# now write an if statement that you can use to remove the frist missing value 
# only when there is a missing value (-1) in a list 
# this statement should always generate a clean_rt list; if there's no missing
# data clean_rt is set to the original rt list.   



# for the last section, you will work with a list of lists:
rt_new = [400, 450, 500, 440, -1, 410, 570]
trial_num = [1,2,3,4,5,6,7]
accuracy = [0, 1, 0, 0, 1, 0]
data = [rt_new, trial_num, accuracy]

# this master list combines information about each trial in an experiment,
# where index 0 in each sublist refers to data from the first trial, etc.
# using the same appraoches as above, find the trial with missing rt data
# and remove it from all sublists in data 
# be sure to only work with the master data list, to practice indexing 
# lists of lists

