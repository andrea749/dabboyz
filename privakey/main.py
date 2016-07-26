#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging
import jinja2
import os
import math
from cycle_encryption import encryptor
from cycle_encryption import decryptor


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))



class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('Matrix.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template('homepage.html')
        self.response.write(template.render())

class CycleHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('cycle.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template('cycle.html')
        decision = self.request.get('submitted')
        if decision == 'Encrypt':
            decryptedmessage = self.request.get('normal_message')
            encryptedmessage = self.Encryptor(decryptedmessage)

        if decision == 'Decrypt':
            encryptedmessage = self.request.get('encrypted_message')
            decryptedmessage = self.Decryptor(encryptedmessage)
        code_word = self.request.get('code_word')

        variables = {
        'encryptedmessage':encryptedmessage,
        'decryptedmessage':decryptedmessage,
        'code_word':code_word
        }
        self.response.write(template.render(variables))

    def Encryptor(self, message):
        decryptedmessage = message
        code_word = str(self.request.get('code_word'))
        answer = encryptor(decryptedmessage, code_word)
        return answer

    def Decryptor(self, message):
        encryptedmessage = message
        code_word = str(self.request.get('code_word'))
        answer = decryptor(encryptedmessage, code_word)
        return answer


class CaesarHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('cipherarticles.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/cycle', CycleHandler),
    ('/caesar', CaesarHandler)
], debug=True)
