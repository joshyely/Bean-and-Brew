import axios, { AxiosError } from 'axios'
import { HttpStatusCode } from 'axios';
import { getToken, deleteToken } from './auth';

const backendBaseURL = '/api'

export const apiJSON = axios.create({
    baseURL: backendBaseURL,
    headers: {
      'Content-Type': 'application/json',
    },
});

apiJSON.interceptors.request.use((config) => {
  const token = getToken();
  if (token != null) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  config.validateStatus = status => status >= 200 && status < 300 && status != 226;
  return config;
});

apiJSON.interceptors.response.use(
  async (response) => response,
  async (error) => {
    switch(error.response?.status){
      case 401:
        deleteToken();
        break;
    }
    return Promise.reject(error)
  }
);

export const apiFormUrlEncoded = axios.create({
  baseURL: backendBaseURL,
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
  },
});

// Test communication with the backend restAPI
export const apiTestCall = () => {
  apiJSON.get('/foobar').then(response => {
    console.log(response);
  });
};

