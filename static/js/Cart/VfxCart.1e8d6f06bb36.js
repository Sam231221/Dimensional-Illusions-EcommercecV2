var updateBtns = document.getElementsByClassName('electricityvfx-cart')
for (var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productName = this.dataset.product
        var publisherId=this.dataset.pubid     
        var action = this.dataset.action
        
     //console.log('productName:', productName, 'action:', action)
    //console.log('USER:', user)  //inheriting user from base.html
     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         updateElectricityVfx(productName,publisherId, action);
     }
  })
}

function addCookieItem(productId, action){
    console.log('Customer Not logged in...')
}

function updateElectricityVfx(productName,publisherId, action){  //passing product id nad action as parameter
 
  //  console.log("Sending ProductName and action")
     var url = '/updateelectricityvfx/'  //it's a view u created which we are gonna pass product id and action.
     fetch(url,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken,
 
        },
        body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action})  //body is a data we wannsa send we r sending productid and action as a string
     })                                                                  //stringify is used for that
     .then((response) =>{
          return response.json()   //then we wanna send back the jsonresponse that we defined in updateItem function
     })
     .then((data) =>{
          console.log('data:',data)  //then we need to console to be able to see the JSONresponse (i.e data,Item was added.)
          location.reload()
     })
 }
 
var updateBtns = document.getElementsByClassName('EnergyVfx-cart')
for (var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(){
     var productName = this.dataset.product
     var publisherId=this.dataset.pubid     
     var action = this.dataset.action

     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         updateEnergyVfx(productName, publisherId,action);
     }
  })
}

function addCookieItem(productid, action){
    console.log('Customer Not logged in...')
}

function updateEnergyVfx(productName,publisherId,action){  //passing product id nad action as parameter
  // console.log("Sending ProductName and action")
     var url = '/updateenergyvfx/'  //it's a view u created which we are gonna pass product id and action.
     fetch(url,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action})  //body is a data we wannsa send we r sending productid and action as a string
     })                                                                  //stringify is used for that
     .then((response) =>{
          return response.json()   //then we wanna send back the jsonresponse that we defined in updateItem function
     })
     .then((data) =>{
          console.log('data:',data)  //then we need to console to be able to see the JSONresponse (i.e data,Item was added.)
          location.reload()
     })
 }
 
 var updateBtns = document.getElementsByClassName('Muzzleflashes-cart')
 for (var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(){
         var productName = this.dataset.product
         var publisherId=this.dataset.pubid     
        var action = this.dataset.action
      //console.log('productName:', productName, 'action:', action)
     //console.log('USER:', user)  //inheriting user from base.html
      if(user == 'AnonymousUser'){  
          addCookieItem(productName, action)
      }
      else{
          updateMuzzlefashesvfx(productName,publisherId, action);
      }
   })
 }
 
 function addCookieItem(productId, action){
     console.log('Customer Not logged in...')
 }
 
 function updateMuzzlefashesvfx(productName, publisherId,action){  //passing product id nad action as parameter
  
   //  console.log("Sending ProductName and action")
      var url = '/updatemuzzleflashvfx/'  //it's a view u created which we are gonna pass product id and action.
      fetch(url,{
         method:'POST',
         headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
  
         },
         body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action})  //body is a data we wannsa send we r sending productid and action as a string
      })                                                                  //stringify is used for that
      .then((response) =>{
           return response.json()   //then we wanna send back the jsonresponse that we defined in updateItem function
      })
      .then((data) =>{
           console.log('data:',data)  //then we need to console to be able to see the JSONresponse (i.e data,Item was added.)
           location.reload()
      })
  }
  
  var updateBtns = document.getElementsByClassName('Shockwaves-cart')
 for (var i=0; i<updateBtns.length; i++){
      updateBtns[i].addEventListener('click', function(){
      var productName = this.dataset.product
      var publisherId=this.dataset.pubid     
      var action = this.dataset.action
      //console.log('productName:', productName, 'action:', action)
     //console.log('USER:', user)  //inheriting user from base.html
      if(user == 'AnonymousUser'){  
          addCookieItem(productName, action)
      }
      else{
          updateShockwavesVfx(productName,publisherId, action);
      }
   })
 }
 
 function addCookieItem(productid, action){
     console.log('Customer Not logged in...')
 }
 
 function updateShockwavesVfx(productName,publisherId, action){  //passing product id nad action as parameter
   // console.log("Sending ProductName and action")
      var url = '/updateshockwavevfx/'  //it's a view u created which we are gonna pass product id and action.
      fetch(url,{
         method:'POST',
         headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
  
         },
         body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action})  //body is a data we wannsa send we r sending productid and action as a string
      })                                                                  //stringify is used for that
      .then((response) =>{
           return response.json()   //then we wanna send back the jsonresponse that we defined in updateItem function
      })
      .then((data) =>{
           console.log('data:',data)  //then we need to console to be able to see the JSONresponse (i.e data,Item was added.)
           location.reload()
      })
  }

