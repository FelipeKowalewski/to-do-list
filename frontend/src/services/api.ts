import axios from "axios";


// Instância central do Axios que conecta com o backend

const api = axios.create({
  baseURL: "http://localhost:8000",
});


// Interceptor para adicionar o token JWT automaticamente

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

// Interceptor de resposta para tratar erros globais

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token inválido ou expirado
      localStorage.removeItem("access_token");

      window.location.href = "/login";
    }

    return Promise.reject(error);
  }
);

export default api;