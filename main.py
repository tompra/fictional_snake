import requests
from bs4 import BeautifulSoup
import pandas

github_username = input('Input Github Account: ')
url = f'https://github.com/{github_username}'
resp = requests.get(url)

if resp.status_code == 200:
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    
    profile_img = soup.find('img', {'class': 'avatar avatar-user width-full border color-bg-default'})
    profile_img_url = profile_img['src'] if profile_img else 'Profile image not found'
    

    follower_container = soup.find('a', href=lambda href: href and f"/{github_username}?tab=followers" in href)
    followers = follower_container.find('span', {'class': 'text-bold color-fg-default'}).text if follower_container else '0'
    

    following_container = soup.find('a', href=lambda href: href and f"/{github_username}?tab=following" in href)
    following = following_container.find('span', {'class': 'text-bold color-fg-default'}).text if following_container else '0'

    location_user = soup.find('li', {'itemprop': 'homeLocation'})
    location = location_user.find('span', {'class': 'p-label'}).text if location_user else 'Location not found'
    

    website_user = soup.find('li', {'data-test-selector': 'profile-website-url'})
    website = website_user.find('a', {'class': 'Link--primary'}).get('href') if website_user else 'Not personal website'

    
    linkedin_user = soup.find('li', {'itemprop': 'social'})
    linkedin_url = linkedin_user.find('a', {'class': 'Link--primary'}).get('href') if linkedin_user else 'Not linkedin profile'


    bio_user = soup.find('div', {'class' : "p-note user-profile-bio mb-3 js-user-profile-bio f4"})
    bio = bio_user.text if bio_user else 'No bio'
        

    repo_user = soup.find('a', {'data-tab-item': 'repositories'})
    number_repo_user = repo_user.find('span', {'class': 'Counter'}).text if repo_user else '0'
    
    repo_user_url = repo_user.get('href') if repo_user else 'No repositories'
    repositories_url = 'https://github.com' + repo_user_url
    
     
    user_data = {
        'Profile Image': profile_img_url,
        'Followers': followers,
        'Following': following,
        'Users Location': location,
        'Personal Website': website,
        'Linkedin Profile': linkedin_url,
        'User Bio': bio,
        'Number of repositories': number_repo_user,
        'Link to repositories': repositories_url
    }
        
    df = pandas.DataFrame([user_data])
    
    print(df)
 

else:
    print(f'Failed to fetch the URL. Status code: {resp.status_code}')




