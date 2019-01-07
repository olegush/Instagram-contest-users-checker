# Instagram contest users checker

The script checkspartisipans of Instagram contests following standart rules:
* tagged a friend(s)
* liked a upload_to_instagram
* subascribed to orginizer account

Based on library [Instabot](https://github.com/instagrambot/)


### How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
.env file with enviroment variables should contain your Instagram login a nd password
```
LOGIN=your_login
PASSWORD=your_password
```


### Quickstart

Run **main.py** with two arguments: username of contest's orginizer and url to Instagram post

```bash
$ python main.py oxtapas https://www.instagram.com/p/BsMRrzGh_a2/

Approved users (175):
['lindsayanngordon', 'meagnparker', 'nat_munoz', 'alixhop', 'boxesofcatss', 'alexiariches', 'maebers', 'flybirdwin', 'alisa86', 'rainray_s', 'krysta_ahlers', 'turnerincalgary', 'itsmecourtneeeeey', 'yycfoodjunkie', 'allison418', 'idrankhere', 'nahaelia', 'hittingthesauceyyc', 'hugs.and.hearts', 'elysium_summers', 'jjjlllggg', 'krosenke', 'ldiggity_', 'mrs_sandiego_', 'marty_rudy_and_me', 'shelovesthedeal', 'k_wollny', 'nic_adair', 'whitroy', 'smorrison87', 'embagzz', 'loaf2go', 'shirls.l', 'rachellaurenxx', 'alozy', 'm_petrovi', 'pak_to_eating', 'winniesusu00', 'micocabrera', 'raylenealannah', 'codyscheibs', 'kimmikazzi', 'stephb_enroute', 'juliagangji', 'xteeyuu', 'robynpenelope', 'cathk808'
.........
```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
