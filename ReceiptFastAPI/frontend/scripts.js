document.getElementById('upload-form').addEventListener('submit', async function(event){
    
    event.preventDefault();
    hideUpload();
    showLoad();
    const formData = new FormData

    const fileInput = document.getElementById('image-input').files[0];
    formData.append('image',fileInput)

    try{
        const response = await fetch("http://127.0.0.1:8000/upload",{
            method:'POST',
            body:formData
        });
        

        if (!response.ok){
            throw new Error('HTTP error status ' + response.status)
        }

        const data = await response.json();
        console.log(data.status)
        recipe_data = data['recipes']
        console.log(recipe_data)
        hideUpload()
        hideLoad()
        showEmail()
        email_recipe(recipe_data)

    } catch(error){
        console.error(error)
        hideLoad();
        showUpload();
    }


})

function email_recipe(data){
    document.getElementById('email-form').addEventListener('submit',async function(event){
        event.preventDefault();
        const email_input = document.getElementById("email-input").value
        
        var valid_regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        const email_warning = document.getElementById('email-warning')

        if (!email_input.match(valid_regex)){
            email_warning.classList.remove('hidden')

        }else{
            email_warning.classList.add('hidden')
            const emailData = new FormData
            emailData.append('email',email_input)
            emailData.append('recipes',data)

            try{
                const response = await fetch("http://127.0.0.1:8000/email_recipe",{
                    method:'POST',
                    body:emailData
                });

                if (!response.ok){
                    console.log("Response problem" + response.status)
                }
                
                //After this we have emial
                hideEmail()
                showComplete()

                

            }catch (error) {
                console.error('Error: ',error)
            }
        }    
    })
}


function showUpload(){
    const upload_container = document.getElementById('upload-container')
    upload_container.style.display = "block";
}


function hideUpload(){
    const upload_container = document.getElementById('upload-container')
    upload_container.style.display = "none";
}


function showLoad(){
    const upload_container = document.getElementById('loading-container')
    upload_container.style.display = "block";
}


function hideLoad(){
    const upload_container = document.getElementById('loading-container')
    upload_container.style.display = "none";
}

function showEmail(){
    const email_container = document.getElementById('email-container');
    email_container.style.display = 'block'
    email_container.classList.remove('hidden');
}

function hideEmail(){
    const email_container = document.getElementById('email-container');
    email_container.style.display = 'none';
    email_container.classList.add('hidden');
}

function showComplete(){
    const complete_container = document.getElementById('completescreen');
    complete_container.style.display = 'block';
    

}