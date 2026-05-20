import pytest
from playwright.sync_api import Page, expect
from pages.post_ad_page import PostAdPage


# ── 5 CAR ADS DATA ────────────────────────────────────────────────────────────
car_ads = [
    {
        "title": "Toyota Corolla GLI 2020",
        "brand": "Toyota",
        "model": "Corolla",
        "version": "GLi",
        "engine": "1.6 TDI",
        "year": "2020",
        "condition": "Fair",
        "fuel": "Petrol",
        "transmission": "Manual",
        "color": "White",
        "mileage": "45000",
        "price": "1800001",
        "wilaya": "16",
        "commune": "Alger Centre",
        "description": "Well maintained Toyota Corolla, single owner, no accidents.",
        "image": "/Users/apple1/Downloads/toyota.png"
    },
    {
        "title": "Honda Civic Sport 2021",
        "brand": "Other",
        "brand_name":"Renault",      
        "model": "Civic",
        "version": "Sport",
        "engine": "1.5 VTEC",
        "year": "2021",
        "condition": "Needs repair",
        "fuel": "Petrol",
        "transmission": "Automatic",
        "color": "Black",
        "mileage": "30000",
        "price": "2200001",
        "wilaya": "31",
        "commune": "Oran",
        "description": "Honda Civic Sport in excellent condition, fully serviced.",
        "image": "/Users/apple1/Downloads/black.jpeg"
    },
    {
        "title": "Renault Clio 2019",
        "brand": "Other",
        "brand_name":"Renault",
        "model": "Clio",
        "version": "Expression",
        "engine": "1.2 TCe",
        "year": "2019",
        "condition": "Good",
        "fuel": "Petrol",
        "transmission": "Manual",
        "color": "Grey",
        "mileage": "60000",
        "price": "120000",
        "wilaya": "25",
        "commune": "Constantine",
        "description": "Renault Cli0  in good condition, regular maintenance done.",
        "image": "/Users/apple1/Downloads/renault.jpeg"
    },
    {
        "title": "Volkswagen Golf 2022",
        "brand": "Other",
        "brand_name":"Volkswagen",
        "model": "Golf",
        "version": "Highline",
        "engine": "2.0 TSIi",
        "year": "2022",
        "condition": "Like new",
        "fuel": "Petrol",
        "transmission": "Automatic",
        "color": "White",
        "mileage": "15000",
        "price": "350000",
        "wilaya": "9",
        "commune": "Blida",
        "description": "Almost new Volkswagen Golf, low mileage, full options.",
        "image": "/Users/apple1/Downloads/volks.jpeg"
    },
    {
        "title": "Hyundai Tucson 2020",
        "brand": "Hyundai",
        "model": "Tucson",
        "version": "GLS",
        "engine": "2.0 V6",
        "year": "2020",
        "condition": "Like new",
        "fuel": "Petrol",
        "transmission": "Automatic",
        "color": "Grey",
        "mileage": "500100",
        "price": "280000",
        "wilaya": "16",
        "commune": "Alger Centre",
        "description": "Hyundai Tucson SUV in great condition, family car.",
        "image": "/Users/apple1/Downloads/tuscan.jpeg"
    },
]


def test_bulk_car_ads(authenticated_page: Page):
    post_ad = PostAdPage(authenticated_page)

    for i, ad in enumerate(car_ads):
        print(f"\n── Posting ad {i + 1}/5: {ad['title']} ──")

        post_ad.go_to_post_ad()
        post_ad.upload_image(ad["image"])
        post_ad.wait_for_ai_processing()

        post_ad.select_category("Vehicles")
        post_ad.select_subcategory("Cars")

        post_ad.select_brand(ad["brand"], ad.get("brand_name", ""))
        post_ad.fill_model(ad["model"])
        post_ad.fill_version(ad["version"])
        post_ad.fill_engine(ad["engine"])
        post_ad.fill_year(ad["year"])
        post_ad.select_condition(ad["condition"])
        post_ad.select_fuel(ad["fuel"])
        post_ad.select_transmission(ad["transmission"])
        post_ad.select_color(ad["color"])
        post_ad.fill_mileage(ad["mileage"])

        post_ad.fill_title(ad["title"])
        post_ad.fill_price(ad["price"])
        post_ad.set_negotiable()

        post_ad.select_wilaya(ad["wilaya"])
        post_ad.fill_commune(ad["commune"])

        post_ad.fill_description(ad["description"])

        post_ad.publish_listing()

        # Wait between ads
        authenticated_page.wait_for_timeout(8000)

        print(f"✓ Ad {i + 1} posted successfully")