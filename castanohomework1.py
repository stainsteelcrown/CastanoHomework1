#!/usr/bin/env python
# Andrew Castano
# Casenco Inc.

import webapp2
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

form="""
<form method="post"> 
    <label>
    <h1>Enter some text to Rot13</h1>
    <br>
    <textarea name="text" rows="10" cols="80">
        %(text)s
    </textarea>
    </label>
    <br>
    <input type="submit">
</form> 
"""

class MainPage(webapp2.RequestHandler):

    def write_form(self, text="") 
        self.response.out.write(form % {"text": text}) 
                                    
    def get(self):
        self.write_form("Begin Here")

    def post(self):
        user_input = self.request.get('text') 
        self.write_form(user_input)

application = webapp2.WSGIApplication([('/', MainPage),
], debug=True)
