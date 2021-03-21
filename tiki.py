mport requests
import json

class Tiki_API:
    def __init__(self):
       self.headers = {
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0'
        }
       self.string_id = "tikivn://products/"
       self.detail_url = url = "https://tiki.vn/api/v2/products/{}?platform=web&spid={}&include=tag,images,gallery,promotions,badges,stock_item,variants,product_links,discount_tag,ranks,breadcrumbs,top_features,cta_desktop"
    def get_id(self, url):
        payload={}
        response = requests.request("GET", url, headers=self.headers, data=payload)
        html = response.text
        
        poss = html.find(self.string_id)
        for i in range(poss, poss+200):
            if(html[i] == '"'):
                pose = i
                break
        
        pdid = html[poss+len(self.string_id):pose]
        if(response.status_code == 200):
            return {'status': True, 'product_id': pdid}
        else:
            return {'status': False}
    def get_product(self, id_product):
        url = self.detail_url.format(id_product, id_product)
        payload={}
        response = requests.request("GET", url, headers=self.headers, data=payload)

        
        if(response.status_code == 200):
            data = json.loads(response.text)
            return {'status': True, 'data': data}
        else:
            return {'status': False}
