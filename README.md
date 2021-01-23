# soln2021jan22

Status: unfinished

## Things that remain:

I only was able to get to part 1. I am almost done with it, but fields under different subsets are still included multiple times, and the subset name is also included as a field which is behavior I would fix. I would fix this by checking for all NaNs to the right of a field name (but also under a category), that would denote a subset name that is included in column B, but should not be included in the field names.

I still need to address the Timestamps being read as 2021-01-18 instead of the last day of the given YYYY-MM, for instance 2018-01-31. I would do this by changing the parameters being passed in to read_excel so that it interprets those values correctly. This should be able to be done using the docs here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html, but also making sure to match the version of pandas that you are using.

I have also not gotten to the point of refactoring the code in order to organize it by classes and their member variables/functions.

Lastly, I have not gotten around to adding unit tests yet. I was planning on doing so using pytest.

## My Script:

I start by using pandas.read_excel to import the excel sheet into a dataframe. This is not always perfect as sometimes the data types can get misinterpreted and other formatting aspects can mess up the import such as whitespace, but it is a good place to start.

I then iterate over the values in column B, deciding how to treat them based on the values to the right of it and the 1 value to the left if populated. For the values to the right, I check if they are all Timestamps.

I also check if the category has already been seen. If so, we make sure to not add that category again so as to not have duplicates. But, only add the new information for that row (such as subset) to the already existing respective category object.

Lastly, after all the rows have been iterated over and the final object is fully created, I dump the object out to a json file.

