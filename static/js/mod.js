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
    const flairInput = document.querySelector('.flair-form input[type="text"]');
    const createButton = document.querySelector('.btn-create-flair button');
    const flairLabel = document.querySelector('#flair-label');
    const newFlairForm = document.querySelector('new-flair-form');

    // createButton.disabled = true;
    // createButton.style.opacity = '0.5';

    flairInput.addEventListener('input', function(){
        if(flairInput.value.trim()!==''){
            createButton.disabled = false;
            createButton.style.opacity = '1';
        }else{
            createButton.disable = true;
            createButton.style.opacity = '0.5';
        }
        console.log(flairInput.value);
        flairLabel.textContent = flairInput.value;
    })
}

const createFlair = ()=>{
    const flairInput = document.querySelector('.flair-form input[type="text"]');
    const communityName = document.querySelector('.new-flair-form').dataset.communityName;
    const flairText = flairInput.value.trim();

    if (flairText !== "") {
        console.log(flairText);
        fetch(`/d/mod/${communityName}/postflair`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(), // Django CSRF protection
            },
            body: JSON.stringify({ flair: flairText }),
        })
        .then(response => response.json())
        .then(data => {
            window.location.reload()
        })
        .catch(error => alert(error));
    }
}

const createNewRule = ()=>{
    const ruleName = document.querySelector('.new-rule-form .name input[type="text"]');
    const ruleDescription = document.querySelector('.new-rule-form .description textarea');
    const saveButton = document.querySelector('.new-rule .heading .save-button');
    const communityName = document.querySelector('.new-rule').dataset.communityName;

    //saveButton.disabled = true;
    if(ruleName.value.trim()!=='' && ruleDescription.value.trim()!==''){
        fetch(`/d/mod/${communityName}/rules/new`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken(), // Django CSRF protection
            },
            body: JSON.stringify({ name: ruleName.value, description: ruleDescription.value }),
        })
        .then(response => response.json())
        .then(data => {
            if(data.redirect_url){
                window.location.href = data.redirect_url;
            }                               
        })
        .catch(error => alert(error));
    }
}