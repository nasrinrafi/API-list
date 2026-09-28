from playwright.sync_api import APIRequestContext
import pytest


def test_get_all_products(api_request_context: APIRequestContext):
    """تست ۱: گرفتن لیست تمام محصولات از طریق API"""
    response = api_request_context.get("/api/productsList")

    # بررسی اینکه سرور پاسخ موفق (Status 200) داده است
    assert response.status == 200

    data = response.json()
    # بررسی اینکه پاسخ شامل لیست محصولات است
    assert len(data["products"]) > 0
    print(f"\nTotal products found via API: {len(data['products'])}")


def test_post_to_all_products_list(api_request_context: APIRequestContext):
    """تست ۲: تست منفی - ارسال درخواست POST به سروری که فقط متد GET قبول می‌کند"""
    response = api_request_context.post("https://automationexercise.com/api/productsList")

    assert response.status == 200
    data = response.json()
    # سایت در این حالت یک پیام خطا با پاسخ مناسب برمی‌گرداند
    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."


def test_verify_login_with_valid_details(api_request_context: APIRequestContext):
    """تست ۳: تست API ورود کاربر با اطلاعات معتبر"""
    response = api_request_context.post(
        "/api/verifyLogin",
        data={
            "email": "testqa2026@gmail.com",
            "password": "SecurePass123!"
        }
    )

    assert response.status == 200
    data = response.json()
    # بسته به اینکه این ایمیل از قبل در سایت ثبت‌نام شده باشد یا نه، پاسخ تغییر می‌کند
    print(f"\nLogin API Response Code: {data.get('responseCode')}")
    print(f"Message: {data.get('message')}")


def test_search_product(api_request_context: APIRequestContext):
    """تست جستجوی محصول از طریق API"""
    response = api_request_context.post(
        "https://automationexercise.com/api/searchProduct",
        form={"search_product": "Tshirt"}  # جستجوی کلمه کلیدی
    )

    assert response.status == 200
    data = response.json()
    assert data.get("responseCode") == 200
    products = data.get("products", [])
    print(f"\nFound {len(products)} products.")


def test_get_user_detail_by_email(api_request_context: APIRequestContext):
    email_address = "nasrinrafi2000@gmail.com"
    response = api_request_context.get(
        "https://automationexercise.com/api/getUserDetailByEmail",
        params={"email": email_address}
    )

    assert response.status == 200
    data = response.json()
    print(f"\nResponse Code: {data.get('responseCode')}")
    assert data.get("responseCode") in [200, 404]


def test_update_userAccount(api_request_context: APIRequestContext):
    response = api_request_context.put("https://automationexercise.com/api/updateAccount",
                                       data={
                                           "name": "nasrin",
                                           "email": "nasrinrafi2000@gmail.com",
                                           "password": "newpassword",
                                           "first_name": "nasrin",
                                           "lastname": "rafi",
                                           "company": "google"
                                       })
    assert response.status == 200
    response_jason = response.json()
    assert response_jason["responseCode"] in [200, 400]


#  assert response_jason["messege"]=="user updated"
# print("user account update succefully via API")

def test_get_all_products_list(api_request_context: APIRequestContext):
    response = api_request_context.get("https://automationexercise.com/api/productsList")
    assert response.status == 200
    data = response.json()
    assert data.get("responseCode") == 200
    products = data.get("products", [])
    print(f"\nTotal users found :{len(products)}")
    for product in products:
        product_id = product.get("id")  # استفاده از رشته "id"
        name = product.get("name")
        price = product.get("price")  # به جای ایمیل، قیمت محصول را داریم
        print(f"ID: {product_id} | Name: {name} | Price: {price}")
        # اطمینان از اینکه لیست کاربران خالی نیست
    assert len(products) > 0



@pytest.mark.parametrize(
        "email,password,expected_code,expected_message", [
            ("wrong_user@fake.com", "wrong_password", 404, "User not found!"),
            ("", "password", 404,"User not found!"),
            ("invalid format", "1343", 404, "User not found!"),
        ]
    )

def test_invalid_login_parametize(api_request_context: APIRequestContext, email, password, expected_code,
                                  expected_message):
    response = api_request_context.post("https://automationexercise.com/api/verifyLogin",
                                        form={
                                            "email": email,
                                            "password": password
                                        }
                                        )
    assert response.status == 200
    data = response.json()
    assert data["responseCode"] == expected_code
    assert data["message"] == expected_message


def create_user(api_request_context: APIRequestContext):
    Params = {"name": "nasrin",
              " last_name": "rafi",
              "email": "nasrinrafi@gamil.com",
              "company": "google",
              "salary": "140k",
              "address": "20488 stevence creeck blvd",
              "city": "cupertino",
              "mobile_number": "146786986"

              }
    response = api_request_context.post("https://automationexercise.com/api/createAccount", form=Params)

    assert response.status == 200
    data = response.json()

    assert data["responseCode"] == 201
    assert data["message"] == "user created"


def get_all_brand_list(api_request_context: APIRequestContext):
    response = api_request_context.get("https://automationexercise.com/api/brandsList")
    assert response.status == 200
    data = response.json()
    brand_list = data.get("brands", [])
    assert len(brand_list) > 0
    for i in brand_list:
        brand_name = i.get("brand")
        print(f"Brand_name: {brand_name}")
