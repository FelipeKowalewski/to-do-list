import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

import { signup } from "../services/auth";
import type { SignupData } from "../types/auth";

export default function Signup() {
  const navigate = useNavigate();

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<SignupData>();

  async function onSubmit(data: SignupData) {
    try {
      await signup(data);
      navigate("/login");
    } catch (err: any) {
      alert(err.response?.data?.detail || "Erro ao criar conta");
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="bg-white p-6 rounded-lg shadow-md w-80 space-y-4"
      >
        <h1 className="text-xl font-semibold text-center">
          Criar conta
        </h1>

        {/* Email */}
        <div>
          <input
            type="email"
            placeholder="Email"
            className="w-full border rounded p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            {...register("email", {
              required: "Email é obrigatório",
            })}
          />
          {errors.email && (
            <p className="text-red-500 text-sm mt-1">
              {errors.email.message}
            </p>
          )}
        </div>

        {/* Senha */}
        <div>
          <input
            type="password"
            placeholder="Senha"
            className="w-full border rounded p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            {...register("password", {
              required: "Senha é obrigatória",
              minLength: {
                value: 6,
                message: "Mínimo de 6 caracteres",
              },
            })}
          />
          {errors.password && (
            <p className="text-red-500 text-sm mt-1">
              {errors.password.message}
            </p>
          )}
        </div>

        {/* Botão */}
        <button
          type="submit"
          disabled={isSubmitting}
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition disabled:opacity-50"
        >
          Criar conta
        </button>

        {/* Link para login */}
        <p className="text-sm text-center text-gray-600">
          Já tem conta?{" "}
          <span
            onClick={() => navigate("/login")}
            className="text-blue-600 hover:underline cursor-pointer"
          >
            Entrar
          </span>
        </p>
      </form>
    </div>
  );
}