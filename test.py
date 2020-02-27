# -*- coding:utf-8 -*-

"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃　　　　　　　    ┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛
"""

import requests

url = 'https://secure.louisvuitton.cn/ajaxsecure/getStockLevel.jsp?'
params = {
    'storeLang': 'zhs-cn',
    'pageType': 'storelocator_section',
    'skuIdList': 'M40712',
    'null': '',
    '_': '1582700363885',

}
header = {
    'Cookie': 'lvbmwe2=F290699193FC6CF5DA9E8F7C4B76132D; lvbmwe1=F6172D768C9641EF1878D5547ABE2C65; ak_bmsc=4E284B624926327599A2217F99D9A2B6DE8A06B59A4F0000C311565EA7520B1D~plU6VL2P+wl40FooiDLU9PWN28Ka+0SA/sAmJch4v5jivVMoJUlMusTuWDuOQHryBZcFBIHr5GtM1Glyt+uSyK4o6zcu9okF+69RMuXDm0vQljdhuptsbdSXUoGswBX+QBw4Aaaupd1U5AbYhn4K6pZuxZc++2kfKfk9SXIer9KeqgXdS4czElMX6ErWg9+i24SfQq2b0RiTs+2FLpVb3ijjSSsuv2oyHKYOIy0u0YxdMcKEDQxhAh3F6GFhHR1Nnx; bm_sz=6601EC27A721A39C31A828C4B3DC0FAA~YAAQtQaK3r1pd2JwAQAAEGU1gAYHFA8AIS4H7VTGZ4oJC3IJLDY3fK2khyJFItM2g9W3gojZXOrtKlCyXWU5iYeqe4Sck9EtYOaI8DGsw+FjUe30GTkNLIE3MIHHx+oA577RFoLNAiJxBPrQUUdnLVB4IyhYibiufwJsifeGHovN14dQG3CAaI9rfy5sntGEmYCXbgY=; _abck=2D14FCC456CA248CEA8966E281779CD4~0~YAAQlQaK3mESjWJwAQAAFxFLgAMWcJJi9YK9NsYtLE4Y9QqegTMJhV7pKKzRLa/THtUFegla+R7qPZSEPSbNYy1HUuiRg5GZlcJ5r9kGdj94+SJDvL99DluMBorXozBvm1bOHKxWVNaC+t0RyT6XybD7NzF6mVJjzSvNPjvieQnis8KZukmTTcs2EzMCJZorrnCmvLZXeISPvR967WkfaXvDprNHtzfb0f87XfiPYnU2iOD7gxe5+CJb4a6uH8U685QU0JYRjn3KnWgFra7VsvDXA6fs6mirPR57PrhON1LTTaFfXMbtocOHQsQKjXBeup+cpK6oKzmDqEPi~-1~-1~-1; qb_permanent=q8eltsc1e34-0k72y37kj-jaaa50x:14:14:1:1:0::0:1:0:BeVhHF:BeVhdN:::::119.113.121.69:dalian:14403:china:CN:38.9214:121.582:dalian:156038:liaoning%20sheng:35605:migrated|1582699084633:EYai==J=CCFu=Ow::XCASzHt:XCANWpf:0:0:0::0:0:.louisvuitton.cn:0; _qubitTracker=q8eltsc1e34-0k72y37kj-jaaa50x; bm_sv=B462E38AE9C80A110C19FB382E9243EC~DDTFaCtPsAyzR6yYH6Qklg7+rU6tttDK9h0kTYlenj3DpCXnBy9AYmT7f1VzbJs5dZ9mhprag6WJi9x++YLXz1GBXbXrok0tdaBLrb59oR4w3/BQ2V3ytV5FNIgLV0rA9ZynCYWH2d20ATsI7qiHHBx50c5Jg895mTjpNbOrGew=; OPTOUTMULTI=0:0%7Cc1:0%7Cc2:0%7Cc4:0%7Cc3:0; utag_main=v_id:0170803564df000e467b739c51620104e005000d00bd0$_sn:1$_se:42$_ss:0$_st:1582702176604$ses_id:1582698947809%3Bexp-session$_pn:14%3Bexp-session$dc_visit:1$dc_event:42%3Bexp-session$dc_region:eu-central-1%3Bexp-session; qb_generic=:XCANWMS:.louisvuitton.cn; lvbmwe2=1F0E1419DEC3D0AA1A38F41172A2C577; lvbmwe1=F6172D768C9641EF1878D5547ABE2C65; AMCV_A69F5C6655799DC57F000101%40AdobeOrg=-2017484664%7CMCMID%7C04893889638958755451437758383743163766%7CMCAID%7CNONE%7CMCAAMLH-1583303753%7C11%7CMCAAMB-1583303753%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y; Hm_lvt_70ef235947285936a07191ef669a6813=1582698949; Hm_lpvt_70ef235947285936a07191ef669a6813=1582700366; _gcl_au=1.1.1513752089.1582698949; Qs_lvt_187854=1582698949; Qs_pv_187854=4557246266446369300%2C2092823954038822700%2C1632911861843064600%2C3156371883119911000%2C1050804741792437600; kameleoonVisitorCode=_js_89z69qhrymnumelv; _ga=GA1.2.1380800014.1582698953; _gid=GA1.2.1460244036.1582698953; s_cc=true; s_sq=%5B%5BB%5D%5D; JSESSIONID=CS4rcVXaFFA36wtbqInKh9HD.front11-prc; ATG_SESSION_ID=CS4rcVXaFFA36wtbqInKh9HD.front11-prc; anonymous_session=true',
    # 'Host': 'secure.louisvuitton.cn',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Cache-Control': 'Cache-Control',
    # 'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
}
r = requests.get(url,params=params, headers=header)
print(r.json())
