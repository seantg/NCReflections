from flask import render_template, Flask, request, url_for, redirect
from app import app
from random import randint




stanza1Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/259718615&amp;auto_play=false&amp;" +
	"hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
stanza1Name = "Stanza 1 Group"
stanza1 = [stanza1Src, stanza1Name]

jon1Name = "What is Something That You Learned?"
jon1Atr = "Jon Catherwood Ginn"
jon1Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud" +
	".com/tracks/261083996&amp;auto_play=false&amp;hide_related=false&amp;" +
	"show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;" +
	"visual=true")
jon1 = [jon1Src, jon1Name, jon1Atr]

jon2Name = "What Is Something You Felt Was Really Difficult?"
jon2Atr = "Jon Catherwood Ginn"
jon2Src = ("https://w.soundcloud.com/player/?url=https%3A//" +
	"api.soundcloud.com/tracks/261084397&amp;auto_play=false&amp;" +
	"hide_related=false&amp;show_comments=true&amp;show_user=true" +
	"&amp;show_reposts=false&amp;visual=true")
jon2 = [jon2Src, jon2Name, jon2Atr]


jon3Name = "What Is Something You Really Enjoyed?"
jon3Atr = "Jon Catherwood Ginn"
jon3Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.c" +
	"om/tracks/261084708&amp;auto_play=false&amp;hide_related=false&amp;show" +
	"_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
jon3 = [jon3Src, jon3Name, jon3Atr]

jon4Name = "What Is Something You Remember From Your Work With Virginia Tech?"
jon4Atr = "Jon Catherwood Ginn"
jon4Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com" +
	"/tracks/261084949&amp;auto_play=false&amp;hide_related=false&amp;show_" +
	"comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
jon4 = [jon4Src, jon4Name, jon4Atr]

courtney1Name = "What was the Hardest Part?"
courtney1Atr = "Courtney Grohs"
courtney1Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tr" +
	"acks/261086538&amp;auto_play=false&amp;hide_related=false&amp;show_comment" +
	"s=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
courtney1 = [courtney1Src, courtney1Name, courtney1Atr]

courtney2Name = "What Was The Hardest Or Easiest Part?"
courtney2Atr = "Courtney Grohs"
courtney2Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/261086767&amp;" +
	"auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show" +
	"_reposts=false&amp;visual=true")
courtney2 = [courtney2Src, courtney2Name, courtney2Atr]


jamie1Name = "How Did You Feel About Working With Different Grade Levels?"
jamie1Atr = "Jamie Simmons"
jamie1Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud" +
	".com/tracks/261087031&amp;auto_play=false&amp;hide_related=false&amp;sho" +
	"w_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
jamie1 = [jamie1Src, jamie1Name, jamie1Atr]

jamie2Name = "What Do You Think Was The Hardest Part?"
jamie2Atr = "Jamie Simmons"
jamie2Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tra" +
	"cks/261087350&amp;auto_play=false&amp;hide_related=false&amp;show_comme" +
	"nts=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
jamie2 = [jamie2Src, jamie2Name, jamie2Atr]

jamie3Name = "What Do You Think You'll Remember Most About This Experience?"
jamie3Atr = "Jamie Simmons"
jamie3Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud" +
	".com/tracks/261087585&amp;auto_play=false&amp;hide_related=false&amp;show_" +
	"comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
jamie3 = [jamie3Src, jamie3Name, jamie3Atr]


jamie4Name = "What Was The Most Fun?"
jamie4Atr = "Jamie Simmons"
jamie4Src = ("https://w.soundcloud.com/player/?url=https%3A//api.sound" +
	"cloud.com/tracks/261087798&amp;auto_play=false&amp;hide_related=fals" +
	"e&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;" +
	"visual=true")
jamie4 = [jamie4Src, jamie4Name, jamie4Atr]

