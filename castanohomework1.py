#!/usr/bin/env python
# Andrew Castano
# Casenco Inc.

import webapp2
import cgi
import string

def escape_html(s):
    return cgi.escape(s, quote = True)

form="""
<form method="post"> 
    <label>
    <h1>Enter some text to Rot13</h1>
    <textarea name="text" rows="10" cols="80">%(text)s</textarea>
    </label>
    <br>
    <input type="submit">
</form> 
"""

def rot13(user_input):
    upper = string.uppercase
    lower = string.lowercase
    alpha_str = ""
    for i in user_input:
        if i.isalpha():
            if i.isupper():
                l = upper.index(i)
                i = upper[(l+13)%len(upper)]
            else:
                l = lower.index(i)
                i = lower[(l+13)%len(upper)]
            
            alpha_str = alpha_str + i
        else:
            alpha_str = alpha_str + i
    return alpha_str

class MainPage(webapp2.RequestHandler):

    def write_form(self, text=""): 
        self.response.out.write(form % {"text": escape_html(text)}) 
                                    
    def get(self):
        self.write_form()

    def post(self):
        user_input = self.request.get('text') 
        rotty = rot13(user_input)
        self.write_form(rotty)

application = webapp2.WSGIApplication([('/', MainPage),
], debug=True)
