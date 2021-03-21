# tiki-api
TIKI.VN API (Unofficial)

# Example
## Get ID Product from link
```
tiki = Tiki_API()
product = tiki.get_id("https://tiki.vn/ta-lot-ve-sinh-cho-meo-co-mui-huong-sumiho-cong-nghe-y-p31884922.html")
```
Response
```
{'status': True, 'product_id' 31884922}
```
## Get product details
```
tiki = Tiki_API()
product = tiki.get_id("https://tiki.vn/ta-lot-ve-sinh-cho-meo-co-mui-huong-sumiho-cong-nghe-y-p31884922.html")
product_details = tiki.get_product(product['product_id'])
```
Response
```
{
   "status":true,
   "data":{
      "id":31884922,
      "master_id":31884922,
      "sku":"8279397163427",
      "name":"Tã lót cho chó mèo thú cưng (có mùi hương) Sumiho công nghệ Ý (nhiều Size) Phụ kiện cho chó mèo",
      "url_key":"ta-lot-ve-sinh-cho-meo-co-mui-huong-sumiho-cong-nghe-y-p31884922",
      "url_path":"ta-lot-ve-sinh-cho-meo-co-mui-huong-sumiho-cong-nghe-y-p31884922.html?spid=42265930",
      "type":"configurable",
      "book_cover":"None",
      "short_description":"TÃ LÓT CHO CHÓ MÈO THÚ CƯNG SUMIHO\nTã lót cho chó mèo thú cưng Sumiho công nghệ Ý là sản phẩm duy nhất tại Việt Nam có mùi hương (trà xanh, phấn trẻ em, oải hương) giúp kháng khuẩn, khử mùi hôi tối...",
      "price":209000,
      "list_price":268000,
      "badges":[
         {
            "code":"tikinow",
            "text":"tikinow"
         }
      ],
      "discount":59000,
      "discount_rate":22,
      "rating_average":4.9,
      "review_count":128,
      "order_count":0,
      "favourite_count":0,
      "thumbnail_url":"https://salt.tikicdn.com/cache/280x280/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg",
      "has_ebook":false,
      "inventory_status":"available",
      "productset_group_name":"Bách Hóa Online/Chăm sóc thú cưng/Dành cho chó/Đồ dùng vệ sinh cho chó",
      "is_fresh":false,
      "seller":"None",
      "is_flower":false,
      "is_gift_card":false,
      "inventory":{
         "product_virtual_type":"None",
         "fulfillment_type":"tiki_delivery"
      },
      "url_attendant_input_form":"",
      "salable_type":"",
      "data_version":11,
      "day_ago_created":556,
      "categories":{
         "id":2,
         "name":"Root",
         "is_leaf":false
      },
      "meta_title":"None",
      "meta_description":"None",
      "meta_keywords":"None",
      "liked":false,
      "rating_summary":[
         
      ],
      "description":"<span class=\\'description-separate\\'></span>Tã lót vệ sinh chó mèo<br />\n6 lớp thấm hút vượt trội<br />\nKhử mùi, kháng khuẩn khi cún đi vệ sinh với mùi hương thơm mát (Phấn, Oải Hương, Trà Xanh)<br />\nThích hợp để sử dụng trong nhà, khi đi du lịch<br />\nTã lót an toàn không gây hại đến sức khỏe của thú cưng<p><span style=\"color: #ff0000;\"><em><strong><span style=\"text-align: left; text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Verdana,Arial,Helvetica,sans-serif; font-size: 14px; font-variant: normal; text-decoration: none; word-spacing: 0px; display: inline !important; white-space: normal; cursor: text; orphans: 2; float: none; -webkit-text-stroke-width: 0px; background-color: #ffffff;\">TÃ LÓT CHO CHÓ MÈO THÚ CƯNG SUMIHO</span></strong></em></span></p>\n<p>Tã lót cho chó mèo thú cưng Sumiho công nghệ Ý là sản phẩm duy nhất tại Việt Nam có mùi hương (trà xanh, phấn trẻ em, oải hương) giúp kháng khuẩn, khử mùi hôi tối đa khi thú cưng đi vệ sinh. <br />Ngoài ra, khác xa với hầu hết các sản phẩm khác trên thị trường, Tã lót Sumiho có đến 6 lớp thấm hút vượt trội, chứa đến <span style=\"color: #ff0000;\"><strong>700ml chất lỏng</strong></span>. Khi cún đi vệ sinh, chất lỏng hoàn toàn được chuyển hóa thành chất gel nhờ lớp chuyển hóa thần kỳ, khiến cho mặt tã luôn khô ráo, sàn nhà luôn sạch sẽ.<br />Thông số kỹ thuật: <br />- Màu sắc: Hồng<br />- Chất liệu: vải không dệt + giấy thấm hút<br />- Kích thước: <br /><span style=\"color: #ff0000;\"><strong>Size S (100 cái)</strong></span>: 33cm x 45c: mùi phấn trẻ em<br /><span style=\"color: #ff0000;\"><strong>Size M (50 cái)</strong></span>: 45cm x 60cm: mùi trà xanh thơm mát<br /><span style=\"color: #ff0000;\"><strong>Size L (30 cái):</strong></span> 60cm x 60cm: mùi trà xanh thơm mát<br /><span style=\"color: #ff0000;\"><strong>Size XL (30 cái):</strong></span> 60cm x 90cm: mùi hoa oải hương</p>\n<p><iframe src=\"//www.youtube.com/embed/_nHgK1zh3Pk\" width=\"560\" height=\"314\" allowfullscreen=\"allowfullscreen\"></iframe></p>\n<p>Ngoài ra, bạn có thể huấn luyện thú cưng của bạn đi vệ sinh đúng chỗ với phương pháp như sau:<br />+ Đặt miếng lót lên khay vệ sinh.<br />+ Hướng dẫn cún đi vào khay (khi cún mắc tè, để ngay cún lên tấm tã lót)<br />+ Tập lại cho cún đi đúng vào khay vào các lần sau<br />+ Khen cún khi cún đi vệ sinh đúng chỗ (kết hợp bánh thưởng, xương gặm, xúc xích v.v.)<br />Tã lót cho chó mèo thú cưng có thể sử dụng được trên sàn, lồng thú cưng, túi thú cưng , nhà vệ sinh, phòng tắm v.v<br />Sản xuất: N<span style=\"background-color: #ffffff;\">ă</span>m 2020<br />Shop xin cam kết đổi trả 100% (miễn phí vận chuyển) nếu quý khách nhận được sản phẩm kém chất lượng.</p>\n<p>#ta #bim #talot #thamlot #cho #meo #chomeo #cuncung #thucung #cun #lot #chuong #lotchuong #nem #phukienchomeo #phukienchocun #sumiho #hut #vesinh #khangkhuan</p>\n<p><img src=\"https://i.imgur.com/SRnf22S.jpg\" alt=\"Ta-lot-cho-meo\" width=\"750\" height=\"421\" /></p>\n<p><img src=\"https://i.imgur.com/gOjlIOZ.jpg\" alt=\"Ta-lot-cho-meo\" width=\"750\" height=\"421\" /></p>\n<p><img src=\"https://i.imgur.com/agmfS5Z.jpg\" alt=\"Ta-lot-cho-meo\" width=\"750\" height=\"421\" /></p><p>Giá sản phẩm trên Tiki đã bao gồm thuế theo luật hiện hành. Tuy nhiên tuỳ vào từng loại sản phẩm hoặc phương thức, địa chỉ giao hàng mà có thể phát sinh thêm chi phí khác như phí vận chuyển, phụ phí hàng cồng kềnh, ...</p>",
      "images":[
         {
            "label":"None",
            "position":"None",
            "base_url":"https://salt.tikicdn.com/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg",
            "thumbnail_url":"https://salt.tikicdn.com/cache/200x280/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg",
            "small_url":"https://salt.tikicdn.com/cache/w42/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg",
            "medium_url":"https://salt.tikicdn.com/cache/w300/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg",
            "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg",
            "is_gallery":true
         },
         {
            "label":"None",
            "position":"None",
            "base_url":"https://salt.tikicdn.com/ts/product/b3/d5/58/7d430d9cb3f04a111c05e32da04e311a.jpg",
            "thumbnail_url":"https://salt.tikicdn.com/cache/200x280/ts/product/b3/d5/58/7d430d9cb3f04a111c05e32da04e311a.jpg",
            "small_url":"https://salt.tikicdn.com/cache/w42/ts/product/b3/d5/58/7d430d9cb3f04a111c05e32da04e311a.jpg",
            "medium_url":"https://salt.tikicdn.com/cache/w300/ts/product/b3/d5/58/7d430d9cb3f04a111c05e32da04e311a.jpg",
            "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/b3/d5/58/7d430d9cb3f04a111c05e32da04e311a.jpg",
            "is_gallery":true
         },
         {
            "label":"None",
            "position":"None",
            "base_url":"https://salt.tikicdn.com/ts/product/94/e7/de/09065b6a62ca9f3f358ccee6d273ad4b.jpg",
            "thumbnail_url":"https://salt.tikicdn.com/cache/200x280/ts/product/94/e7/de/09065b6a62ca9f3f358ccee6d273ad4b.jpg",
            "small_url":"https://salt.tikicdn.com/cache/w42/ts/product/94/e7/de/09065b6a62ca9f3f358ccee6d273ad4b.jpg",
            "medium_url":"https://salt.tikicdn.com/cache/w300/ts/product/94/e7/de/09065b6a62ca9f3f358ccee6d273ad4b.jpg",
            "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/94/e7/de/09065b6a62ca9f3f358ccee6d273ad4b.jpg",
            "is_gallery":true
         }
      ],
      "ranks":[
         {
            "type":"month",
            "period":"2021-02-21",
            "rank":"1",
            "category_id":"8402",
            "url":"/bestsellers-month/do-dung-ve-sinh-cho-cho/c8402",
            "name":"Đồ dùng vệ sinh cho chó"
         }
      ],
      "warranty_policy":"None",
      "custom_attributes":[
         {
            "attribute":"hotline",
            "display_name":"HOTLINE: 1900 6035",
            "value":"(1.000đ/phút, 8-21h cả T7, CN)"
         }
      ],
      "brand":{
         "id":111461,
         "name":"OEM",
         "slug":"oem"
      },
      "seller_specifications":[
         {
            "name":"Tiki hoàn tiền 111% nếu phát hiện hàng giả",
            "value":"None",
            "url":"None"
         },
         {
            "name":"Cam kết hàng chính hiệu",
            "value":"None",
            "url":"None"
         }
      ],
      "current_seller":{
         "id":92900,
         "sku":"2191802082719",
         "store_id":86230,
         "name":"Sumiho Pet Boutique",
         "slug":"sumiho-pet-boutique",
         "link":"https://tiki.vn/cua-hang/sumiho-pet-boutique",
         "is_best_store":false,
         "logo":"https://vcdn.tikicdn.com/ts/seller/bf/ac/5c/98ab09c0fcde32cbc883ca486f5af838.png",
         "product_id":"42265930",
         "price":209000,
         "is_offline_installment_supported":"None"
      },
      "other_sellers":[
         
      ],
      "specifications":[
         {
            "name":"Content",
            "attributes":[
               {
                  "name":"Thương hiệu",
                  "value":"OEM"
               },
               {
                  "name":"Chất liệu",
                  "value":"Vải không dệt, giấy thấm hút chuyển hóa chất lỏng thành gel"
               },
               {
                  "name":"Hướng dẫn bảo quản",
                  "value":"Để nơi khô ráo, tránh ánh nắng mặt trời"
               },
               {
                  "name":"Hướng dẫn sử dụng",
                  "value":"Xem chi tiết mô tả sản phẩm"
               }
            ]
         },
         {
            "name":"Operation",
            "attributes":[
               {
                  "name":"Quy cách đóng gói",
                  "value":"30 cái/Túi"
               }
            ]
         },
         {
            "name":"System",
            "attributes":[
               {
                  "name":"SKU",
                  "value":2191802082719
               }
            ]
         }
      ],
      "product_links":[
         
      ],
      "configurable_options":[
         {
            "code":"option1",
            "name":"Kích cỡ",
            "position":0,
            "values":[
               {
                  "label":"Size L: 60cm x 60cm (30 cái)"
               },
               {
                  "label":"Size M: 45cm x 60cm (50 cái)"
               },
               {
                  "label":"Size S: 33cm x 45cm (100 cái)"
               },
               {
                  "label":"Size XL: 60cm x 90cm (30 cái)"
               }
            ]
         }
      ],
      "configurable_products":[
         {
            "child_id":31884932,
            "sku":"7989608803967",
            "name":"Tã lót vệ sinh chó mèo (có mùi hương) Sumiho công nghệ Ý - Size S: 33cm x 45cm (100 cái)",
            "price":229000,
            "thumbnail_url":"https://salt.tikicdn.com/cache/280x280/ts/product/23/81/cd/cdb604e2b56b99bc3a00c9d344cbadba.jpg",
            "images":[
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/23/81/cd/cdb604e2b56b99bc3a00c9d344cbadba.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/23/81/cd/cdb604e2b56b99bc3a00c9d344cbadba.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/23/81/cd/cdb604e2b56b99bc3a00c9d344cbadba.jpg"
               },
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/cf/bf/59/b4b1ad0440420ad0355d0cf6a3593a7d.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/cf/bf/59/b4b1ad0440420ad0355d0cf6a3593a7d.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/cf/bf/59/b4b1ad0440420ad0355d0cf6a3593a7d.jpg"
               },
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/9a/27/6b/c64a3adcd68743f868db837813b9d5f0.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/9a/27/6b/c64a3adcd68743f868db837813b9d5f0.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/9a/27/6b/c64a3adcd68743f868db837813b9d5f0.jpg"
               }
            ],
            "selected":false,
            "inventory_status":"available",
            "id":42263113,
            "option1":"Size S: 33cm x 45cm (100 cái)"
         },
         {
            "child_id":31884956,
            "sku":"9969124683135",
            "name":"Tã lót vệ sinh chó mèo (có mùi hương) Sumiho công nghệ Ý - Size L: 60cm x 60cm (30 cái)",
            "price":209000,
            "thumbnail_url":"https://salt.tikicdn.com/cache/280x280/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg",
            "images":[
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/c3/62/bb/c81b5ef44f1ffedd83858bb0a7543fcf.jpg"
               },
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/b3/d5/58/7d430d9cb3f04a111c05e32da04e311a.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/b3/d5/58/7d430d9cb3f04a111c05e32da04e311a.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/b3/d5/58/7d430d9cb3f04a111c05e32da04e311a.jpg"
               },
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/94/e7/de/09065b6a62ca9f3f358ccee6d273ad4b.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/94/e7/de/09065b6a62ca9f3f358ccee6d273ad4b.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/94/e7/de/09065b6a62ca9f3f358ccee6d273ad4b.jpg"
               }
            ],
            "selected":true,
            "inventory_status":"available",
            "id":42265930,
            "option1":"Size L: 60cm x 60cm (30 cái)"
         },
         {
            "child_id":31884944,
            "sku":"2870059051661",
            "name":"Tã lót vệ sinh chó mèo (có mùi hương) Sumiho công nghệ Ý - Size M: 45cm x 60cm (50 cái)",
            "price":219000,
            "thumbnail_url":"https://salt.tikicdn.com/cache/280x280/ts/product/67/bc/6e/e195745c9ba5d826b47e51b06f90913c.jpg",
            "images":[
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/67/bc/6e/e195745c9ba5d826b47e51b06f90913c.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/67/bc/6e/e195745c9ba5d826b47e51b06f90913c.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/67/bc/6e/e195745c9ba5d826b47e51b06f90913c.jpg"
               },
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/4d/c7/23/ba806e2fd7660dd9bf3777d183df3531.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/4d/c7/23/ba806e2fd7660dd9bf3777d183df3531.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/4d/c7/23/ba806e2fd7660dd9bf3777d183df3531.jpg"
               },
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/7b/da/95/caa53f430b87daacb081e72043387721.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/7b/da/95/caa53f430b87daacb081e72043387721.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/7b/da/95/caa53f430b87daacb081e72043387721.jpg"
               }
            ],
            "selected":false,
            "inventory_status":"available",
            "id":42265781,
            "option1":"Size M: 45cm x 60cm (50 cái)"
         },
         {
            "child_id":31884965,
            "sku":"9667676399855",
            "name":"Tã lót vệ sinh chó mèo (có mùi hương) Sumiho công nghệ Ý - Size XL: 60cm x 90cm (30 cái)",
            "price":229000,
            "thumbnail_url":"https://salt.tikicdn.com/cache/280x280/ts/product/fb/90/42/7d5e0f76021dd006aa0943df6cde4572.jpg",
            "images":[
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/fb/90/42/7d5e0f76021dd006aa0943df6cde4572.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/fb/90/42/7d5e0f76021dd006aa0943df6cde4572.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/fb/90/42/7d5e0f76021dd006aa0943df6cde4572.jpg"
               },
               {
                  "large_url":"https://salt.tikicdn.com/cache/w1200/ts/product/17/4e/9f/a76a944a85f4377a2aae6d768fa33f53.jpg",
                  "medium_url":"https://salt.tikicdn.com/cache/550x550/ts/product/17/4e/9f/a76a944a85f4377a2aae6d768fa33f53.jpg",
                  "small_url":"https://salt.tikicdn.com/cache/75x75/ts/product/17/4e/9f/a76a944a85f4377a2aae6d768fa33f53.jpg"
               }
            ],
            "selected":false,
            "inventory_status":"available",
            "id":42271910,
            "option1":"Size XL: 60cm x 90cm (30 cái)"
         }
      ],
      "services_and_promotions":[
         
      ],
      "promotions":[
         
      ],
      "stock_item":{
         "qty":797497,
         "min_sale_qty":1,
         "max_sale_qty":100,
         "preorder_date":false
      },
      "breadcrumbs":[
         {
            "url":"/bach-hoa-online/c4384",
            "name":"Bách Hóa Online",
            "category_id":4384
         },
         {
            "url":"/thu-cung/c5451",
            "name":"Chăm sóc thú cưng",
            "category_id":5451
         },
         {
            "url":"/danh-cho-cho/c5452",
            "name":"Dành cho chó",
            "category_id":5452
         },
         {
            "url":"/do-dung-ve-sinh-cho-cho/c8402",
            "name":"Đồ dùng vệ sinh cho chó",
            "category_id":8402
         },
         {
            "name":"Tã lót cho chó mèo thú cưng (có mùi hương) Sumiho công nghệ Ý (nhiều Size) Phụ kiện cho chó mèo",
            "url":"https://tiki.vn/ta-lot-ve-sinh-cho-meo-co-mui-huong-sumiho-cong-nghe-y-p31884922.html"
         }
      ],
      "installment_info":"None",
      "video_url":"",
      "youtube":"",
      "is_seller_in_chat_whitelist":true
   }
}

```
