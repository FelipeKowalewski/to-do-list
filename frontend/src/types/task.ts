export interface Task {
  id: number;
  title: string;
  description: string;
  status: string;
  created_date: string;
  user_id: number;
}

export interface TaskCreate {
  title: string;
  description?: string;
}

export interface TaskUpdate {
  title?: string;
  description?: string;
  status?: string;
}