# event-logger-api
Simple RESTful API to log events

## Getting Started

**Using docker / docker-compose ( Make sure you have docker installed locally)**
   - from the project directory run 
   `docker-compose build && docker-compose up -d`
   - this should setup containers for the server and database(this application uses postgres DB). The application should start running on [localhost:8000](http://127.0.0.1:8000/event)
   - to run tests execute `docker exec -it activity-server pipenv run python manage.py test --noinput --verbosity 2`
### Endpoints
 - **Save an Event** 

```
 POST /event
      {
        "email": "diego@chefhero.com",
        "environment": "production",
        "component": "order",
        "message": "the buyer #1 has placed an order successfully",
        "data": {
            "key": 123,
            "another key": "Some value"
        }
      }
```

 - **Retrieve Events(without filter)** 
   This returns all events

```
 GET /event
```
 - **Retrieve Events(using query filter)** 

```
 GET /event?q=<insert your queries here>
 
 EXAMPLE:
 GET /event?q=((email eq 'diego@chefhero.com') AND (createdAt gte '2018-1-1') AND (message ct 'buyer' ))
```
***NOTE*** : Date format in `YYYY-MM-DD`
 #### About the query filter
 - Sub queries but be grouped in brackets e.g `(component eq 'order')`
 - Combine queries using `AND` / `OR` keywords ( case-sensitive ) e.g `(email eq 'diego@chefhero.com') OR (createdAt gte '2018-1-1')`
 - List of query keywords below:

| Keyword( case-sensitive )         | Meaning           |
| ------------- |:-------------:|
| eq      | equal to |
| ct     | contains      |
| gte | greater thanor equal to      |
| AND | operatinal AND  (&)    |
| OR | operatinal OR     |

   
## Event Schema

The ID field of the [Event DB model](https://github.com/Kelechukwu/event-logger-api/blob/main/activityApi/api/models.py#L6) uses an auto-generated UUID4 field because
- the ID field needs to be unique since its the primary-key
- it also needs to be very hard to guess so that malicious users find it harder to gain access to records
- it allows easy distribution and replication of databases across multiple servers.

## Testing

This application has a tests folder where unit tests and intergation tests should be added for the api app.
See an example [here] (https://github.com/Kelechukwu/event-logger-api/blob/main/activityApi/api/tests/tests.py#L8)
 - to run existing tests execute `docker exec -it activity-server pipenv run python manage.py test --noinput --verbosity 2`

### What to test for
1. Test that a client can save an event . There is already an [integration test](https://github.com/Kelechukwu/event-logger-api/blob/main/activityApi/api/tests/tests.py#L15) for this 
2. Test that a client can retrieve events . [Example](https://github.com/Kelechukwu/event-logger-api/blob/main/activityApi/api/tests/tests.py#L24)
3. Test that a client can query for specific events.  For this there is an API query syntax with certain keywords that should be tested 
4. Finally, business logic that can be found in utils.py can be tested too in unittests

## Scaling this service
To make this service to be able to handle hundreds of requests per second we could do the following:
- Distrubute the requests by using a load balancer with multiple instances of the service behind. The load can be distributed using round-robin approach
- Sharding the data using a property like component or email. Where you can have the data sit on multiple DB servers based on the component name. Consistent hashing will ensure that the correct records are stored in the correct instance
- Having read Replicas( if there is a heavy read ratio). A master with replicas that are only used for reads while the master can handle only writes
- Caching results of frequently used queries could help reduce the load on the DB. 
