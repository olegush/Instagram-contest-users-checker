# Instagram contest users checker

The script checkspartisipans of Instagram contests following standart rules:
* tagged a friend(s)
* liked a upload_to_instagram
* subascribed to orginizer account

downloads random comic from [xkcd.com](https://xkcd.com/) and post it on the wall of [VK](https://vk.com/) group


### How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
You should:
- create VK group [https://vk.com/groups?w=groups_create](https://vk.com/groups?w=groups_create)
- create standalone VK application [https://vk.com/editapp?act=create](https://vk.com/editapp?act=create)
- get client_id of the application
- get access_token with 'photos', 'wall' and 'offline' permissions [https://vk.com/dev/access_token](https://vk.com/dev/access_token)


.env file with enviroment variables should contain your CLIENT_ID and TOKEN
```
CLIENT_ID=client_id
TOKEN=token
```


### Quickstart

Just run **main.py**
```bash
$ python salary.py
1. Got random comic ID:1630

2. Data from XKCD for comic "quadcopter.png" was fetched

3. The comic "quadcopter.png" was downloaded to current dir

4. Got url to upload on VK server

5. The comic was uploaded on the server 852216

6. The comic got upload ID:456239425

7. The post published on the wall of the group

8. Image "quadcopter.png" successfully removed
```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).





# Space Instagram

First script, the **fetch_spacex.py** fetches photos of the latest launch of [SpaceX program](https://www.spacex.com/). The second, **fetch_hubble.py** fetches photos of [The Hubble Telescope](http://hubblesite.org/), collection "news". And the third, **upload_to_instagram.py** prepares and publishes photos to Instagram account.


### How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

.env file with enviroment variables should contain your password and login to Instagram.
```
LOGIN=your_login
PASSWORD=your_passwod
```


### Quickstart

Run **fetch_spacex.py** or/and **fetch_hubble.py** to fetch photos, wich will be save in **image** folder. Then run **upload_to_instagram.py** it prepares photos in the **images/for_instagram** folder and uploads them to Instagram account.
