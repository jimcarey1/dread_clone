const createPostComment = ()=>{
    console.log('Hi, This function is running properly.')
    const commentInput = document.querySelector('.post-view .add-comment-form form .comment-input input');

    const communityName = document.querySelector('.post-view').dataset.communityName;
    const postId = document.querySelector('.post-view').dataset.postId;
    if(commentInput.value.trim()!==''){
        fetch(`submit/`,{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(), //Django CSRF Protection
            },
            body: JSON.stringify({content:commentInput.value})
        })
        .then((response)=>response.json())
        .then((data)=>{
            if(data.redirect_url){
                window.location.href= data.redirect_url;
            }
        })
        .catch((error)=>alert(error));
    }
}