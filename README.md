# nyc-zcta-data-helpers
Python helper and data parser scripts for analyzing NYC data on the ZCTA level. Built for Group X's CIS9650 project.

ZipToZCTA:
To put ZCTA data into your file, given your file has a zipcode field:
  Put your file in same folder
  Run nycloc.py
  Follow prompts in IPython window
  Look for new file in same folder

Note that all files in main folder and the zip_to_zcta10_nyc_with_NBH.csv file in a Datafiles folder is required to run this program.

Also, if you want to just quickly get the ZCTA in your code, you can import nycloc, moving all files into your directory, and call getZCTAValueFromZip.  This is less efficient than the file method, though.
