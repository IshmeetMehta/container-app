# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def showPinehead():
    html = "<div style='text-align:center;margin:20px;'><h1>Greetings from Another Academy!</h1><img src='https://storage.googleapis.com/la-gcp-labs-resources/essentials/Logo-Pinehead-NVY.png' width='40%' alt='Pinehead @ Google Academy'></div>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
