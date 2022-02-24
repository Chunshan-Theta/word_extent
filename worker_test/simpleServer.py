import os
from util.aredis_queue import QueueRespondsTask
import asyncio

from util import Job


async def main():

    while True:
        QRTask = QueueRespondsTask(task_name)
        task = await QRTask.get_content()
        if task is None:
            await asyncio.sleep(1)
            continue

        #
        obj = task.get("obj", None)
        request_id = task.get("request_id", None)
        job_obj = Job(request_id=request_id, content=obj)

        #
        await QRTask.to_master(job_obj.to_json(), job_obj.request_id)


task_name = os.getenv("task_name", "default")
print(f"Get work from: {task_name}")
asyncio.run(main())
