from typing import Optional, List

from fastapi import APIRouter, Header
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(prefix='/product', tags=['product', ])

product = ['watch', 'camera', 'phone']


@router.get('/all')
def get_all_products():
    data = ' '.join(product)
    return Response(content=data, media_type='text/plain')


@router.get('/header')
def with_header(response: Response, custom_header: Optional[List[str]] = Header(None)):
    response.headers['custom_response_header'] = ' and '.join(custom_header)
    return product


@router.get('/{pk}', responses={
    200: {
        'content': {
            'text/html': {
                'example': '<div>Product</div>'
            }
        },
        'description': 'Returns the HTML for an object'
    },
    404: {
        'content': {
            'text/plain': {
                'example': 'Product is not exists'
            }
        },
        'description': 'Returns 404 Error'
    }
})
def get_single_product(pk: int):
    try:
        data = product[pk]
        out = f"""
            <head>
              <style>
              .product {{
                width: 500px;
                height: 30px;
                border: 2px inset green;
                background-color: lightblue;
                text-align: center;
              }}
              </style>
            </head>
            <div class="product">{data}</div>
            """
        return HTMLResponse(content=out, media_type="text/html")
    except IndexError:
        return PlainTextResponse(content='Product is not exists', media_type='text/plain', status_code=404)
