import Vue from 'vue';
import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
//axios.defaults.headers.common['Authorization'] = document.cookie;
//
//function getToken(type){
//    let cookies = document.cookie.split("=");
//    let last_index = cookies.length -1;
//    let token = null;
//    if (cookies.length > 5) {
//        token = cookies[last_index];
//    }
//    return token;
//}
//
//function withAuth(headers={}) {
//  return () => ({
//    ...headers,
//    'withCredentials': true,
//    'Authorization': `Bearer ${getToken('jwt-access')}`
//  })
//}

const axiosHelpers = {
    getRequest(url, headersObj={}) {
        headersObj.withCredentials = true;
        return axios.get(url, headersObj)
        .catch((error) => {
            if (quotaExceeded(error)){
                sessionStorage.clear()
            }
        })
    },
    postRequest(url, data, headersObj={}) {
        headersObj.withCredentials = true;
        return axios.post(url, data, headersObj)
        .catch((error) => {
            if (quotaExceeded(error)){
                sessionStorage.clear()
            }
        })
    },
    deleteRequest(url, headersObj={}) {
        headersObj.withCredentials = true;
        return axios.delete(url, headersObj)
        .catch((error) => {
            if (quotaExceeded(error)){
                sessionStorage.clear()
            }
        })
    },
    putRequest(url, data, headersObj={}) {
        headersObj.withCredentials = true;
        return axios.put(url, data, headersObj)
        .catch((error) => {
            if (quotaExceeded(error)){
                sessionStorage.clear()
            }
        })
    },
    patchRequest(url, data, headersObj={}) {
        headersObj.withCredentials = true;
        return axios.patch(url, data, headersObj)
        .catch((error) => {
            if (quotaExceeded(error)){
                sessionStorage.clear()
            }
        })
    }
}

function quotaExceeded(e){
    let quotaExceeded = false;
    if (e.code) {
      switch (e.code) {
        case 22:
          quotaExceeded = true;
          break;
        case 1014:
          // Firefox
          if (e.name === 'NS_ERROR_DOM_QUOTA_REACHED') {
            quotaExceeded = true;
          }
          break;
      }
    } else if (e.number === -2147024882) {
      // Internet Explorer 8
      quotaExceeded = true;
    }
    return quotaExceeded;
}

export { axiosHelpers };