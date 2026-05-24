import axios from "axios";

const baseURL = import.meta.env.VITE_API_URL || "http://localhost:8000/api";

export const api = axios.create({
  baseURL,
  headers: { "Content-Type": "application/json" },
  timeout: 60000,
});

api.interceptors.response.use(
  (r) => r,
  (error) => {
    const message =
      error.response?.data?.error || error.message || "Network error";
    return Promise.reject(new Error(message));
  }
);
