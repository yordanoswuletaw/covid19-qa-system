
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document")


# Let's first fetch some documents that we want to query
import pandas as pd 
df = pd.read_csv('SAMPLE_COVID_QA_PROCESSED.csv')

# Convert files to dicts
# You can optionally supply a cleaning function that is applied to each doc (e.g. to remove footers)
# It must take a str as input, and return a str.
dicts = df.to_dict('records')

# We now have a list of dictionaries that we can write to our document store.
# If your texts come from a different source (e.g. a DB), you can of course skip convert_files_to_dicts() and create the dictionaries yourself.
# The default format here is:
# {
#    'text': "<DOCUMENT_TEXT_HERE>",
#    'meta': {'name': "<DOCUMENT_NAME_HERE>", ...}
#}
# (Optionally: you can also add more key-value-pairs here, that will be indexed as fields in Elasticsearch and
# can be accessed later for filtering or shown in the responses of the Finder)

# Let's have a look at the first 3 entries:
#print(dicts[:3])

# Now, let's write the dicts containing documents to our DB.


final_dicts = []
for each in dicts:
    tmp = {}
    tmp['text'] = each.pop('body_text')
    tmp['meta'] = each
    final_dicts.append(tmp)

document_store.write_documents(final_dicts)