import axios, { AxiosError } from 'axios'
import { HttpStatusCode } from 'axios';
import { getToken, deleteToken } from './auth';

const backendBaseURL = 'http://localhost:5000/'

export const apiJSON = axios.create({
  baseURL: backendBaseURL,
  headers: {
    'Content-Type': 'application/json',
  },
  validateStatus: (status) => status >= 200 && status < 300 && status !== 226,
});

apiJSON.interceptors.request.use((config) => {
  const token = getToken();
  if (token != null) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

apiJSON.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response) {
      switch (error.response?.status) {
        case 401:
          deleteToken();
          break;
      }
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


export const apiTest = async () => {
  let response = await axios({
    method: 'get',
    baseURL: '/api',
    url: '/',
  });

  if (response.status != HttpStatusCode.Accepted) {
    console.log('API ERROR: ', response);
  }
  else {
    console.log('API SUCCESS: ', response);
  }
}

