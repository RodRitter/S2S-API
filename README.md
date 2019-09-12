# Stock2Shop API Server

## Dependencies
- Vagrant
- Virtualbox (Vagrant needs this)

## Installation
First make sure you're in the project root

- `$ vagrant up` - Install the virtual environent. This might take a little while
  - Once this is done, the server should be running
- Navigate to `http://localhost:8080` (Frontend)
- API service is located at `http://localhost:5000` (Backend)

In the case where the server isn't automatically running:
- `$ vagrant ssh` - This will ssh you into the Ubuntu server
- `vagrant@machine:$ sudo service apache2 restart && sudo service s2s-api restart` - This will run the API server

## Endpoints
Documentation: http://localhost:5000/documentation

- `/products/` - [GET] Will return all products
- `/products/` - [POST] Will create a new product
  - parameters: sku string | attributes array(object) `{key: foo, value: bar}`
