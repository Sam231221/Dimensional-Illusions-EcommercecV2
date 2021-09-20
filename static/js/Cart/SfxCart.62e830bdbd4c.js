var updateBtns = document.getElementsByClassName('electricitysfx-cart')
for (var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
    var productName = this.dataset.product
    var publisherId=this.dataset.pubid     
     var action = this.dataset.action


     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         updateElectricitySfx(productName, publisherId,action);
     }
  })
}

function addCookieItem(productId, action){
    console.log('Customer Not logged in...')
}

function updateElectricitySfx(productName, publisherId,action){  
 
     var url = '/updatelightiningsfx/' 
     fetch(url,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken,
 
        },
        body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action}) 
     })                                                                  
     .then((response) =>{
          return response.json()  
     })
     .then((data) =>{
          console.log('data:',data)  
          location.reload()
     })
 }

 var updateBtns = document.getElementsByClassName('firesfx-cart')
for (var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(){
     var productName = this.dataset.product
     var publisherId=this.dataset.pubid     
     var action = this.dataset.action
     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         updateFireSfx(productName,publisherId, action);
     }
  })
}

function addCookieItem(productId, action){
    console.log('Customer Not logged in...')
}

function updateFireSfx(productName,publisherId, action){ 

     var url = '/updatefiresfx/'  
     fetch(url,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken,
 
        },
        body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action}) 
     })                                                                 
     .then((response) =>{
          return response.json()   
     })
     .then((data) =>{
          console.log('data:',data) 
          location.reload()
     })
 }
 
var updateBtns = document.getElementsByClassName('EnergySfx-cart')
for (var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(){
     var productName = this.dataset.product
     var publisherId=this.dataset.pubid     
     var action = this.dataset.action
     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         updateEnergySfx(productName, publisherId,action);
     }
  })
}
function addCookieItem(productId, action){
    console.log('Customer Not logged in...')
}

function updateEnergySfx(productName, publisherId,action){  
     var url = '/updateEnergysfx/' 
     fetch(url,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken,
 
        },
        body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action})  
     })                                                               
     .then((response) =>{
          return response.json()  
     })
     .then((data) =>{
          console.log('data:',data) 
          location.reload()
     })
 }

var updateBtns = document.getElementsByClassName('EnvironmentalSfx-cart')
for (var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(){
     var productName = this.dataset.product
     var publisherId=this.dataset.pubid     
     var action = this.dataset.action

     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         updateEnvironmentalsfx(productName, publisherId,action);
     }
  })
}

function addCookieItem(productId, action){
    console.log('Customer Not logged in...')
}

function updateEnvironmentalsfx(productName,publisherId ,action){  

     var url = '/updateEnvironmentalsfx/'  
     fetch(url,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action}) 
     })                                           
     .then((response) =>{
          return response.json()  
     })
     .then((data) =>{
          console.log('data:',data)  
          location.reload()
     })
 }
 

 var updateBtns = document.getElementsByClassName('MachinerySfx-cart')
for (var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(){
     var productName = this.dataset.product
     var publisherId=this.dataset.pubid     
     var action = this.dataset.action

     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         updateMachinerySfx(productName, publisherId,action);
     }
  })
}


function addCookieItem(productId, action){
    console.log('Customer Not logged in...')
}

function updateMachinerySfx(productName, publisherId,action){ 

     var url = '/updatemachinerysfx/'  
     fetch(url,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken,
 
        },
        body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action})  
     })                                             
     .then((response) =>{
          return response.json()  
     })
     .then((data) =>{
          console.log('data:',data)  
          location.reload()
     })
 }
 

 var updateBtns = document.getElementsByClassName('WeaponSfx-cart')
 for (var i=0; i<updateBtns.length; i++){
      updateBtns[i].addEventListener('click', function(){
      var productName = this.dataset.product
      var publisherId=this.dataset.pubid     
      var action = this.dataset.action

      if(user == 'AnonymousUser'){  
          addCookieItem(productName, action)
      }
      else{
          updateWeaponsfx(productName, publisherId,action);
      }
   })
 }
 
 function addCookieItem(productId, action){
     console.log('Customer Not logged in...')
 }
 
 function updateWeaponsfx(productName,publisherId ,action){  

      var url = '/updateweaponsfx/'  
      fetch(url,{
         method:'POST',
         headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
         },
         body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action})  
        })                                             
        .then((response) =>{
             return response.json()  
        })
        .then((data) =>{
             console.log('data:',data)  
             location.reload()
        })
  }
 
  var updateBtns = document.getElementsByClassName('FightingSfx-cart')
 for (var i=0; i<updateBtns.length; i++){
      updateBtns[i].addEventListener('click', function(){
      var productName = this.dataset.product
      var publisherId=this.dataset.pubid     
      var action = this.dataset.action

      if(user == 'AnonymousUser'){  
          addCookieItem(productName, action)
      }
      else{
          updateFightingSfx(productName, publisherId,action);
      }
   })
 }
 
 
 function addCookieItem(productId, action){
     console.log('Customer Not logged in...')
 }
 
 function updateFightingSfx(productName, publisherId,action){ 
      var url = '/updatefightingsfx/'  
      fetch(url,{
         method:'POST',
         headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
  
         },
         body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action})  
      })                                                               
      .then((response) =>{
           return response.json()   
      })
      .then((data) =>{
           console.log('data:',data) 
           location.reload()
      })
  }
   
 