from website.auth import db
from website.models import Category, Product
from main import create_app
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


app = create_app()


def seed():
    with app.app_context():
        # Categories
        categories = [
            'Dog food & treats',
            'Dog beds & baskets',
            'Dog toys, sport & training',
            'Dog grooming & care'
        ]

        # Products
        products_data = [
            {
                "name": "Healthy Paws Dog Food",
                "description": "Nutritious and delicious dog food made with all-natural ingredients.",
                "price": 15.0,
                "image": "Dog_Dryfood_1.jpg",
                "category": "Dog food & treats"
            },
            {
                "name": "Tasty Bone Treats",
                "description": "Yummy bone-shaped treats that your dog will love.",
                "price": 8.0,
                "image": "Dog_Dryfood_1.jpg",
                "category": "Dog food & treats"
            },
            {
                "name": "Grain-Free Dog Biscuits",
                "description": "Tasty and healthy grain-free biscuits for sensitive dogs.",
                "price": 10.0,
                "image": "Dog_Dryfood_1.jpg",
                "category": "Dog food & treats"
            },
            {
                "name": "Organic Dog Chew",
                "description": "Organic and long-lasting chew to keep your dog busy.",
                "price": 7.0,
                "image": "Dog_Dryfood_1.jpg",
                "category": "Dog food & treats"
            },
            {
                "name": "Comfy Dog Bed",
                "description": "Super comfortable and cozy bed for your furry friend.",
                "price": 25.0,
                "image": "Dog_Beds_1.jpg",
                "category": "Dog beds & baskets"
            },
            {
                "name": "Soft Dog Blanket",
                "description": "Soft and warm blanket for your dog to snuggle in.",
                "price": 12.0,
                "image": "Dog_Beds_1.jpg",
                "category": "Dog beds & baskets"
            },
            {
                "name": "Orthopedic Dog Basket",
                "description": "Orthopedic basket to support your dog's joints and back.",
                "price": 30.0,
                "image": "Dog_Beds_1.jpg",
                "category": "Dog beds & baskets"
            },
            {
                "name": "Waterproof Dog Bed",
                "description": "Waterproof and easy to clean dog bed.",
                "price": 28.0,
                "image": "Dog_Beds_1.jpg",
                "category": "Dog beds & baskets"
            },
            {
                "name": "Squeaky Dog Ball",
                "description": "Fun squeaky ball for playtime.",
                "price": 5.0,
                "image": "Dog_Toys_Sports_Acc_1.jpg",
                "category": "Dog toys, sport & training"
            },
            {
                "name": "Dog Agility Kit",
                "description": "Complete agility kit to keep your dog fit and active.",
                "price": 50.0,
                "image": "Dog_Toys_Sports_Acc_1.jpg",
                "category": "Dog toys, sport & training"
            },
            {
                "name": "Interactive Dog Toy",
                "description": "Keep your dog entertained and active with this interactive toy.",
                "price": 20.0,
                "image": "Dog_Toys_Sports_Acc_1.jpg",
                "category": "Dog toys, sport & training"
            },
            {
                "name": "Dog Training Leash",
                "description": "Durable leash for training your dog.",
                "price": 15.0,
                "image": "Dog_Toys_Sports_Acc_1.jpg",
                "category": "Dog toys, sport & training"
            },
            {
                "name": "Dog Grooming Brush",
                "description": "Easily remove loose hair and tangles with this grooming brush.",
                "price": 10.0,
                "image": "Dog_Grooming_Care_1.jpg",
                "category": "Dog grooming & care"
            },
            {
                "name": "Natural Dog Shampoo",
                "description": "Gentle and natural shampoo to keep your dog's coat shiny and clean.",
                "price": 12.0,
                "image": "Dog_Grooming_Care_1.jpg",
                "category": "Dog grooming & care"
            },
            {
                "name": "Dog Nail Clippers",
                "description": "Easy to use nail clippers to keep your dog's nails trimmed.",
                "price": 8.0,
                "image": "Dog_Grooming_Care_1.jpg",
                "category": "Dog grooming & care"
            },
            {
                "name": "Dog Ear Cleaner",
                "description": "Gentle ear cleaner to remove wax and dirt from your dog's ears.",
                "price": 10.0,
                "image": "Dog_Grooming_Care_1.jpg",
                "category": "Dog grooming & care"
            }
        ]

        for category_name in categories:
            category = Category(name=category_name)
            db.session.add(category)
        db.session.commit()

        for product_data in products_data:
            category = Category.query.filter_by(
                name=product_data['category']).first()
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                image=product_data['image'],
                category_id=category.id
            )
            db.session.add(product)
        db.session.commit()

        print('Database seeded successfully.')


if __name__ == '__main__':
    seed()
