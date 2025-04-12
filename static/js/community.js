const navigateToPost = (element)=>{
    const url = element.getAttribute('data-url');
    if(url){
        window.location.href = url;
    }
}