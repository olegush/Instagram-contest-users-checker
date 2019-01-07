# Instagram contests users checker

The script checks participants of Instagram contests following standart rules and prints approved users list for picking a winner.

For approve user should:
* tag his friend(s)
* like the post
* subscribe to the orginizer account

The script based on library [Instabot](https://github.com/instagrambot/)


### How to install

Python3 should be already installed. Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

.env file with enviroment variables should contain your Instagram login and password. If your post has more than 100 comment its better to create new account for this purposes.
```
LOGIN=your_login
PASSWORD=your_password
```


### Quickstart

Run **main.py** with two arguments: username of contest's orginizer and url to Instagram post

```bash
$ python main.py oxtapas https://www.instagram.com/p/BsMRrzGh_a2/

Approved users (175):
['lindsayanngordon', 'meagnparker', 'nat_munoz', 'alixhop', 'boxesofcatss', 'alexiariches', 'maebers', 'flybirdwin', 'alisa86', 'rainray_s', 'krysta_ahlers', 'turnerincalgary', 'itsmecourtneeeeey', 'yycfoodjunkie', 'allison418', 'idrankhere', 'nahaelia', 'hittingthesauceyyc', 'hugs.and.hearts', 'elysium_summers', 'jjjlllggg', 'krosenke', 'ldiggity_', 'mrs_sandiego_', 'marty_rudy_and_me', 'shelovesthedeal', 'k_wollny', 'nic_adair', 'whitroy', 'smorrison87', 'embagzz', 'loaf2go', 'shirls.l', 'rachellaurenxx', 'alozy', 'm_petrovi', 'pak_to_eating', 'winniesusu00', 'micocabrera', 'raylenealannah', 'codyscheibs', 'kimmikazzi', 'stephb_enroute', 'juliagangji', 'xteeyuu', 'robynpenelope', 'cathk808', 'mikedecline', 'kerrybaking', 'nickyjm88', 'lifewhereweare', 'ezzapet', 'gardens.in.mind', 'baanjen', 'gillian.bruce', 'megan.amber.creative', 'coralstring', 'sheffieldthepug','alison_burton', 'tastebudsyyc', 'heyjanino', 'julie.gathercole', 'deseraeevensonphoto', 'mycookingaromas', 'mhubba32', 'repudiation', 'calgarykatie6', 'ms4tuna', 'justine_a_h', 'lifeofkaf', 'yogalove20', 'adventures.with.dee', 'natkho14','kateyorkyyc', 'calvi._.n', 'cottonleigh', 'brndon.pyne', 'sinbin.tri', 'tiffflynn', 'teatime_circus', 'amartincreative', 'alli456', 'kiki.the.shopaholic', 'trntwrnr', 'chau_mander', 'tamalama_s', 'leelajacobs', 'skreinhart', 'vicki_valentine', 'kmvdanan', 'munchwithlynn', 'saralianne', 'nattner', 'craftlifeyyc', 'merakisupplyco', 'runawaywithcc', 'chan_teezzy', 'dishnthekitchen', 'mjessiman', 'hippolee999', 'vanessafraser', 'latteortwo', 'ontarioandgore', 'jessicarosolmakeup', 'm_a_r_1_3', 'cbridges', 'zuco_dm', 'bornlippystyle', 'allisonjh', 'megwanders2944', 'gutstolive', 'zachary_mohl', 'redpaperboutique', 'browsandblush', 'hangryinyyc', 'vwlho', 'kaelaneats', 'schmirlert', 'love_always_lindsay_dreher', 'jaymalynn79', 'cooking.buddies', 'tonynols', 'april_lee_b', 'teresakkk', 'jessrucie', 'alanajwillerton', 'leahvanloon', 'heyseto', 'skitzilla', 'nicoleeponsonby', 'steph_j_deboice', 'foodmammacom', 'mscrazylady', 'yycfoodiesdiary', 'kazz1972', 'missjennileigh', 'meet_melanie', 'chefbecks92', 'chantel.cruikshank', 'tyknigh', 'jayne_l8', 'tamfran123', 'mandycostache', 'idaviani', 'minson519', 'kyrrs', 'roopiej', 'amandaarbo', 'dustywm', 'poeticallycreative', 'anrensch88', 'ak.kendrick', 'sandi_lynn', 'fernzevnik', 'xoxsandee', 'carolinaayc', 'monastable', 'alex_zarnowski', 'mortgagesbyjessalyn', 'marissrawr', 'flavourfultraveller', 'laura_lovett', 'mkdundas', 'brendanattwell', 'lauraeileenb', 'lanikayp', 'nisansala73', 'misslipton', 'alexrst1', 'jessekiah', 'calgaryfoodslut', 'rosie_j_miller', 'karewint', 'leontaridis', 'pulltheleversuz']
```

This example's execution (>1200 comments) took about 3 hours, so if you want to watch a process, print something in a loop(s)


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
