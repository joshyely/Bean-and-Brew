import axios from 'axios'
import { getToken, deleteToken } from './auth';

export const api = axios.create({
    baseURL: '/api',
    headers: {
      'Content-Type': 'application/json',
    },
});

api.interceptors.request.use((config) => {
  const token = getToken();
  if (token != null) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      deleteToken();
    }
    return Promise.reject(error)
  }
)

// Test communication with the backend restAPI
export const apiTestCall = () => {
  api.get('/foobar').then(response => {
    console.log(response);
  });
};

