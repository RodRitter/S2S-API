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
API: http://localhost:5000/

- `/products/` - [GET] Will return all products
- `/products/` - [POST] Will create a new product
  - parameters: sku string | attributes array(object) `{key: foo, value: bar}`

## Directory Structure
- `[apache]` - Holds all the apache site .conf files. They are copied to their location when the machine is provisioned
- `[service]` - Holds custom services to run the API in the background (`s2s-api`)
- `[frontend]` - The compiled frontend code lives here so we can share a host - [Frontend Source Code](https://github.com/RodRitter/S2S-Frontend)
- `[api]` - Here is the meat of it all. The API code lives here

## Tech stack
Frontend:
- React
  - React is my go-to frontend framework.
- Bootstrap
  - To save time, I used Bootstrap to make everything look nice

Backend:
- Flask
  - I chose flask because of it's quick setup time and ease of use. I kept it pretty light of plugins to avoid complexity.
- Swagger
  - This was the easiest framework I could find to generate documentation. It allowed me to take advantage of swagger-ui to make it look purdy
  
