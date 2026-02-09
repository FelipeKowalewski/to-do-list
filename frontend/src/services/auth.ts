import api from "./api";
import type { LoginData, SignupData, TokenData } from "../types/auth";

/**
 * Realiza login do usuário
 */
export async function login(data: LoginData): Promise<TokenData> {
  const response = await api.post<TokenData>("/auth/login", data);

  // Salva token
  localStorage.setItem("access_token", response.data.access_token);

  return response.data;
}

/**
 * Realiza cadastro do usuário
 */
export async function signup(data: SignupData) {
  const response = await api.post("/auth/signup", data);
  return response.data;
}

/**
 * Logout simples
 */
export function logout() {
  localStorage.removeItem("access_token");
}