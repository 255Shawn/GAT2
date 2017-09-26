from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


##DRIVE = build('drive','v3', http=creds.authorize(Http()))
gauth = GoogleAuth()
drive = GoogleDrive(gauth) # Create GoogleDrive instance with authenticated GoogleAuth instance
#file_service = drive.files()

#file_service = drive.files()


#data = drive.ListFile().get(fileId=file['id'], fields='*').execute()




# Auto-iterate through all files in the root folder.
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))



page_token = None
while True:
    #response = drive_service.files().list(q="mimeType='image/jpeg'",

    response = drive.files().list(q="mimeType='image/jpeg'",
                                          spaces='drive',
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
    for file in response.get('files', []):
        # Process change
        print 'Found file: %s (%s)' % (file.get('name'), file.get('id'))
    page_token = response.get('nextPageToken', None)
    if page_token is None:
        break;