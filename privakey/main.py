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
        template = jinja_environment.get_template('matrix.html')
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

        variables = {
        'encryptedmessage':encryptedmessage,
        'decryptedmessage':decryptedmessage
        }
        self.response.write(template.render(variables))

    def Encryptor(self, message):
        decryptedmessage = message
        cycle_size = int(self.request.get('cycle_size'))
        shifts = []
        for i in range(1, cycle_size + 1):
            shift = int(self.request.get('shift%s' % (i)))
            shifts.append(shift)
        answer = encryptor(decryptedmessage, cycle_size, shifts)
        return answer

    def Decryptor(self, message):
        encryptedmessage = message
        cycle_size = int(self.request.get('cycle_size'))
        shifts = []
        for i in range(1, cycle_size + 1):
            shift = int(self.request.get('shift%s' % (i)))
            shifts.append(shift)
        answer = decryptor(encryptedmessage, cycle_size, shifts)
        return answer



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/cycle', CycleHandler)
], debug=True)
