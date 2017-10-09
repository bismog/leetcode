from google.appengine.ext import db

class Story(db.Model):
    title = db.StringProperty()
    body = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)

story = Story(title="My title")
story.body = 'My body'
story.put()

stories = story.all().filter('date >=', yesterday).order('-date')
for story in stories:
    print story.title
