#! python3
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')  # how to download a file
res.status_code     # checking to see if the file saved as a string. Status code 200 means OK
res.raise_for_status() # raises an exception in case there was an error If nothing pops up you are all good.
playFile = open('RomeoAndJuliet.txt','wb') # wb stands for write binary. MUST when you want to save downloaded data to a file

# For loop is needed to write the data into the designated file
for chunk in res.iter_content():
    playFile.write(chunk) # returns how many bytes it wrote in the file

playFile.close()