jamie5Name = "What Will You Remember The Most About This Poem?"
jamie5Atr = "Jamie Simmons"
jamie5Src =  ("https://w.soundcloud.com/player/?url=https%3A//api.soundc" +
	"loud.com/tracks/261088009&amp;auto_play=false&amp;hide_related=false&a" +
	"mp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
jamie5 = [jamie5Src, jamie5Name, jamie5Atr]

emily1Name ="What Did You Think Was Hard Throughout This Process?"
emily1Atr = "Emily Heflin"
emily1Src = ("https://w.soundcloud.com/player/?url=https%3A//api.sound" +
	"cloud.com/tracks/261088284&amp;auto_play=false&amp;hide_related=fals" +
	"e&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
emily1 = [emily1Src, emily1Name, emily1Atr]

emily2Name = "What Do You Remember Most?"
emily2Atr = "Emily Hiflin"
emily2Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundc" +
	"loud.com/tracks/261088461&amp;auto_play=false&amp;hide_related=fals" +
	"e&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
emily2 = [emily2Src, emily2Name, emily2Atr]

emily3Name = "What Was One Thing You Enjoyed?"
emily3Atr = "Emily Hiflin"
emily3Src = ("https://w.soundcloud.com/player/?url=https%3A//api.sound" +
	"cloud.com/tracks/261088656&amp;auto_play=false&amp;hide_related=false" +
	"&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
emily3 = [emily3Src, emily3Name, emily3Atr]

hollyName = "What Was Your Favorite Part About The Final Exhibit?"
hollyAtr = "Holly Lesko"
hollySrc = ("https://w.soundcloud.com/player/?url=https%3A//api.soundclou" +
	"d.com/tracks/261089104&amp;auto_play=false&amp;hide_related=false&amp;s" +
	"how_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
holly = [hollySrc, hollyName, hollyAtr]



emily4Name = "What Was One Thing You Learned?"
emily4Atr = "Emily Hiflin"
emily4Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundclo" +
	"ud.com/tracks/261088859&amp;auto_play=false&amp;hide_related=false&amp;s" +
	"how_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
emily4 = [emily4Src, emily4Name, emily4Atr]

jon11Name = "What Do You Remember Most About The Program?"
jon11Atr = "Jon Catherwood Ginn"
jon11Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud" +
	".com/tracks/261089322&amp;auto_play=false&amp;hide_related=false&amp;show" +
	"_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
jon11 = [jon11Src, jon11Name, jon11Atr]

jon12Name = "What Is One Thing You Felt Was Really Difficult To Do?"
jon12Atr = "Jon Catherwood Ginn"
jon12Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud" +
	".com/tracks/261089489&amp;auto_play=false&amp;hide_related=false&amp;sho" +
	"w_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
jon12 = [jon12Src, jon12Name, jon12Atr]

jon13Name = "What Is Something That You Learned?"
jon13Atr = "Jon Catherwood Ginn"
jon13Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud" +
	".com/tracks/261089679&amp;auto_play=false&amp;hide_related=false&amp;show" +
	"_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
jon13 = [jon13Src, jon13Name, jon13Atr]

jon14Name = "What Is Something You Really Enjoyed?"
jon14Atr = "Jon Catherwood Ginn"
jon14Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundclou" +
	"d.com/tracks/261089869&amp;auto_play=false&amp;hide_related=false&amp;s" +
	"how_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
jon14 = [jon14Src, jon14Name, jon14Atr]

allFiles = [jon1, jon2, jon3, jon4, courtney1, courtney2, jamie1, jamie2, jamie3, jamie4, jamie5, emily1, emily2, emily3, emily4, holly, jon11, jon12, jon13, jon14]
numFiles = 20


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/individual/<reflectionNumber>')
def individual(reflectionNumber):
	soundcloudInfo = {'src': allFiles[int(reflectionNumber)][0], 'name': allFiles[int(reflectionNumber)][1]}
	return render_template('reflection.html', scInfo=soundcloudInfo)

@app.route('/random')
def random():
	fileChosen = allFiles[randint(0, numFiles - 1)]
	soundcloudInfo = {'src': fileChosen[0], 'name': fileChosen[1], 'author': fileChosen[2]}

	return render_template('reflection.html', scInfo=soundcloudInfo)

@app.route('/collection')
def collection():
	return render_template('collection.html', files=allFiles)

@app.route('/about')
def about():
	return render_template('about.html')
