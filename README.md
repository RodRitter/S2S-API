# Stock2Shop API Server

## Dependencies
- Vagrant
- VirtualBox (Vagrant needs this)
  - I've had trouble on Mac with VB so if you run into trouble with it there, I'm sorry!

## Installation
First make sure you're in the project root

- `$ vagrant up` - Install the virtual environent. This might take a little while
  - Once this is done, the server should be running
- Navigate to `http://localhost:8080` (Frontend)

In the case where the server isn't automatically running:
- `$ vagrant ssh` - This will ssh you into the Ubuntu server
- `vagrant@machine:$ sudo service apache2 restart && sudo service s2s-api restart` - This will run the API server

If you have port conflicts, you can change them in `VagrantFile`. Run `$ vagrant up --provision` to register port forwarding after that.
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

## Tech Stack
Frontend:
- `React`
  - React is my go-to frontend framework.
- `Bootstrap`
  - To save time, I used Bootstrap to make everything look nice

Backend:
- `Flask`
  - I chose flask because of it's quick setup time and ease of use. I kept it pretty light of plugins to avoid complexity.
- `Swagger`
  - This was the easiest framework I could find to generate documentation. It allowed me to take advantage of swagger-ui to make it look purdy

## Scaling & Improvement Considerations
- The first thing I would do is use a testing suite and write tests for the few endpoints we have. This way you have a stable base when you scale up.
- The next thing I would do is create automated CI builds for the server, using webhooks into the repositories for both backend and frontend.


#### Minor changes
- I would change the structure of the `attributes` API structure to allow for easier accessibility to key/value pairs. The less parsing the frontend has to do, the better.
ie. Instead of `attributes: [{foo: bar}, {size: small}]` I would do something like `attributes: [{key: foo, value: bar}]`
- Then I'd find a better way to create automated documentation, using decorators instead of manually creating the blueprint




