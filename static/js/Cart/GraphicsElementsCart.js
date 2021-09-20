var updateBtns = document.getElementsByClassName('Landscape-cart')
for (var i=0; i<updateBtns.length; i++){
     updateBtns[i].addEventListener('click', function(){
     var productName = this.dataset.product
     var publisherId=this.dataset.pubid
     var action = this.dataset.action


     if(user == 'AnonymousUser'){  
         addCookieItem(productName, action)
     }
     else{
         UpdateLandscape(productName,publisherId,action);
     }
  })
}

function addCookieItem(productName, action){
    console.log('Customer Not logged in...')
}

function UpdateLandscape(productName, publisherId,action){  
 

     var url = '/UpdateLandscape/'  
     fetch(url,{
        method:'POST',
        headers:{
           'Content-Type': 'application/json',
           'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productName': productName,'publisherId':publisherId, action: action})  
     })                                                                  
     .then((response) =>{
          return response.json()   //then we wanna send back the jsonresponse that we defined in updateItem function
     })
     .then((data) =>{
          console.log('data:',data)  //then we need to console to be able to see the JSONresponse (i.e data,Item was added.)
          location.reload()
     })
 }
 

 var updateBtns = document.getElementsByClassName('Character-cart')
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
         UpdateCharacter(productName, publisherId,action);
     }
  })
}

//ADDING INCREASE OR DECREASE ITEM FUNCITON IN CART
//FOR GUEST USERS
function addCookieItem(productName, publisherId,action){
    console.log('Customer Not logged in...')
}

function UpdateCharacter(productName, publisherId ,action){  //passing product id nad action as parameter
 
    //console.log("Sending ProductName and action")
     var url = '/UpdateCharacter/'  //  Note mention the url not the name of url
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
 
 var updateBtns = document.getElementsByClassName('Opticallens-cart')
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
          UpdateOpticallens(productName, publisherId,action);
      }
   })
 }

 //FOR GUEST USERS
 function addCookieItem(productName, publisherId,action){
     console.log('Customer Not logged in...')
 }
 
 function UpdateOpticallens(productName, publisherId ,action){  
  
      var url = '/UpdateOpticallens/'  
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