#!/usr/bin/env python
# Andrew Castano
# Casenco Inc.

import webapp2
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

form="""
<form method="post"> 
    <h1>Enter some text to Rot13</h1>
    <br>
    <textarea style="width: 350px; height: 150px;" name="rot13" value=%(rot13)s> 
    </textarea>
    <br>
    <input type="submit">
</form> 
"""

class MainPage(webapp2.RequestHandler):

    def write_form(self, error="", rot13=""):
        self.response.out.write(form) 
                                    
    def get(self):
        self.write_form()

    def post(self):
        user_input = self.request.get('rot13')

application = webapp2.WSGIApplication([('/', MainPage),
], debug=True)
