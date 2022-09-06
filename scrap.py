import requests
import json


print("Extracting Doctors...")
req  = requests.get("https://intake.steerhealth.io/api/doctor-search", json={"organizationId":"aa1f8845b2eb62a957004eb491bb8ba70a", "size":10000,"page":0})
data = json.loads(req.content)
doctors = data["items"] # array of doctors

print("Total "+str(len(doctors)) + " doctors extracted")
# print(data["items"][-1]["firstName"])
rows = []
for doctor in doctors: 
    newDoc = [ doctor["firstName"],  doctor["lastName"] , doctor["email"], doctor["phoneNumber"], doctor['updatedAt'], doctor['_id']]
    rows.append(newDoc)


# importing csv module
import csv
  
# csv file name
filename = "doctors.csv"
  
# field names
fields = ['First Name', 'Last Name', 'Email', 'Phone', 'Updated At', 'ID']
  
# name of csv file
  
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
      
    # writing the fields
    csvwriter.writerow(fields)
      
    # writing the data rows
    csvwriter.writerows(rows)
