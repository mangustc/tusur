import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.set(name="university", value="TUSUR")
print(r.get(name="university"))

r.lpush("employees", "Andrey", "Oleg")
print(r.lrange("employees", 0, -1))

r.hset(name="building", mapping={
    "address": "Vershinina Street, 74",
    "name": "Fakultet elektronnoy tekniki tusura",
    "working_hours": "8:30 - 17:30"
})
print(r.hgetall(name="building"))

r.sadd("employees2", "Sanya", "Ivan", "Sanya")
print(r.smembers("employees2"))

