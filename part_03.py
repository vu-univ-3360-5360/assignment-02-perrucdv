
# coding: utf-8

# In[ ]:


alderman_votes
Out[1]: 
{'format': 'csv',
 'name': 'alderman_votes',
 'path': 'data/alderman_votes.csv',
 'schema': {'fields': [{'description': 'Note that some entries contain a full name and others only have a last name.',
    'name': 'alderman',
    'rdfType': 'http://www.w3.org/2001/XMLSchema#string',
    'title': 'Alderman',
    'type': 'string'},
   {'description': 'VOTE KEY: Y=Yes; N=No; A=Absent; NV=Not Voting;  E=Excused; V=Vacant R=Recusals from voting',
    'name': 'vote',
    'rdfType': 'http://www.w3.org/2001/XMLSchema#string',
    'title': 'Vote',
    'type': 'string'},
   {'name': 'ward',
    'rdfType': 'http://www.w3.org/2001/XMLSchema#integer',
    'title': 'Ward',
    'type': 'integer'},
   {'description': 'YYYY-MM-DD',
    'name': 'date',
    'rdfType': 'http://www.w3.org/2001/XMLSchema#date',
    'title': 'Date',
    'type': 'date'},
   {'name': 'record',
    'rdfType': 'http://www.w3.org/2001/XMLSchema#string',
    'title': 'Record',
    'type': 'string'}]}}

len(alderman_votes['schema']['fields'])
Out[2]: 5


