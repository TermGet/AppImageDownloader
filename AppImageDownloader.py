import requests, json, os

url = 'https://appimage.github.io/feed.json'
r = requests.get(url)
data = r.json()['items']


appimage_name = input('Name: ')
appimage_exists = False
for entry in data:
    if entry['name'].lower() == appimage_name.lower(): #we found it!
            
        try: #check if url exists
            appimage_exists = True
            appimage_release_url = entry['links'][-1]['url']
            print(f"url: {appimage_release_url}")
            appimage_download_url = appimage_release_url.replace('github.com', 'api.github.com/repos') + "/latest"
            print("Downloading AppImage...")
            os.system('curl -s ' + appimage_download_url + ' \
            | grep "browser_download_url.*AppImage" \
            | cut -d : -f 2,3 \
            | tr -d \\" \
            | wget -qi -')
            print("Done!")
            exit()

        except TypeError: #No link
            print(f'The AppImage "{appimage_name}" doesn\'t have a download URL. This means that it is probably not hosted on GitHub. Unfortenately, this script only works with GitHub releases of AppImages')

        
if appimage_exists == False:
    print(f'The AppImage "{appimage_name}" doesn\'t exist. If an AppImage is missing, please report it to AppImageHub.')
