from typing import List, Optional
from fastapi import APIRouter, Cookie, Depends, Form, Response, status, Header
from fastapi.responses import HTMLResponse, PlainTextResponse
from custom_log import log
import time

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch', 'camera', 'phone']

async def time_consuming_functionality():
    time.sleep(5)
    return 'ok'

@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)

    return products

@router.get('/all')
async def get_all_products():
    await time_consuming_functionality()

    #return products
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")

    log(
        tag="MyAPI",
        message="Call to get all products"
    )

    return response

@router.get('/withheader')
def get_products(
    response: Response,
    # custom_header: Optional[str] = Header(None)
    custom_header: List[str]= Header(None),
    test_cookie: Optional[str] = Cookie(None)
):
    if custom_header:
        response.headers['custom_response_header'] = ", ".join(custom_header)

    return {
        'data': products,
        'custom_header': custom_header,
        'my_cookie': test_cookie
    }

@router.get('/{id}', responses= {
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
            }
        },
        "description": "Returns the HTML for an object"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "Product not available"
            }
        },
        "description": "A cleatext error message"
    },
})
def get_product(id: int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=out,
            media_type="text/plain"
        )
    else:
        product = products[id]
        out = f"""
            <head>
                <style>
                    .product {{
                        width: 500px;
                        height: 30px;
                        boarder: 2px inset green;
                        background-color: lightblue;
                        tyext-align: center;
                    }}
                </style>
            </head>
            <div class="product"> {product} </div>
        """

        return HTMLResponse(content=out, media_type="text/html")