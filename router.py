from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TasksRepository
from schemas import STask, STaskAdd, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TasksRepository.add_one(task)

    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TasksRepository.find_all()
    return tasks
