const API = 'http://localhost:8000/api/v1'

export const postRegister = async (data: any) => {
  const info = await fetch(`${API}/register`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  const rawData = await info.json()
  console.log(rawData);
  
  return rawData
}

export const postLogin = async (data: any) => {
  const info = await fetch(`${API}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  const rawData = await info.json()
  console.log(rawData.access_token)
  return rawData.access_token
}

export const postProfile = async (data: any, token: string) => {
  const info = await fetch(`${API}/profile`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(data)
  })
  const rawData = await info.json()
  console.log(rawData);
  return rawData
}

export const getProfileByEmail = async (email: string, token: string) => {
  const info = await fetch(`${API}/profile/${email}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }
  })
  const rawData = await info.json()
  console.log(rawData);
  return rawData
}

export const getUserDataByEmail = async (email: string, token: string) => {
  const info = await fetch(`${API}/user/${email}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    }
  })
  const rawData = await info.json()
  console.log(rawData);
  return rawData
}