var updateBtns = document.getElementsByClassName('Particlesvfx-cart')
for (var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productName = this.dataset.product
        var publisherId=this.dataset.pubid     
        var action = this.dataset.action
     //console.log('productName:', productName, 'action:', action)
    //console.log('USER:', user)  //inheriting user from base.html
     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         updateParticlesvfx(productName, publisherId,action);
     }
  })
}

function addCookieItem(productId, action){
    console.log('Customer Not logged in...')
}

function updateParticlesvfx(productName, publisherId,action){  //passing product id nad action as parameter
 
  //  console.log("Sending ProductName and action")
     var url = '/updateparticlevfx/'  //it's a view u created which we are gonna pass product id and action.
     fetch(url,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken,
 
        },
        body:JSON.stringify({'productName': productName, 'publisherId':publisherId,action: action})  //body is a data we wannsa send we r sending productid and action as a string
     })                                                                  //stringify is used for that
     .then((response) =>{
          return response.json()   //then we wanna send back the jsonresponse that we defined in updateItem function
     })
     .then((data) =>{
          console.log('data:',data)  //then we need to console to be able to see the JSONresponse (i.e data,Item was added.)
          location.reload()
     })
 }
 
var updateBtns = document.getElementsByClassName('EnvironmentVfx-cart')
for (var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(){
     var productName = this.dataset.product
     var publisherId=this.dataset.pubid     
     var action = this.dataset.action
     //console.log('productName:', productName, 'action:', action)
    //console.log('USER:', user)  //inheriting user from base.html
     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         updateEnvironmentVfx(productName, publisherId,action);
     }
  })
}

function addCookieItem(productid, action){
    console.log('Customer Not logged in...')
}

function updateEnvironmentVfx(productName, publisherId,action){  //passing product id nad action as parameter
   // console.log("Sending ProductName and action")

     var url = '/updateenvironmentalvfx/'  //it's a view u created which we are gonna pass product id and action.
     fetch(url,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken,
 
        },
        body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action})  //body is a data we wannsa send we r sending productid and action as a string
     })                                                                  //stringify is used for that
     .then((response) =>{
          return response.json()   //then we wanna send back the jsonresponse that we defined in updateItem function
     })
     .then((data) =>{
          console.log('data:',data)  //then we need to console to be able to see the JSONresponse (i.e data,Item was added.)
          location.reload()
     })
 }
 
 var updateBtns = document.getElementsByClassName('DebrisAndCrackvfx-cart')
 for (var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(){
         var productName = this.dataset.product
         var publisherId=this.dataset.pubid     
      var action = this.dataset.action
      if(user == 'AnonymousUser'){  
          addCookieItem(productName, action)
      }
      else{
          updateDebrisandCracksvfx(productName,publisherId, action);
      }
   })
 }
 
 function addCookieItem(productId, action){
     console.log('Customer Not logged in...')
 }
 
 function updateDebrisandCracksvfx(productName, publisherId,action){  //passing product id nad action as parameter
  
   //  console.log("Sending ProductName and action")
      var url = '/updatedebrisandcrackvfx/'  //it's a view u created which we are gonna pass product id and action.
      fetch(url,{
         method:'POST',
         headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
  
         },
         body:JSON.stringify({'productName': productName, 'publisherId':publisherId,action: action})  //body is a data we wannsa send we r sending productid and action as a string
      })                                                                  //stringify is used for that
      .then((response) =>{
           return response.json()   //then we wanna send back the jsonresponse that we defined in updateItem function
      })
      .then((data) =>{
           console.log('data:',data)  //then we need to console to be able to see the JSONresponse (i.e data,Item was added.)
           location.reload()
      })
  }
  
    
  
 