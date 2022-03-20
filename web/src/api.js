import axios from 'axios'
let devMode = process.env.NODE_ENV === 'development'
// Todo: remove
// devMode=true

const axi = axios.create({
    baseURL: devMode ? 'http://localhost:5000/' : '/',
    withCredentials: true
})

const ENDPOINTS = {
    WEATHER_CURRENT:'/api/weather/current',
    WEATHER_DAILY:'/api/weather/daily'
}

export default {
    fetchWeatherCurrent(lat, lon){
        return axi.get(ENDPOINTS.WEATHER_CURRENT,
            {
                params: { lat, lon }
            })
    },
    fetchWeatherDaily(lat, lon){
        return axi.get(ENDPOINTS.WEATHER_DAILY,
            {
                params: { lat, lon }
            })
    }
}