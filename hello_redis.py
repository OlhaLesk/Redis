import redis


REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_PWD = ""

def hello_redis():
    """Example Hello Redis Program"""
    # Redis Connection object
    try:
        # The decode_repsonses flag here directs the client to convert
        # the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=REDIS_HOST,
                              port=REDIS_PORT,
                              password=REDIS_PWD,
                              decode_responses=True)

        # Set the hello message in Redis
        r.set("msg:hello", "Hello Redis!!!")
        # Retrieve the hello message from Redis
        msg = r.get("msg:hello")
        print(msg)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    hello_redis()
