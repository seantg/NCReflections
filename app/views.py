from flask import render_template, Flask, request, url_for, redirect
from app import app
from random import randint




stanza1Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/259718615&amp;auto_play=false&amp;" +
	"hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
stanza1Name = "Stanza 1 Group"
stanza1 = [stanza1Src, stanza1Name]

groupAStanza2Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/259718596&amp;auto_play=false&amp;" +
	"hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
groupAStanza2Name = "Stanza 2 Group A"
groupAStanza2 = [groupAStanza2Src, groupAStanza2Name]

groupBSrc = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/259718608&amp;au" +
	"to_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
groupBName = "Group B"
groupB = [groupBSrc, groupBName]

groupAStanza1Name = "Stanza 1 Group A"
groupAStanza1Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/259718589&amp;auto_play=f" +
	"alse&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
groupAStanza1 = [groupAStanza1Src, groupAStanza1Name]

untitledName = "Untitled"
untitledSrc = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/259718583&amp;auto_play=false&amp;" +
	"hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
untitled = [untitledSrc, untitledName]

groupAName = "Group A"
groupASrc = ("https://w.soundcloud.com/player/?url=https%3A//" +
	"api.soundcloud.com/tracks/259718579&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
groupA = [groupASrc, groupAName]

groupA2Name = "Group A (2)"
groupA2Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/259718574&amp;auto_play=false&amp;" +
	"hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
groupA2 = [groupA2Src, groupA2Name]

stanza2Name = "Stanza 2"
stanza2Src = ("https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/259718567&amp;auto_play=false&amp;" +
	"hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true")
stanza2 = [stanza2Src, stanza2Name]

allFiles = [stanza1, groupAStanza2, groupB, groupAStanza1, untitled, groupA, groupA2, stanza2]
numFiles = 8


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
	soundcloudInfo = {'src': fileChosen[0], 'name': fileChosen[1]}

	return render_template('reflection.html', scInfo=soundcloudInfo)

@app.route('/collection')
def collection():
	return render_template('collection.html', files=allFiles)
