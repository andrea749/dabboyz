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
import json
from cipherinfo import ciphers
from cycle_encryption import cycle_encryptor
from cycle_encryption import cycle_decryptor
from caesarian_shift import caesar_encryptor
from caesarian_shift import caesar_decryptor
from copy import copy
from trifid import find
from trifid import slice_list
from trifid import trifid_encryptor
from trifid import trifid_decryptor




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
        ciphername = ciphers['cycle']['name']
        cipherdescription = ciphers['cycle']['description']
        variables = {
        'ciphername':ciphername,
        'cipherdescription':cipherdescription
        }
        self.response.write(template.render(variables))

    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        message2encrypt = self.request.get('message2encrypt')
        message2decrypt = self.request.get('message2decrypt')
        code_word = self.request.get('code_word')
        try:
            encrypted = self.Encryptor(message2encrypt)
        except:
            pass
        try:
            decrypted = self.Decryptor(message2decrypt)
        except:
            pass
        resp = {
          'encrypted': encrypted,
          'decrypted': decrypted
        }
        return self.response.write(json.dumps(resp))
        # template = jinja_environment.get_template('cycle.html')
        # ciphername = ciphers['cycle']['name']
        # cipherdescription = ciphers['cycle']['description']
        # decision = self.request.get('submitted')
        #
        # if not self.request.get('code_word'):
        #     code_word = 'ERROR: Please input shift parameter.'
        #     variable = {
        #     'ciphername':ciphername,
        #     'cipherdescription':cipherdescription,
        #     'code_word':code_word
        #     }
        #     self.response.write(template.render(variable))
        #
        # else:
        #     if decision == 'Encrypt':
        #         decryptedmessage = self.request.get('normal_message')
        #         encryptedmessage = self.Encryptor(decryptedmessage)
        #
        #     if decision == 'Decrypt':
        #         encryptedmessage = self.request.get('encrypted_message')
        #         decryptedmessage = self.Decryptor(encryptedmessage)
        #     code_word = self.request.get('code_word')
        #
        #     variables = {
        #     'ciphername':ciphername,
        #     'cipherdescription':cipherdescription,
        #     'encryptedmessage':encryptedmessage,
        #     'decryptedmessage':decryptedmessage,
        #     'code_word':code_word
        #     }
        #     self.response.write(template.render(variables))

    def Encryptor(self, message):
        decryptedmessage = message
        code_word = str(self.request.get('code_word'))
        answer = cycle_encryptor(decryptedmessage, code_word)
        return answer

    def Decryptor(self, message):
        encryptedmessage = message
        code_word = str(self.request.get('code_word'))
        answer = cycle_decryptor(encryptedmessage, code_word)
        return answer


class CaesarHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('cipherarticles.html')
        ciphername = ciphers['caesar']['name']
        cipherdescription = ciphers['caesar']['description']
        variables = {
        'ciphername':ciphername,
        'cipherdescription':cipherdescription
        }
        self.response.write(template.render(variables))

    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        message2encrypt = self.request.get('message2encrypt')
        message2decrypt = self.request.get('message2decrypt')
        shift = self.request.get('shift')
        try:
            encrypted = self.Encryptor(message2encrypt)
        except:
            pass
        try:
            decrypted = self.Decryptor(message2decrypt)
        except:
            pass
        resp = {
          'encrypted': encrypted,
          'decrypted': decrypted
        }
        return self.response.write(json.dumps(resp))



        # template = jinja_environment.get_template('cipherarticles.html')
        # decision = self.request.get('submitted')
        #
        # if not self.request.get('shift'):
        #     decryptedmessage = 'ERROR: Please input shift parameter.'
        #     variable = {'decryptedmessage':decryptedmessage}
        #     self.response.write(template.render(variable))
        #
        # else:
        #     if decision == 'Encrypt':
        #         decryptedmessage = self.request.get('normal_message')
        #         encryptedmessage = self.Encryptor(decryptedmessage)
        #
        #     if decision == 'Decrypt':
        #         encryptedmessage = self.request.get('encrypted_message')
        #         decryptedmessage = self.Decryptor(encryptedmessage)
        #
        #     shift = int(self.request.get('shift'))
        #     variables = {
        #     'shift':shift,
        #     'encryptedmessage':encryptedmessage,
        #     'decryptedmessage':decryptedmessage
        #     }
        #     self.response.write(template.render(variables))

    def Encryptor(self, message):
        decryptedmessage = message
        shift = int(self.request.get('shift'))
        answer = caesar_encryptor(message,shift)
        return answer

    def Decryptor(self, message):
        encryptedmessage = message
        shift = int(self.request.get('shift'))
        answer = caesar_decryptor(message,shift)
        return answer

class TrifidHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('trifid.html')
        ciphername = ciphers['trifid']['name']
        cipherdescription = ciphers['trifid']['description']
        variables = {
        'ciphername':ciphername,
        'cipherdescription':cipherdescription
        }
        self.response.write(template.render(variables))

    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        message2encrypt = self.request.get('message2encrypt')
        message2decrypt = self.request.get('message2decrypt')
        try:
            encrypted = self.Encryptor(message2encrypt)
        except:
            pass
        try:
            decrypted = self.Decryptor(message2decrypt)
        except:
            pass
        resp = {
          'encrypted': encrypted,
          'decrypted': decrypted
        }
        return self.response.write(json.dumps(resp))

        # template = jinja_environment.get_template('trifid.html')
        # decision = self.request.get('submitted')
        #
        # if decision == 'Encrypt':
        #     decryptedmessage = self.request.get('normal_message')
        #     encryptedmessage = self.Encryptor(decryptedmessage)
        #
        # if decision == 'Decrypt':
        #     encryptedmessage = self.request.get('encrypted_message')
        #     decryptedmessage = self.Decryptor(encryptedmessage)
        #
        # variables = {
        # 'encryptedmessage':encryptedmessage,
        # 'decryptedmessage':decryptedmessage
        # }
        # self.response.write(template.render(variables))

    def Encryptor(self, message):
        answer = trifid_encryptor(message)
        return answer

    def Decryptor(self,message):
        answer = trifid_decryptor(message)
        return answer


class ColumnarHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('cycle.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template('cycle.html')
        decision = self.request.get('submitted')

        if not self.request.get('code_word'):
            code_word = 'ERROR: Please input shift parameter.'
            variable = {'code_word':code_word}
            self.response.write(template.render(variable))

        else:
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
        answer = cycle_encryptor(decryptedmessage, code_word)
        return answer

    def Decryptor(self, message):
        encryptedmessage = message
        code_word = str(self.request.get('code_word'))
        answer = cycle_decryptor(encryptedmessage, code_word)
        return answer





app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/cycle', CycleHandler),
    ('/caesar', CaesarHandler),
    ('/trifid', TrifidHandler),
    ('/columnar',ColumnarHandler)
], debug=True)
