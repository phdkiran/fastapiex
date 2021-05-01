# fastapiex
Install packages using requirements.txt

Run application using uvicorn main:app 

Generate transactions using POST /items/ 
and GET /items/blog_id.

POST  example:
POST http://localhost:8000/items/
{"id":2,"author":"kiran","title":"elk","content":"super","date":"2021-01-10"}

GET example:
http://localhost:8000/items/2
{"id":2,"author":"kiran","title":"elk","content":"super","date":"2021-01-10"}

http://localhost:8000/items/3
"Blog id 3 not present"



http POST localhost:8000/items/ id=2  author=kiran title=elk content=super date=2021-01-10
