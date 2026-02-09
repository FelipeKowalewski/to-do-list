import { useEffect, useState } from "react"
import { listTasks, createTask, updateTask, deleteTask } from "../services/tasks"
import type { Task } from "../types/task"

const statusLabel: Record<Task["status"], string> = {
  pending: "Pendente",
  in_progress: "Em progresso",
  done: "Finalizada",
}

export default function Tasks() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [editingId, setEditingId] = useState<number | null>(null)
  const [isCreating, setIsCreating] = useState(false)

  const [formData, setFormData] = useState({
    title: "",
    description: "",
    status: "pending" as Task["status"],
  })

  async function loadTasks() {
    const data = await listTasks()
    setTasks(
      data.sort(
        (a, b) =>
          new Date(b.created_date).getTime() -
          new Date(a.created_date).getTime()
      )
    )
  }

  useEffect(() => {
    loadTasks()
  }, [])

  function startCreate() {
    setIsCreating(true)
    setEditingId(null)
    setFormData({ title: "", description: "", status: "pending" })
  }

  function startEdit(task: Task) {
    setEditingId(task.id)
    setIsCreating(false)
    setFormData({ title: task.title, description: task.description, status: task.status })
  }

  async function handleCreate() {
    await createTask(formData)
    setIsCreating(false)
    loadTasks()
  }

  async function handleUpdate(taskId: number) {
    await updateTask(taskId, formData)
    setEditingId(null)
    loadTasks()
  }

  async function handleDelete(taskId: number) {
    await deleteTask(taskId)
    loadTasks()
  }

  return (
    <div className="min-h-screen bg-gray-100">
      {/* HEADER */}
      <header className="fixed top-0 left-0 right-0 bg-white shadow px-6 py-4 flex justify-between items-center z-10">
        <button
          onClick={startCreate}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors"
        >
          + Nova Task
        </button>

        <div className="flex items-center gap-3">
          <span className="text-gray-700">usuario@email.com</span>
          <div className="w-8 h-8 bg-gray-300 rounded-full" />
        </div>
      </header>

      {/* CONTENT */}
      <main className="pt-24 px-6 space-y-4 max-w-5xl mx-auto">
        {/* CREATE CARD */}
        {isCreating && (
          <TaskCard
            formData={formData}
            setFormData={setFormData}
            onSave={handleCreate}
            onCancel={() => setIsCreating(false)}
            isCreating={true}
          />
        )}

        {/* TASK LIST */}
        {tasks.map((task) => {
          const isEditing = editingId === task.id

          return (
            <div
              key={task.id}
              className="bg-white rounded shadow min-h-[140px] flex flex-col justify-between px-4 py-3"
            >
              <div className="flex-1 mb-2">
                {isEditing ? (
                  <EditableFields formData={formData} setFormData={setFormData} />
                ) : (
                  <>
                    <h3 className="font-semibold text-lg">{task.title}</h3>
                    <p className="text-sm text-gray-600">{task.description}</p>
                    <p className="text-xs text-gray-500 mt-1">
                      {statusLabel[task.status]} • {new Date(task.created_date).toLocaleString()}
                    </p>
                  </>
                )}
              </div>

              <div className="flex gap-3">
                {isEditing ? (
                  <>
                    <button
                      onClick={() => handleUpdate(task.id)}
                      className="bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700 transition-colors"
                    >
                      Salvar
                    </button>
                    <button
                      onClick={() => setEditingId(null)}
                      className="bg-gray-400 text-white px-3 py-1 rounded hover:bg-gray-500 transition-colors"
                    >
                      Cancelar
                    </button>
                  </>
                ) : (
                  <>
                    <button
                      onClick={() => startEdit(task)}
                      className="text-blue-600 hover:underline"
                    >
                      Editar
                    </button>
                    <button
                      onClick={() => handleDelete(task.id)}
                      className="text-red-600 hover:underline"
                    >
                      Excluir
                    </button>
                  </>
                )}
              </div>
            </div>
          )
        })}
      </main>
    </div>
  )
}

/* ===========================
   COMPONENTES AUXILIARES
=========================== */

function EditableFields({
  formData,
  setFormData,
  disabledStatus = false,
}: {
  formData: { title: string; description: string; status: Task["status"] }
  setFormData: React.Dispatch<
    React.SetStateAction<{ title: string; description: string; status: Task["status"] }>
  >
  disabledStatus?: boolean
}) {
  return (
    <div className="flex flex-col gap-2">
      <input
        className="w-full border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
        placeholder="Título"
        value={formData.title}
        onChange={(e) => setFormData({ ...formData, title: e.target.value })}
      />

      <input
        className="w-full border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
        placeholder="Descrição"
        value={formData.description}
        onChange={(e) => setFormData({ ...formData, description: e.target.value })}
      />

      <select
        className="w-full border border-gray-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
        value={formData.status}
        onChange={(e) =>
          setFormData({ ...formData, status: e.target.value as Task["status"] })
        }
        disabled={disabledStatus}
      >
        <option value="pending">Pendente</option>
        <option value="in_progress">Em progresso</option>
        <option value="done">Finalizada</option>
      </select>
    </div>
  )
}

function TaskCard({
  formData,
  setFormData,
  onSave,
  onCancel,
  isCreating = false,
}: {
  formData: { title: string; description: string; status: Task["status"] }
  setFormData: React.Dispatch<
    React.SetStateAction<{ title: string; description: string; status: Task["status"] }>
  >
  onSave: () => void
  onCancel: () => void
  isCreating?: boolean
}) {
  return (
    <div className="bg-white rounded shadow min-h-[140px] flex flex-col justify-between px-4 py-3">
      <EditableFields formData={formData} setFormData={setFormData} disabledStatus={isCreating} />

      <div className="flex gap-3 mt-2">
        <button
          type="button"
          onClick={onSave}
          className="bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700 transition-colors"
        >
          Criar
        </button>
        <button
          onClick={onCancel}
          className="bg-gray-400 text-white px-3 py-1 rounded hover:bg-gray-500 transition-colors"
        >
          Cancelar
        </button>
      </div>
    </div>
  )
}
