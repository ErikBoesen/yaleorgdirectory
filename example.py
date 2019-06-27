import yaleorgdirectory
import os

# "api" name can be whatever is most convenient for your program
api = yaleorgdirectory.YaleOrgDirectory(os.environ['YALE_API_KEY'])

orgs = api.organizations()
for org in orgs:
    print(org.website)
