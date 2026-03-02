from odoo import models, fields, api
import requests
from bs4 import BeautifulSoup
import json

class logmodel(models.Model):
    _inherit = 'log_log'
    
    def show_email_template(self):
        # self.ensure_one()
        template_id = self.env.ref('user_management.email_template_shakib').id
       
        return {
        'type': 'ir.actions.act_window',
        'res_model': 'mail.template',
        'view_mode': 'form',
        'res_id': template_id,   # This opens existing template
        'target': 'current',
    }
class GoogleSearchResult(models.Model):
    _name = 'google_search_result'
    _description = 'Google Search Result'
    
    keyword = fields.Char(string="Keyword", required=True)
    title = fields.Char(string='Title')
    link = fields.Char(string='URL')
    snippet = fields.Text(string='Snippet')
    position = fields.Integer(string='Position') 
    
      
    def google_search(self):
        url = "https://api.serphouse.com/serp/live"
        payload = {
            "data":{
                    "q": self.keyword,
                    "domain": "google.com",
                    "loc": "Dhaka,Dhaka Division,Bangladesh",
                    "lang": "en",
                    "device": "desktop",
                    "serp_type": "web",
                    "page": "1",
                    "verbatim": "0"
        }
        }
        headers = {
            'accept': "application/json",
            'content-type': "application/json",
            'authorization': "Bearer tGtCrM0hK1uD0hYf6CWDs8xdn1xehPCL4vl7izKF8kvISNtnk1VNE1Mg52N3"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        

        data = response.json()
        print(json.dumps(data, indent=4))
        # self.env['google_search_result'].search([]).unlink()
        results = data.get('results', {}).get('results', {}).get('organic', [])
        print(results)
        for item in results:
            # self.create({
            #     'title': item.get('title', ''),
            #     'link': item.get('url', ''),
            #     'snippet': item.get('snippet', ''),
            #     'position': item.get('pos', 0),
            # })
            self.env['google_search_result'].create({
                # 'search_bar_id': self.id,   # <-- link to this search
                'keyword':  self.keyword,
                'position': item.get('pos', 0),
                'title':    item.get('title', ''),
                'link':     item.get('url', ''),
                'snippet':  item.get('snippet', ''),
            })

        # 3. Return action to show results in UI
        return {
            'type': 'ir.actions.act_window',
            'name': 'Search Results',
            'res_model': 'google_search_result',
            'view_mode': 'list',
            'target': 'current',
        }
        # print(json.dumps(data, indent=4))
        # print(response.text)
        # for r in response.text:
        #     print(r)