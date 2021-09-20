var updateBtns = document.getElementsByClassName('AudioPack-cart')
for (var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(){
     var productName = this.dataset.product
     var publisherId=this.dataset.pubid  
     var action = this.dataset.action
    // console.log('productName:', productName, 'action:', action)
    //console.log('USER:', user)  //inheriting user from base.html
     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         updateAudioPack(productName,publisherId, action);
     }
  })
}

function addCookieItem(productName, action){
    console.log('Customer Not logged in...')
}

function updateAudioPack(productName,publisherId, action){  //passing product id nad action as parameter
 
    //console.log("Sending ProductName and action")
     var url = '/updateSoundpack/'  //  Note mention the url not the name of url
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
 
 var updateBtns = document.getElementsByClassName('VfxPack-cart')
 for (var i=0; i<updateBtns.length; i++){
      updateBtns[i].addEventListener('click', function(){
      var productName = this.dataset.product
      var publisherId=this.dataset.pubid  
      var action = this.dataset.action
     // console.log('productName:', productName, 'action:', action)
     //console.log('USER:', user)  //inheriting user from base.html
      if(user == 'AnonymousUser'){  
          addCookieItem(productName, action)
      }
      else{
          updateVfxPack(productName,publisherId, action);
      }
   })
 }
 
 function addCookieItem(productName, action){
     console.log('Customer Not logged in...')
 }
 
 function updateVfxPack(productName,publisherId, action){  //passing product id nad action as parameter
  
      var url = '/updatevfxpack/'  
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

  var updateBtns = document.getElementsByClassName('FlimTransitionPack-cart')
  for (var i=0; i<updateBtns.length; i++){
       updateBtns[i].addEventListener('click', function(){
       var productName = this.dataset.product
       var publisherId=this.dataset.pubid  
       var action = this.dataset.action
      // console.log('productName:', productName, 'action:', action)
      //console.log('USER:', user)  //inheriting user from base.html
       if(user == 'AnonymousUser'){  
           addCookieItem(productName, action)
       }
       else{
           updateFlimtransitionPack(productName,publisherId, action);
       }
    })
  }
  
  function addCookieItem(productName, action){
      console.log('Customer Not logged in...')
  }
  
  function updateFlimtransitionPack(productName,publisherId, action){  //passing product id nad action as parameter
   
       var url = '/updateflimtransitionpack/'  
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
    
   var updateBtns = document.getElementsByClassName('MotionGraphicsPack-cart')
   for (var i=0; i<updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
        var productName = this.dataset.product
        var publisherId=this.dataset.pubid  
        var action = this.dataset.action
       // console.log('productName:', productName, 'action:', action)
       //console.log('USER:', user)  //inheriting user from base.html
        if(user == 'AnonymousUser'){  
            addCookieItem(productName, action)
        }
        else{
            updateMotionGraphicsPack(productName,publisherId, action);
        }
     })
   }
   
   function addCookieItem(productName, action){
       console.log('Customer Not logged in...')
   }
   
   function updateMotionGraphicsPack(productName,publisherId, action){  //passing product id nad action as parameter
    
        var url = '/updatemotiongraphicspack/'  
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
   