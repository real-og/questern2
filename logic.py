import redis

def increase_counter(redis_host, redis_port, redis_password, counter_key, increment_by=1):
    try:
        redis_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password)
        current_value = redis_client.get(counter_key)
        if current_value is None:
            current_value = 0
        else:
            current_value = int(current_value)
        new_value = current_value + increment_by
        redis_client.set(counter_key, new_value)
        return new_value

    except Exception as e:
        print("Произошла ошибка:", e)
        return None