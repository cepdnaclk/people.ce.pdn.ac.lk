# Downloads staff pages that are in google drive (For staff members that dosen't have a github account)
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
# Instructions: https://docs.google.com/document/d/e/2PACX-1vT_4ZN2C4hkgqNFhTkYqY9C9b2qfMroM9m9eZV0gVgINSn9BpuTWPpgesDOY4tiplLAdkF8lS7IfBqV/pub

from google_drive_downloader import GoogleDriveDownloader as gdd  # pip install googledrivedownloader
import os

# add all the files that need to be downloaded here
filesToDownload = [
    {
        # https://drive.google.com/file/d/1z1wv6wgyqxghiCAuFlhlVkcg1ialjLhd/view?usp=sharing
        'fileID': "1z1wv6wgyqxghiCAuFlhlVkcg1ialjLhd",
        'downloadPath': "../pages/staff/academic-staff/janaka-alawatugoda.html"
    }
]

for each in filesToDownload:
    # first delete the exisiting file
    os.remove(each['downloadPath'])

    # download new file from drive
    gdd.download_file_from_google_drive(file_id=each['fileID'], dest_path=each['downloadPath'])
