import asyncio
import aioredis
import texts
from loader import SHEET_LINK

class RedisClient:
    def __init__(self, loop):
        self.loop = loop
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.create_redis_pool('redis://localhost', encoding='utf-8')

    async def close(self):
        self.redis.close()
        await self.redis.wait_closed()

    async def append_user(self, id: str, username: str, full_name: str = 'Без имени'):
        await self.redis.hmset(id, {'username': username, 'full_name': full_name, 'level': '1'})

    async def change_level(self, id, level):
        await self.redis.hset(id, 'level', level)

    async def change_name(self, id, name):
        await self.redis.hset(id, 'full_name', name)

    async def change_email(self, id, email):
        await self.redis.hset(id, 'email', email)

    async def set_lottary_number(self, id, number):
        await self.redis.hset(id, 'lottary_number', number)

async def main():
    loop = asyncio.get_event_loop()
    redis_client = RedisClient(loop)

    await redis_client.connect()

    await redis_client.append_user('user_id', 'username', 'full_name')
    await redis_client.change_level('user_id', '2')
    await redis_client.change_name('user_id', 'new_name')

    await redis_client.close()

if __name__ == "__main__":
    asyncio.run(main())
