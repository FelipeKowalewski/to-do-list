import { useForm } from "react-hook-form";

import { login } from "../services/auth";
import type { LoginData } from "../types/auth";

export default function Login() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm<LoginData>();

  async function onSubmit(data: LoginData) {
    try {
      const token = await login(data);
      localStorage.setItem("access_token", token.access_token);
      window.location.href = "/tasks";
    } catch {
      alert("Email ou senha inválidos");
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <form
            onSubmit={handleSubmit(onSubmit)}
            className="bg-white p-6 rounded shadow w-80 space-y-4"
        >
            <h1 className="text-xl font-semibold text-center">Login</h1>

            <input
                type="email"
                placeholder="Email"
                className="w-full border p-2 rounded"
                {...register("email", { required: "Email é obrigatório" })}
            />
            {errors.email && (
                <p className="text-red-500 text-sm">{errors.email.message}</p>
            )}

            <input
                type="password"
                placeholder="Senha"
                className="w-full border p-2 rounded"
                {...register("password", { required: "Senha é obrigatória" })}
            />
            {errors.password && (
                <p className="text-red-500 text-sm">{errors.password.message}</p>
            )}

            <button
                type="submit"
                className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
            >
                Entrar
            </button>
        </form>
    </div>
  );
}