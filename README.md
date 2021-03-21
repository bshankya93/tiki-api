# tiki-api
TIKI.VN API (Unofficial)

#Example
##Get ID Product from link
```
tiki = Tiki_API()
product = tiki.get_id("https://tiki.vn/ta-lot-ve-sinh-cho-meo-co-mui-huong-sumiho-cong-nghe-y-p31884922.html")
```
Response
```
{'status': True, 'product_id' 31884922}
```
##Get product details
```
tiki = Tiki_API()
product = tiki.get_id("https://tiki.vn/ta-lot-ve-sinh-cho-meo-co-mui-huong-sumiho-cong-nghe-y-p31884922.html")
product_details = tiki.get_product(product['product_id'])
```
Response
```
{
   "status":true,
   "data":[
      {
         "id":31884922,
         "sku":"8279397163427",
         "name":"Tã lót cho chó mèo thú cưng (có mùi hương) Sumiho công nghệ Ý (nhiều Size) Phụ kiện cho chó mèo",
         "url_key":"ta-lot-ve-sinh-cho-meo-co-mui-huong-sumiho-cong-nghe-y-p31884922",
         "url_path":"ta-lot-ve-sinh-cho-meo-co-mui-huong-sumiho-cong-nghe-y-p31884922.html",
         "type":"configurable",
         "short_description":"",
         "price":209000,
         "list_price":268000,
         "price_usd":0.0,
         "discount":59000,
         "discount_rate":22,
         "rating_average":5.0,
         "brand":{
            "exclusive_seller_id":0,
            "id":111461,
            "is_document_required":0,
            "listdata_id":111461,
            "status":1,
            "thumbnail":"brands/Brands-2776.jpg",
            "url_key":"thuong-hieu/oem.html",
            "value":"OEM"
         },
         "review_count":141,
         "favourite_count":0,
         "thumbnail_url":"https://salt.tikicdn.com/cache/280x280/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg",
         "has_ebook":false,
         "inventory_status":"available",
         "productset_group_name":"Bách Hóa Online/Chăm sóc thú cưng/Dành cho chó/Đồ dùng vệ sinh cho chó",
         "salable_type":"",
         "thumbnail_width":280,
         "thumbnail_height":280,
         "seller_product_id":42265930,
         "sp_seller_id":92900,
         "master_id":0,
         "sp_seller_name":"Sumiho Pet Boutique",
         "badges":[
            {
               "code":"zorba"
            }
         ],
         "is_visible":true,
         "is_fresh":false,
         "is_flower":false,
         "is_gift_card":false
      }
   ]
}

```
