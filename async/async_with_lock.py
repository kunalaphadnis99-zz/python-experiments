import asyncio

lock = asyncio.Lock()

# Should be used inside function
# ... later
async with lock:
    pass
    # access shared state

# same as above
lock = asyncio.Lock()

# ... later
await lock.acquire()
try:
    pass
    # access shared state
finally:
    lock.release()
