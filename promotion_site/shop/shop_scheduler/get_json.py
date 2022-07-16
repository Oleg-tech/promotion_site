import requests
import json

url = "https://api.catalog.ecom.silpo.ua/api/2.0/exec/EcomCatalogGlobal"

headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}

categoryId = 22

data = """
{
    "method":"GetSimpleCatalogItems",
    "data":{"merchantId":1,
            "basketGuid":"",
            "deliveryType":2,
            "filialId":2043,
            "From":1,
            "businessId":1,
            "To":1000,
            "ingredients":false,
            "categoryId":22,
            "sortBy":"popular-asc",
            "RangeFilters":{},
            "MultiFilters":{},
            "UniversalFilters":[],
            "CategoryFilter":[],
            "Promos":["additional",
                      "cina-tyzhnya",
                      "akciyi-vlasnogo-importu",
                      "melkoopt"]
                            
            }   
}
"""


def get_file():
    response = requests.post(url, data=data, headers=headers)
    print(response)
    with open('shop/static/json/data.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
