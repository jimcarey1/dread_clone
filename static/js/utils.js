const getCSRFToken = ()=>{
    let cookieValue = null;
    if(document.cookie && document.cookie!==''){
        document.cookie.split(';').forEach(cookie=>{
            const [name, value] = cookie.trim().split('=');
            if(name==='csrftoken'){
                cookieValue = decodeURIComponent(value);
            }
        })
    }
    return cookieValue;
}