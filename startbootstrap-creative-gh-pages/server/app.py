import csv
import json
import tempfile

import falcon

app = application = falcon.App()

class PersonDetails:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir

    def on_get(self, req, resp):
        with open('server/static/form.html') as f:
            resp.content_type = falcon.MEDIA_HTML
            resp.text = f.read()

    def on_post(self, req, resp):
        with tempfile.NamedTemporaryFile(dir=self.data_dir, delete=False,
                                         mode='w', suffix='.json') as fp:
            json.dump(req.media, fp)
        raise falcon.HTTPFound("https://www.onlinesbi.com/sbicollect/icollecthome.htm?corpID=4750977")

app.add_route('/details', PersonDetails())
