from flask import Flask, render_template, redirect, escape, session, request, url_for
from sample import birthday

app = Flask(__name__)

@app.route('/')
def index ():
    # this is used to "setup" the session with starting values
    session['lyrics'] = birthday.START
    return redirect(url_for("sing"))

@app.route("/sing", methods=['GET', 'POST'])
def sing():
    lyrics = session.get('lyrics')
    if request.method == "GET":
        if lyrics:
            song = birthday.load_lyrics(lyrics)
            return render_template("lyrics.html",song = song)
        
        else:
            return render_template("drama.html")

    else:
        action = request.form.get('action')
        if lyrics and action:
            song = birthday.load_lyrics(lyrics)
            next_song = song.sing_me_a_song(action)

            if not next_song:
                session['lyrics'] = birthday.lyrics_name(lyrics)
            else:
                session['lyrics'] = birthday.lyrics_name(next_song)

        return redirect(url_for("sing"))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == "__main__":
    app.run()