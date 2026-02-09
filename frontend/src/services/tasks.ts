import api from "./api";
import type { Task, TaskCreate, TaskUpdate } from "../types/task";


/**
 * Lista todas as tasks do usuário logado
 */
export async function listTasks(): Promise<Task[]> {
  const response = await api.get<Task[]>("/tasks");
  return response.data;
}

/**
 * Cria uma nova task
 */
export async function createTask(task: TaskCreate): Promise<Task> {
  const response = await api.post<Task>("/tasks", task);
  return response.data;
}

/**
 * Atualiza uma task existente
 */
export async function updateTask(
  taskId: number,
  task: TaskUpdate
): Promise<Task> {
  const response = await api.put<Task>(`/tasks/${taskId}`, task);
  return response.data;
}

/**
 * Deleta uma task
 */
export async function deleteTask(taskId: number): Promise<void> {
  await api.delete(`/tasks/${taskId}`);
}