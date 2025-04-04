const handleCreateNewFlair = () => {
    const newFlairButton = document.querySelector('button.btn-new-flair');
    const newFlairForm = document.querySelector('div.new-flair-form');
    const postFlair = document.querySelector('div.post-flair');

    console.log(newFlairForm.style.display);
    if(newFlairForm.style.display === 'none' || newFlairForm.style.display === ''){
        newFlairForm.style.display = 'flex';
    }else{
        newFlairForm.style.display = 'none';
    }
    newFlairForm.style.width = '30%'
    console.log(postFlair.style.width)
}

const createAndSaveFlair = ()=>{
    const flairInput = document.querySelector('.flair-form input');
    const createButton = document.querySelector('.btn-new-flair button');
    const flairLabel = document.querySelector('flair-label');
    
}