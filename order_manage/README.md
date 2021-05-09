Order Manage

two apps: 
1. order: for storing Items, Order and Customer information
2. inventory: for storing Deliver info


```
pip install -r requirements.txt
```

Run the below fixtures before hitting the API endpoints
```
python3 manage.py loaddata customer.json
```  

```
python3 manage.py loaddata item_category.json
```
```
python3 manage.py loaddata items.json
```
```
python3 manage.py loaddata teams.json
```


Delivery object has One to One relationship with Order object and a signal is trigerred when an order is created so that the corresponding Delivery object is also created
For more Object Relation info, an jpg file of ER Diag is attached

APIs:
**orders/create_order/** : creates order 
    input data: 
        distance: int
        items: array of Item objects
        customer: one customer id
        amount: array of quantity for each item object
        request = {
            "amount": [1],
            "items": [1],
            "distance": 1,
            "customer": 1
        }
        response - 
                HTTP 200 OK
            Allow: POST, OPTIONS
            Content-Type: application/json
            Vary: Accept

            {
            "order_id": "090521_06"
            }

-------------------------

**orders/get_items/** - fetch all orders from inventory


-----------------------


**inventory/get_order/** - get delivery time for the requested order
    request = {"order_id" :"090521_02"}
    reponse = HTTP 200 OK
            Allow: POST, OPTIONS
            Content-Type: application/json
            Vary: Accept

            {
            "msg": "The Estimated Delivery Time is 13:20:27.420844 for your order 090521_02"
            }


-------------------------


**inventory/finish_order/** - to change the status of an order to Completed state 

      input data:
            {"order_id": <order_id>}

      response =  HTTP 200 OK
        Allow: POST, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "msg ": "The order has been changed to completed. "
        }

--------------------------

**inventory/order_confirmation_status/** - gets the order status

        mehtod: POST
        input data:
            {"order_id": <order_id>}


