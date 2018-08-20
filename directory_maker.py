import os
import acoustid
import sys
# define the name of the directory to be created
path = "/home/dayscholars/Desktop/lyceaum_exrecises/project_acoustic/pyacoustid/sample1"

# define the access rights
access_rights = 0o755
API_KEY = 'l4RPd5DsJ4'

try:  
    os.mkdir(path, access_rights)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s" % path)

#directory_path = "/home/dayscholars/Desktop/lyceaum_exrecises/project_acoustic/pyacoustid"
def get_directory():
    print("Please enter the path of directory in which you want to sort the mp3 files")
    directory_path = input("-->")
    return directory_path
    
def search_mp3():
    directory_path = get_directory()
    for file in os.listdir():
        if file.endswith(".mp3"):
            return os.path.join(directory_path, file)

def get_acoustid(mp3_location):
    results = acoustid.match(API_KEY, mp3_location)
    print(results)
    return results

if __name__ == '__main__':
    get_directory()
    get_acoustid(search_mp3())


    
