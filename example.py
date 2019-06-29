import yaleorgdirectory
import os

# 'api' name can be whatever is most convenient for your program
api = yaleorgdirectory.YaleOrgDirectory(os.environ['YALE_API_KEY'])

# Get a list
orgs = api.organizations()
for org in orgs:
    print('%s has %d tags.' % (org.name, len(org.tags)))
    print(len(orgs))

# Get a smaller list by tag
residences = api.organizations(['undergradhousing'])
for residence in residences:
    print(residence.name)

# Or get a single organization
hopper = api.organization('Grace Hopper College')
# You can also pass tags to make the search slightly more efficient, but this isn't necessary
print(hopper.website)
