# Base Store with Django REST Framework

___

**An online store on the Django Rest Framework is a web application
that allows users to browse, order, and purchase products online.
The application will contain many different features, such as
displaying a list of products, detailed product descriptions,
and a shopping cart.**

___

# Usage

The API has the following endpoints:

 - ***`api/products-list/`*** - **Displays a list of all products**
 - `product-detail/<int:pk>/` - **Shows information about a specific product**
 - `api/category/` - **Displays a list of all categories**
 - `api/cart-detail/` - **Creates or displays a shopping cart for the current user**
 - `api/add-product-cart/` - **Adds products to the current user's basket**
 - `api/cart-delete/` - **Deletes the user's basket to perform this action, the user must be logged in**
 - `api/order/` - **Creates an order** 
 - `api/comment/` - **Authorised users can add comments to a specific product**

**To create a user, you need to send a POST request `auth/users/`**

**To access endpoints that require authentication,
you must have a valid token. You can get a token
by sending a POST request to `auth/token/login/`
with the correct user credentials.**

___

# Models

## ___Product___

**The Product model represents a product in the shop.
It has the following fields:**
1. `id` - **Product identifier**
2. `category` - **(external key on the Category model) - Product category.**
3. `image` - **Product image (optional field)**
4. `price` - Product price
5. `description` - Product description
6. `created` - **Date and time of product creation is filled in automatically**
7. `availability` - **A boolean field that shows whether the product is in stock `True` - yes, `False` - no.**

## ___Category___

**The Category model represents the category of the products
in the shop. It has the following fields:**
1. `id` - **Category identifier**
2. `name` - **Category name**

## ___Cart___

**The Cart model represents the user's shopping cart.
It has the following fields:**
1. `user` - **foreign key for the User model**
2. `total` - **Total amount of goods in the basket**
3. `created` - **Date and time the basket was created (filled in automatically)**

## ___CartProduct___
**The CartProduct model represents products that the user adds
to their cart. The model has the following fields:**
1. `cart` - **Foreign key of the cart**
2. `product` - **Foreign key product**
3. `quantity` - **Quantity of a particular item in the basket**
4. `total` - **Total price of the added product**

## ___Order___
**The Order model represents the creation of an order.
It has the following fields:**
It has the following fields:**
1. `user`- **Foreign key for the User model**
2. `total` - **Total amount of goods in the basket**
3. `created`- **Date and time the basket was created (filled in automatically)**

## OrderItem
**The OrderItem model represents a user order.
It has the following fields:**
1. `order` - **Foreign key order**
2. `cart` - **Foreign key cart**
3. `city` - **The city to which you want to send the order**
4. `index` - **City code**
5. `total` - **Total price of the added product**

## ___Comment___
**The Comments model represents a comment left by the user
on an item in the shop. It has the following fields:**
1. `author` - **The user who left the comment.**
2. `parent` - **The parent comment to which this comment is attached.**
3. `text` - **Comment text**
4. `created` - **Date and time the comment created**
5. `product` - **The product to which this comment is linked.**

___

**In the requirements.txt file, you can find the modules that
were used during the development phase of this project.**
