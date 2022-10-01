from flask import Flask, render_template
import datetime as dt
import random

app = Flask(__name__)

Qs = ["Never have I ever played hooky from school or work","Never have I ever stolen anything","Never have I ever missed a flight","Never have I ever drunk-dialed my ex","Never have I ever gotten lost alone in a new Place","Never have I ever bribed someone","Never have I ever sang karaoke","Never have I ever broken a bone","Never have I ever lived alone","Never have I ever lied to law enforcement","Never have I ever gotten a tattoo","Never have I ever used a fake ID","Never have I ever got seriously hungover","Never have I ever used someone else’s toothbrush","Never have I ever fallen asleep in public","Never have I ever fought in public","Never have I ever dined and dashed","Never have I ever had to go to court","Never have I ever been to a destination wedding","Never have I ever lied to a boss","Never have I ever crashed an ex's wedding","Never have I ever pranked someone","Never have I ever regifted a gift","Never have I ever trolled someone on social media","Never have I ever climbed out of a window","Never have I ever got on the wrong train or bus","Never have I ever cursed in a place of worship","Never have I ever snooped through someone’s stuff","Never have I ever tried marijuana","Never have I ever gone 24 hours without showering","Never have I ever gone on a solo vacation","Never have I ever gone on a road trip","Never have I ever ate an entire pizza by myself","Never have I ever saved a life","Never have I ever got a tattoo","Never have I ever wanted to be on a reality TV show","Never have I ever started a fire","Never have I ever gotten stopped by airport security","Never have I ever gone viral online","Never have I ever left gum in a public space","Never have I ever slept outdoors for an entire night","Never have I ever made a speech in front of 100 people or more","Never have I ever lied to my best friend about who I was with","Never have I ever left someone on read","Never have I ever made up a story about someone who wasn’t real","Never have I ever believed something was haunted","Never have I ever been the alibi for a lying friend","Never have I ever pulled an all-nighter","Never have I ever regretted an apology","Never have I ever pretended I was sick for attention","Never have I ever disliked something that I cooked","Never have I ever deleted a post on social media because it didn’t get enough likes","Never have I ever thrown a drink at someone","Never have I ever binged an entire series in one day","Never have I ever been blackout drunk","Never have I ever pretended to be sick to get out of something"]

Player = ["Palak","Raja","Bhashkar","Pronoy","Bharat","Nimma","Fahima","Amrita","Vikash","Renu","Namrata"]

@app.route("/question")
def question():# df):
    return '<br><br><br><br><br><br><br><br><br><br><br><center><h1>{}</h1></center>'.format(random.choice(Qs))

@app.route("/player")
def player():# df):
    return '<br><br><br><br><br><br><br><br><br><br><br><center><h1>{}</h1></center>'.format(random.choice(Player))
    
@app.route("/both")
def app_name():# df):
    return '<br><br><br><br><br><br><center><h1>{}</h1></center><br><br><br><br><br><center><h1>{}</h1></center>'.format(random.choice(Qs),random.choice(Player))
    
@app.route("/special")
def special():# df):
    return '<br><br><br><br><br><br><center><h1>Never have I ever lied about my age</h1></center><br><br><br><br><br><center><h1>Some boss or director! ;P</h1></center>'
    
if __name__ == "__main__":
    app.run(debug=True)