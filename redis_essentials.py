import redis


# The port=6379 and db=0 are default values.
r = redis.Redis(host='localhost', port=6379, db=0)

print(r.set('foo','bar'))
print(r.get('foo'))

# increase/decrease
print(r.set('count',1))
print(r.incr('count'))
print(r.incr('count'))
print(r.decr('count'))
print(r.get('count'))

print(r.set('count',123456789012345678901234567890))
try:
    print(r.incr('count'))
except redis.exceptions.ResponseError as err:
    print(err)

# rpush, llen, and lindex
# The rpush inserts all the specified values at the tail
# of the list stored at key.
# The llen returns the length of the list stored at key.
# The lindex returns the element at index index in the list
# stored at key. The index is zero-based, so 0 means the
# first element, 1 the second element and so on.
print(r.rpush('hispanic', 'uno'))
print(r.rpush('hispanic', 'dos'))
print(r.rpush('hispanic', 'tres'))
print(r.rpush('hispanic', 'cuatro'))
print(r.llen('hispanic'))
print(r.lindex('hispanic', 3))
