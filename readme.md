Welcome!

This is readme file describing my backend for product inventory system.

The UI documentation is available via Swagger.

<p align="center">
  <img src="screenshots/Screenshot 2024-03-03 at 15.10.42.png" width="350" title="swagger1">
  <img src="screenshots/Screenshot 2024-03-03 at 15.10.54.png" width="350" alt="swagger2">
  <img src="screenshots/Screenshot 2024-03-03 at 15.11.05.png" width="350" alt="swagger3">
</p>


You can see below available API roots

<p align="center">
  <img src="screenshots/Screenshot 2024-03-03 at 15.13.01.png" width="350" title="API roots">
</p>

You can set filters, ordering and search fields.

<p align="center">
  <img src="screenshots/Screenshot 2024-03-03 at 15.13.31.png" width="350" title="filters">
  <img src="screenshots/Screenshot 2024-03-03 at 15.13.56.png" width="350" title="filters">
</p>


The images below demonstarte you how CRUD works in all of objects(Location, Establishment, Product). And the pagination is 4 objects per page.

<p align="center">
  <img src="screenshots/Screenshot 2024-03-03 at 15.15.41.png" width="350" title="CRUD">
  <img src="screenshots/Screenshot 2024-03-03 at 15.16.13.png" width="350" title="CRUD">
  <img src="screenshots/Screenshot 2024-03-03 at 15.16.53.png" width="350" title="CRUD">
  <img src="screenshots/Screenshot 2024-03-03 at 15.18.15.png" width="350" title="CRUD">
  <img src="screenshots/Screenshot 2024-03-03 at 15.18.28.png" width="350" title="CRUD">
  <img src="screenshots/Screenshot 2024-03-03 at 15.18.51.png" width="350" title="CRUD">
  <img src="screenshots/Screenshot 2024-03-03 at 15.19.08.png" width="350" title="CRUD">
  <img src="screenshots/Screenshot 2024-03-03 at 15.19.38.png" width="350" title="CRUD">
  <img src="screenshots/Screenshot 2024-03-03 at 20.18.26.png" width="350" title="CRUD">
  <img src="screenshots/Screenshot 2024-03-03 at 20.20.19.png" width="350" title="CRUD">
  <img src="screenshots/Screenshot 2024-03-03 at 20.20.25.png" width="350" title="CRUD">
</p>

This is the connection of database to PostgreSQL.

<p align="center">
  <img src="screenshots/Screenshot 2024-03-03 at 20.15.39.png" width="350" title="API roots">
</p>

There are some tests that checks the work of post requests in Product, Location and Establishment written using pytest.
<p align="center">
  <img src="screenshots/Screenshot 2024-03-03 at 20.08.33.png" width="350" title="API roots">
</p>

You can find containerization in dockerfiles.

<p align="center">
  <img src="screenshots/Screenshot 2024-03-03 at 20.32.07.png" width="350" title="API roots">
</p>

Even though this project fits all requirements, it still will be developed by adding more opportunities and security restrictions such as authentication and autorization for users.

Update:
Even though it wasn't in requirements, I decided to add Users. And you can see its setup below.


Added custom User with JWT authentication.
You can register with post request and get activation code(the code actually supposed to be sent to email, but there is an issue with sending an email)

<p align="center">
  <img src="screenshots/Screenshot 2024-03-12 at 21.07.51.png" width="350" title="API roots">
</p>

Then you can activate your account with sending get request.

<p align="center">
  <img src="screenshots/Screenshot 2024-03-12 at 21.08.18.png" width="350" title="API roots">
</p>


You can login and get refresh and access tokens.
<p align="center">
  <img src="screenshots/Screenshot 2024-03-12 at 21.06.40.png" width="350" title="API roots">
</p>


You can delete the user via delete request.
<p align="center">
  <img src="screenshots/Screenshot 2024-03-12 at 21.06.48.png" width="350" title="API roots">
</p>



