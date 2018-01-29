
# coding: utf-8

# In[ ]:


# Import the datadotworld module as dw
import datadotworld as dw

# Import the city council votes dataset
dataset = dw.load_dataset("https://data.world/stephen-hoover/chicago-city-council-votes")

# Use describe() to review all the metadata that is downloaded with the dataset. 
# Print it to the screen using pp.pprint().
pp.pprint(dataset.describe())

# Use describe() again to get a description of a specific resource: alderman_votes. Print it to the screen.
pp.pprint(dataset.describe("alderman_votes"))

